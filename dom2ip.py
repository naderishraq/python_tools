#!/user/bin/python3
# domain to ip finder tools


import socket
import pyfiglet 
from termcolor import colored
banner = colored(pyfiglet.figlet_format("Dom 2 Ip Finder Tools"),'green')

print(banner)


print(colored(("CREATED BY SA\/3 p|-|r0|\/| |)Ar|<"),'red'))

domain_name = input(colored("Enter Your Target Domain Name :",'yellow'))

ip = socket.gethostbyname(domain_name)

print(ip,)


