apt-get update && apt-get install sudo nano python python3 -y
sudo apt-get install libglib2.0-0 libglib2.0-dev -y
sudo apt-get install libdbus-1-dev -y
sudo apt-get install libudev-dev -y
sudo apt-get install libical-dev -y
sudo apt-get install libreadline-dev -y
sudo apt-get install libusb-1.0-0-dev -y
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.32.tar.xz
tar -xf bluez-5.32.tar.xz
cd bluez-5.32
./configure
make
make install
sudo apt-get install python3-pymysql -y
sudo apt-get install git
sudo pip3 install pygal
sudo pip3 install cairosvg
sudo pip3 install plotly
rm -fr install-requirements.sh
cd