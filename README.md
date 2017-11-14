Klassenklima
===================

Dieses Projekt wird als Diplomarbeit 2017/18 in der HTL Braunau von Lukas Friedl, Alexander Leimer und Martin Schachl ausgeführt.
In diesem Projekt soll es darum gehen, dass die Sensoren des **TI CC2650** und **MG811** ausgelesen und ausgewertet werden.
Die gesammelten Daten der Sensoren werden über Bluetooth und WLAN übertragen. Für die Messung des CO2 wird der **MG811** Sensor verwenden, da dieser nur über einen Analogausgang verfügt, wird das Signal von einem **NODE MCU ESP8266** digitalisiert und über WLAN an den Raspberry PI übertragen. Die restlichen Daten werden durch einen **TI CC2650** Sensortag über Bluetooth übertragen. Am Raspberry PI, der als Hauptrechner dient, werden die gesendeten Daten mit Hilfe eines Python Programmes ausgewertet, visualisiert und anschließend auf einen externen SQL Server übertragen.