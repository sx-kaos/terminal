import os 
import time
import pynput
import datetime
import time
import psutil
import platform
import webbrowser
from datetime import *
import random
import GPUtil
import cpuinfo
import string
import colorama
import ctypes
import sys
from time import sleep
from os import *
from colorama import init
from win32api import GetSystemMetrics
from alive_progress import alive_bar
from halo import Halo

#gathering all system information needed
class needed():
    ctypes.windll.kernel32.SetConsoleTitleW(f" ")
    spinner = Halo(text='Loading', spinner='dots', color = 'cyan') #front end
    spinner.start() #loading screen whilst gathering system info
    today = date.today()
    now = datetime.now()
    date = today.strftime("%B %d, %Y")
    username = os.getlogin()
    os_name = platform.system()
    os_release = platform.release()
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    monitor_width = GetSystemMetrics(0)
    monitor_height = GetSystemMetrics(1)
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    ram = round(psutil.virtual_memory().total/1000000000, 2) #in Gigabytes
    spinner.stop() # stop loading screen once system info gathered
    os.system('cls' if os.name == 'nt' else 'clear')

#colors using ansi escape sequences
class c:
	grey = '\033[1;30;40m'
	red = '\033[1;31;40m'
	dark_red = '\033[2;31;40m'
	green = '\033[1;32;40m'
	yellow = '\033[0;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'
	black = '\033[1;30;40m'

#terminal style typing
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep((random.randrange(0.001, 0.275)))

print(f"""
{c.cyan}╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
{c.cyan}│    {c.white}__                                                                      {c.cyan}│
{c.cyan}│   {c.white}/ /  __  __   ____   ____ _   _____                                      {c.cyan}│
{c.cyan}│  {c.white}/ /  / / / /  / __ \ / __ `/  / ___/      Welcome to lunar                {c.cyan}│
{c.cyan}│ {c.white}/ /  / /_/ /  / / / // /_/ /  / /          Type help for a list of cmds    {c.cyan}│
{c.cyan}│{c.white}/_/   \____/  /_/ /_/ \____/  /_/                                           {c.cyan}│
{c.cyan}│                                                                            {c.cyan}│
{c.cyan}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
""")
def main():
	try:
		print(f"{c.white}╭{needed.username}@lunar")
		command = input(f"{c.white}╰─→ ")
		valid = ['neofetch',
				 'help',
				 'cls',
				 'ipconfig'
				 'ifconfig',
				 'clear',
				 'date',
				 'exit',
				 'time',
				 'cd',
				 'nslookup',
				 'google',
				 'ping',
				 'dir',
				 '',
				 '	']
		if command == 'cls':
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""
{c.cyan}╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
{c.cyan}│    {c.white}__                                                                      {c.cyan}│
{c.cyan}│   {c.white}/ /  __  __   ____   ____ _   _____                                      {c.cyan}│
{c.cyan}│  {c.white}/ /  / / / /  / __ \ / __ `/  / ___/      Welcome to lunar                {c.cyan}│
{c.cyan}│ {c.white}/ /  / /_/ /  / / / // /_/ /  / /          Type help for a list of cmds    {c.cyan}│
{c.cyan}│{c.white}/_/   \____/  /_/ /_/ \____/  /_/                                           {c.cyan}│
{c.cyan}│                                                                            {c.cyan}│
{c.cyan}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
	""")
			main()
		elif command == '':
			main()
		elif command == 'clear':
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""
{c.cyan}╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
{c.cyan}│    {c.white}__                                                                      {c.cyan}│
{c.cyan}│   {c.white}/ /  __  __   ____   ____ _   _____                                      {c.cyan}│
{c.cyan}│  {c.white}/ /  / / / /  / __ \ / __ `/  / ___/      Welcome to lunar                {c.cyan}│
{c.cyan}│ {c.white}/ /  / /_/ /  / / / // /_/ /  / /          Type help for a list of cmds    {c.cyan}│
{c.cyan}│{c.white}/_/   \____/  /_/ /_/ \____/  /_/                                           {c.cyan}│
{c.cyan}│                                                                            {c.cyan}│
{c.cyan}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
	""")
			main()
		elif command == 'neofetch':
			print(f"╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
			print(f" {c.cyan}OS:{c.white} {needed.os_name} {needed.os_release}")
			print(f" {c.cyan}Uptime:{c.white} {needed.days} Day(s), {needed.hour:02} Hour(s), {needed.mins:02} Min(s)")
			print(f" {c.cyan}Resolution:{c.white} {needed.monitor_width}x{needed.monitor_height}")
			print(f" {c.cyan}CPU:{c.white} {needed.cpu}")
			print(f" {c.cyan}RAM:{c.white} {needed.ram}GB")
			print(f"{c.white}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
			main()
		elif command == 'help':
			print(f"help - shows all commands")
			print(f"neofetch - displays (some) system information")
			print(f"cls/clear - clears the window")
			print(f"date/time - displays date or time")
			print(f"ping - ping a domain or IP address")
			print(f"dir - displays all files in the current directory")
			print(f"google - searchs something in your installed webbrowser")
			print(f"ip/ifconfig - displays IP information")
			print(f"nslookup - lookup a domain or IP address")
			print(f"cd - change directory")
			print(f"exit - closes the terminal")
			main()
		elif command == 'date':
			print(f"{needed.date}")
			main()
		elif command == 'time':
			now = datetime.now()
			time2 = now.strftime("%H:%M:%S")
			print(f"{time2}")
			main()
		elif command == 'google':
			query = input("What do you want to search up? ")
			webbrowser.open_new_tab(query)
			main()
		elif command == 'ping':
			try:
				amount = int(input(f'How many times do you want to ping?: '))
				if amount == int(0):
					print(f'please enter an amount greater than zero')
					main()
				target = input("Target to ping: ")
				for i in range(int(amount)):
					os.system(f'PING -n 1 {target} | FIND "TTL="')
					os.system(f'IF ERRORLEVEL 1 (SET in=c & echo offline)')
					os.system(f'ping -t 2 0 10 127.0.0.1 >nul')
				main()
			except ValueError:
				print(f'{amount} is not a valid number, please try again')
				main()
			main()
		elif command == 'exit':
			exit()
		elif command == 'ifconfig':
			os.system('ipconfig /all')
			main()
		elif command == 'ipconfig':
			os.system('ipconfig /all')
			main()
		elif command == 'dir':
			arguments = input("Any arguments? ")
			os.system(f'dir {arguments}')
			main()
		elif command == 'cd':
			path = input("Path: ")
			try:
				os.chdir(path)
			except OSError:
				print("Invalid path")
			main()
		elif command == 'nslookup':
			target = input("IP/domain: ")
			if target == '':
				print(f"'{target}' is not a valid IP/domain")
				main()
			if target == ' ':
				print(f"'{target}' is not a valid IP/domain")
				main()
			if ' ' in target:
				print(f"'{target}' is not a valid IP/domain")
				main()
			system(f'nslookup {target}')
			main()
		elif command not in valid:
		    print(f"{command} is not recognised as a valid command")
		    main()
	except KeyboardInterrupt:
		print("^C")
		main()
main()
