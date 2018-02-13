import urllib.request
import urllib.parse

url = 'http://10.2.254.36'
try:
    print("test")
    f = urllib.request.urlopen(url)
    arr=(f.read().decode('utf-8'))
    print(arr)
    waste,arr=arr.split("<html>")
    print(arr)
    co2,temp=arr.split(":")
    print(co2)
    print(temp)
except:
    print("error: no connection to sensor")
