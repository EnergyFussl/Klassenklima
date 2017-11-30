<?php
$servername = "localhost";
$username = "lfrie_sensoren";
$password = "dIea?163";
$dbname = "lfriedl_sensoren";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT Monthname(datum) AS `Monat`, ROUND(AVG(temp),2) AS `Temperatur` FROM klima group by Month(datum)";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        $data = array();
        foreach ($result as $row) {
                $data[] = $row;
        }
    }
} else {
    echo "0 results";
}
$conn->close();

$myJSON = json_encode($data);
echo $myJSON;


?>