
fobj = open("config.txt", "r")
i=-1
read=[0,0,0,0,0,0]
help=[0,1,2,3,4,5,6,7,8,9,10,11]
farbe=[0,1,2,3,4,5,6,7,8,9,10,11]

def strtointarr(arr):
        s=arr.split(",")
        a=[0,0,0]
        for i in range(0,3,1):
                a[i]=int(s[i])
        return a



for line in fobj:
   if i>-1 and i<6:
      line.rstrip()
      waste,read[i]=line.split("=")
      print(read[i])
   if i>6 and i<19:
      line.rstrip()
      waste,help[i-7]=line.split("=")
      farbe[i-7]=strtointarr(help[i-7])
      print(i)
      print(farbe[i-7])
   i+=1
fobj.close()


