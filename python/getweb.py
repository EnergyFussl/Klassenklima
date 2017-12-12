import urllib.request
import urllib.parse

url = 'http://193.168.137.80'
try:
    print("test")
    f = urllib.request.urlopen(url)
    arr=(f.read().decode('utf-8'))
    waste,arr=arr.split("<html>")
    print(arr)
except:
    print("error: no connection to sensor")
