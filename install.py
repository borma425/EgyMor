import os
import time
from sources import *

print "[1] for kali"
print "[2] for termux"
tool = raw_input("protocol ==> ")
   
if tool == "1" or tool == "01":
     kali_user()
elif tool == "2" or tool == "02":
     termux_user()
