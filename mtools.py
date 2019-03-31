#by abdala
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
      print "[01] make payload"
      print "[02] start hacking with metasploit"
      print "[03] hack with ip"
      print "[04] hack with link"
      print "[05] check sql web"
      print bcolors.BOLD + "\n   [10] Exit the morocco tools\n" + bcolors.ENDC
      tool = raw_input("protocol ==> ")
  
      if tool == "1" or tool == "01":
           mak_pylaod()
           
      elif tool == "2" or tool == "02":
           start_hacking()
           
      elif tool == "3" or tool == "03":
           scan_ip()

      elif tool == "4" or tool == "04":
           link_hack()
           
      elif tool == "5" or tool == "05":
           sql_injection()
           
      elif tool == "10":
           remove()
           sys.exit()
         
      elif start == "00":
           main()
           
if __name__ == "__main__":
        main()
