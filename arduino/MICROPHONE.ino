// Configuration of the pins
int analogPin = A0;
int digitalPin = 2;
int sensorValue = 0;
int rot = 12;
int blau = 13;
int gruen = 11;
 
void setup () 
{
  // write the correct pinMode
  pinMode(digitalPin, INPUT);
  pinMode(rot, OUTPUT);
  pinMode(gruen, OUTPUT);
  pinMode(blau, OUTPUT);
  
  Serial.begin (9600);
}
 
void loop () 
{
  // read the analogPin to check the current value of the microfon
  sensorValue = analogRead (analogPin);

  // enable the correct Port to output the proper color
  if (sensorValue <= 42) {
    digitalWrite(gruen, HIGH);
  }
  if (sensorValue > 42) {
    digitalWrite(gruen, LOW);
    digitalWrite(gruen, HIGH);
    digitalWrite(rot, HIGH);
    delay(1000);
  }
  if (sensorValue > 43) {
    digitalWrite(gruen, LOW);
    digitalWrite(rot, HIGH);
    delay(1000);
  }
  if (sensorValue < 42) {
    digitalWrite(rot, LOW);
  }
  // output the current value of the analog Pin to the serial monitor
  Serial.println (sensorValue, DEC);
}

