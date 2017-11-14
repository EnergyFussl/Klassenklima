#include <ESP8266WiFi.h>

/* Hardware Related Defines */
#define MG_PIN                    (0)
#define BOOL_PIN                  (2)
#define DC_GAIN                   (8.5)

/* Software Related Defines */
#define READ_SAMPLE_INTERVAL      (50)
#define READ_SAMPLE_TIMES         (5)

/* Application Related Defines */
#define ZERO_POINT_VOLTAGE        (0.390)
#define REACTION_VOLTAGE          (0.020)

/* Global Variable */
float CO2Curve[3] = {2.602, ZERO_POINT_VOLTAGE, (REACTION_VOLTAGE / (2.602 - 3))};

const char* ssid = "Hotspot";//type your ssid
const char* password = "hotspot123";//type your password

// config static IP
IPAddress ip(192, 168, 0, 65); // where xx is the desired IP Address
IPAddress gateway(192, 168, 0, 1); // set gateway to match your network
IPAddress subnet(255, 255, 255, 0); // set subnet mask to match your network
IPAddress dns(192, 168, 0, 1);  // set dns server

int ledPin = 2; // GPIO2 of ESP8266
WiFiServer server(80);//Service Port


void setup() {


  /********************** MG811 Related ****************************/

  {
    Serial.begin(9600);                              //UART setup, baudrate = 9600bps
    pinMode(BOOL_PIN, INPUT);                        //set pin to input
    digitalWrite(BOOL_PIN, HIGH);                    //turn on pullup resistors

    Serial.print("MG-811 Demostration\n");
  }



  /********************** WLAN Related ****************************/

  Serial.begin(115200);
  delay(10);

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  // Wifi Modus AP Disable
  WiFi.mode(WIFI_STA);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // Set Static IP Address
  //WiFi.config(ip, dns, gateway, subnet);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");

}


void loop() {


  /********************** MG811 Related ****************************/

  int percentage;
  float volts;

  volts = MGRead(MG_PIN);
  Serial.print( "SEN-00007:" );
  Serial.print(volts);
  Serial.print( "V           " );

  percentage = MGGetPercentage(volts, CO2Curve);
  Serial.print("CO2:");
  if (percentage == -1) {
    Serial.print( "<400" );
  } else {
    Serial.print(percentage);
  }
  
  Serial.print( "ppm" );
  Serial.print("\n");

  if (digitalRead(BOOL_PIN) ) {
    Serial.print( "=====BOOL is HIGH======" );
  } else {
    Serial.print( "=====BOOL is LOW======" );
  }

  Serial.print("\n");

  delay(2000);



  /********************** WLAN Related ****************************/

  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }

  // Wait until the client sends some data
  Serial.println("new client");
  while (!client.available()) {
    delay(1);
  }

  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();

  // Match the request

  int value = LOW;
  if (request.indexOf("/LED=ON") != -1) {
    digitalWrite(ledPin, HIGH);
    value = HIGH;
  }
  if (request.indexOf("/LED=OFF") != -1) {
    digitalWrite(ledPin, LOW);
    value = LOW;
  }

  //Set ledPin according to the request
  //digitalWrite(ledPin, value);

  // Return the response
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");

  client.print("CO2-Sensordata: ");

  client.print(percentage);
  
/*
  if (value == LOW) {
    client.print("On");
  } else {
    client.print("Off");
  }
  client.println("<br><br>");
  client.println("Click <a href=\"/LED=ON\">here</a> turn the LED on pin 2 ON<br>");
  client.println("Click <a href=\"/LED=OFF\">here</a> turn the LED on pin 2 OFF<br>");
  client.println("</html>");
*/

  delay(1);
  Serial.println("Client disconnected");
  Serial.println("");
}




float MGRead(int mg_pin)
{
  int i;
  float v = 0;

  for (i = 0; i < READ_SAMPLE_TIMES; i++) {
    v += analogRead(mg_pin);
    delay(READ_SAMPLE_INTERVAL);
  }
  v = (v / READ_SAMPLE_TIMES) * 5 / 1024 ;
  v = v - 0.30;
  return v;
}

int MGGetPercentage(float volts, float *pcurve)
{
  if (((volts) / DC_GAIN ) >= ZERO_POINT_VOLTAGE) {
    Serial.print("IF GetPercentage\n");
    return -1;
  } else {
    return pow(10, ((volts / DC_GAIN) - pcurve[1]) / pcurve[2] + pcurve[0]);
  }
}










