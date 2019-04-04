import os
import time
from sources import *
from time import sleep as timeout

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

def main():
      banner()
      print "\033[92m------------------------------------------------"
      print "\033[94m[01] tools metasploit"
      print "\033[92m------------------------------------------------"
      print "\033[94m[02] check sql web"
      print "\033[92m------------------------------------------------"
      print bcolors.BOLD + "\n   [10] Exit the MT\n" + bcolors.ENDC
      tool = raw_input("protocol ==> ")
  
      if tool == "1" or tool == "01":
           print "\033[92m-----------------------------------------"
           print "\033[94m(0) install metasploit"
           print "\033[92m-----------------------------------------"
           print "\033[94m(1) make payload"
           print "\033[92m-----------------------------------------"
           print "\033[94m(2) open listen session with metasploit"
           print "\033[92m-----------------------------------------"
           print "\033[94m(3) hack with ip"
           print "\033[92m-----------------------------------------"
           print "\033[94m(4) hack with link"
           print "\033[92m-----------------------------------------"
           print bcolors.BOLD + "\n   [00] Back to main menu\n" + bcolors.ENDC
           vun = raw_input("protocol ==> ")
           if vun == "0":
               metasploit()
           elif vun == "1" or vun == "01":
               mak_pylaod()
           elif vun == "2" or vun == "02":
               start_hacking()
           elif vun == "3" or vun == "03":
               scan_ip()
           elif vun == "4" or vun == "04":    
               print "\033[92m(1)first vulnerable"
               print "\033[92m(2)second vulnerable"
               print "\033[92m(3)third vulnerable"
               tol = raw_input("protocol ==> ")
               if tol == "1" or tol == "01":
                   link_hack()
               elif tol == "2" or tol == "02":
                   link_hack2()
               elif tol == "3" or tol == "03":
                   link_hack3()
				   
           elif tool == "2" or tool == "02":
                   sql_injection()
                   
           elif vun == "00" or vun == "0":
               restart_program()
   
      elif tool == "10":
           remove()
           sys.exit()
         
      elif start == "00":
           main()
           
if __name__ == "__main__":
        main()
