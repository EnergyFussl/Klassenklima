fobj = open("config.txt", "r")
i=-1
read=[0,0,0,0,0,0]
for line in fobj:
   if i>-1:
      line.rstrip()
      waste,read[i]=line.split("=")
      print(read[i])
   i+=1
fobj.close()
