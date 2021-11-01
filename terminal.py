import os 
import time
import pynput
import datetime
import psutil
import platform
import webbrowser
import random
import GPUtil
import cpuinfo
import string
import colorama
import ctypes
import sys
from os import * 
from colorama import init
from win32api import GetSystemMetrics
from pynput.keyboard import Key, Listener
from pynput import *

init()

class c:
	grey = '\033[1;30;40m'
	red = '\033[1;31;40m'
	dark_red = '\033[2;31;40m'
	green  = '\033[1;32;40m'
	yellow  = '\033[1;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.275)

def main():
	def hack():
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""\033[1;32;40m
			┌─┐┌┐┌┌┬┐┌─┐┬─┐┬┌┐┌┌─┐  ┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐  ┌┬┐┌─┐┌┬┐┌─┐
			├┤ │││ │ ├┤ ├┬┘│││││ ┬  ├─┤├─┤│  ├┴┐├┤ ├┬┘  ││││ │ ││├┤ 
			└─┘┘└┘ ┴ └─┘┴└─┴┘└┘└─┘  ┴ ┴┴ ┴└─┘┴ ┴└─┘┴└─  ┴ ┴└─┘─┴┘└─┘o
	""")
		time.sleep(0.35)
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""\033[1;32;40m
			┌─┐┌┐┌┌┬┐┌─┐┬─┐┬┌┐┌┌─┐  ┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐  ┌┬┐┌─┐┌┬┐┌─┐
			├┤ │││ │ ├┤ ├┬┘│││││ ┬  ├─┤├─┤│  ├┴┐├┤ ├┬┘  ││││ │ ││├┤ 
			└─┘┘└┘ ┴ └─┘┴└─┴┘└┘└─┘  ┴ ┴┴ ┴└─┘┴ ┴└─┘┴└─  ┴ ┴└─┘─┴┘└─┘oo
	""")
		time.sleep(0.35)
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""\033[1;32;40m
			┌─┐┌┐┌┌┬┐┌─┐┬─┐┬┌┐┌┌─┐  ┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐  ┌┬┐┌─┐┌┬┐┌─┐
			├┤ │││ │ ├┤ ├┬┘│││││ ┬  ├─┤├─┤│  ├┴┐├┤ ├┬┘  ││││ │ ││├┤ 
			└─┘┘└┘ ┴ └─┘┴└─┴┘└┘└─┘  ┴ ┴┴ ┴└─┘┴ ┴└─┘┴└─  ┴ ┴└─┘─┴┘└─┘ooo
	""")
		time.sleep(0.35)
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""\033[1;32;40m
                                ┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐  ┌┬┐┌─┐┌┬┐┌─┐
                                ├─┤├─┤│  ├┴┐├┤ ├┬┘  ││││ │ ││├┤
                                ┴ ┴┴ ┴└─┘┴ ┴└─┘┴└─  ┴ ┴└─┘─┴┘└─┘
                                """)
		print("")
		victim = input("person to hack: ")
		print(f"hacking {victim}...")
		time.sleep(1.5)
		print(f"Gathering {victim}'s data")
		time.sleep(1.5)
		print(f"Stealing all {victim}'s money")
		time.sleep(1.5)
		print("")
		print(f"Successfully hacked {victim}")
		print("")


	a = os.getlogin()
	os_name = platform.system()
	os_release = platform.release()
	grey = '\033[1;30;40m'
	red = '\033[0;31;40m'
	command = input(f"{a}@{os_name}:~$ ")
	valid_commands = ['cls',
                                'cd',
                                'clear',
                                'neofetch',
                                'dir',
                                'help',
                                'time',
                                'date',	
                                '',
                                ' ',
                                'info',
                                'report',
                                'search',
                                'ping',
                                'exit']
	if command == 'cls':
		os.system('cls' if os.name == 'nt' else 'clear')
		main()
	elif command == 'clear':
		os.system('cls' if os.name == 'nt' else 'clear')
		main()
	elif command == 'neofetch':
		cpu = cpuinfo.get_cpu_info()['brand_raw']
		width = GetSystemMetrics(0)
		height = GetSystemMetrics(1)
		if os_name == 'Windows' or 'windows':
			lib = ctypes.windll.kernel32
			t = lib.GetTickCount64()
			t = int(str(t)[:-3])
			mins, sec = divmod(t, 60)
			hour, mins = divmod(mins, 60)
			days, hour = divmod(hour, 24)
			print(f"""

	                               \033[1;36;40m..,    \033[1;36;40mjackk\033[1;37;40m@\033[1;36;40m{os_name}
	\033[1;36;40m		    ....,,:;+ccllll
	\033[1;36;40m      ...,,+:;  cllllllllllllllllll   OS: \033[1;37;40m{os_name} {os_release}
	\033[1;36;40m,cclllllllllll  lllllllllllllllllll   Host: \033[1;37;40mMWIP
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   Kernel: \033[1;37;40mWIP
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   Uptime: \033[1;37;40m{days} day(s), {hour:02} hours, {mins:02} mins
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   Packages: \033[1;37;40mWIP
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   Shell: \033[1;37;40mSmiley terminal 2021
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   Resolution: \033[1;37;40m{width}x{height}
										
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   Terminal: \033[1;37;40mSmiley
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   WM: \033[1;37;40mWIP
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   WM Theme: \033[1;37;40mWIP
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   CPU: \033[1;37;40m{cpu}
	\033[1;36;40mllllllllllllll  lllllllllllllllllll   GPU: \033[1;37;40m WIP
	\033[1;36;40m`'ccllllllllll  lllllllllllllllllll   Memory: \033[1;37;40m{round(psutil.virtual_memory().total/1000000000, 2)} GB
	\033[1;36;40m       `' \*::  :ccllllllllllllllll
	\033[1;36;40m                       ````''*::cll
	\033[1;36;40m                               ``


		""")
		main()
	elif command == 'tree':
		system('tree')
		main()
	elif command == 'dir':
		system('dir')
		main()
	elif command == 'help':
		print("""Commands:
\033[1;36;40mcls - \033[1;37;40mClears screen
\033[1;36;40mcd - \033[1;37;40mShows current directory
\033[1;36;40mclear - \033[1;37;40mSame as cls
\033[1;36;40mneofetch - \033[1;37;40mDisplays system info
\033[1;36;40mdir - \033[1;37;40mShows all files in current directory 
\033[1;36;40mhelp - \033[1;37;40mTakes you here 
\033[1;36;40minfo - \033[1;37;40mGives a little more info about this project
\033[1;36;40mreport - \033[1;37;40mReport any bugs
\033[1;36;40msearch - \033[1;37;40mOpen a url onto a new tab
\033[1;36;40mping - \033[1;37;40mPings specified IP/website/server
\033[1;36;40mrandstr - \033[1;37;40moutputs a random string (combination of letters and numbers)
\033[1;36;40mrandint - \033[1;37;40moutputs a random string of numbers (numbers only)
\033[1;36;40mexit - \033[1;37;40mExits the terminal (pressing ctrl + c does the same thing)
	""")
		print("Just a quick heads up, the commands are case sensitive, e.g. if you type neofetch with a space at the end it wont work")
		print("")
		main()
	elif command =='cd':
		os.system('cd')
		main()
	elif command == '?':
		print("""Commands:
\033[1;36;40mcls - \033[1;37;40mClears screen
\033[1;36;40mcd - \033[1;37;40mShows current directory
\033[1;36;40mclear - \033[1;37;40mSame as cls
\033[1;36;40mneofetch - \033[1;37;40mDisplays system info
\033[1;36;40mdir - \033[1;37;40mShows all files in current directory 
\033[1;36;40mhelp - \033[1;37;40mTakes you here 
\033[1;36;40minfo - \033[1;37;40mGives a little more info about this project
\033[1;36;40mreport - \033[1;37;40mReport any bugs
\033[1;36;40msearch - \033[1;37;40mOpen a url onto a new tab
\033[1;36;40mping - \033[1;37;40mPings specified IP/website/server
\033[1;36;40mrandstr - \033[1;37;40moutputs a random string (combination of letters and numbers)
\033[1;36;40mrandint - \033[1;37;40moutputs a random string of numbers (numbers only)
\033[1;36;40mexit - \033[1;37;40mExits the terminal (pressing ctrl + c does the same thing)
	""")
		print("Just a quick heads up, the commands are case sensitive, e.g. if you type neofetch with a space at the end it wont work")
		print("")
		main()
	elif command == 'info':
		os.system('cls' if os.name == 'nt' else 'clear')
		print("You are currently using smiley terminal")
		print("It is alternative to your OS's terminal")
		print("It is still in development so please report any bugs by typing 'report'")
		print("All commands can be found by typing 'help'")
		main()
	elif command == 'report':
		print("you can report any bugs on our discord server")
		print("https://discord.gg/NSU4pUnEQS")
		main()
	elif command == 'search':
		site = input("link: ")
		webbrowser.open_new_tab(site)
		main()
	elif command == 'ping':
		ip = input("Target: ")
		system(f'ping {ip}')
		main()
	elif command ==	'randint':
		print(random.randint(0, 1000))
		main()
	elif command == 'randstr':
		print("".join(random.choices(string.ascii_lowercase + string.digits, k = 10)))
		main()
	elif command == 'banner':
		print("""
                    _   _                
                   (_) | |               
  ___   _ __ ___    _  | |   ___   _   _ 
 / __| | '_ ` _ \  | | | |  / _ \ | | | |
 \__ \ | | | | | | | | | | |  __/ | |_| |
 |___/ |_| |_| |_| |_| |_|  \___|  \__, |
                                    __/ |
                                   |___/ 

""")
		main()
	elif command ==	'reload':
		system('start terminal.py')
		exit()
	elif command == 'hack':
		hack()
		main()
	elif command == '':
		main()
	elif command == ' ':
		main()
	if ' ' in command:
		pass
	if '	' in command:
		main()
	elif command not in valid_commands:
		print(f"\033[1;32;40m{command} is not recognized as an internal or external command {c.white}")
		main()


		
main()
