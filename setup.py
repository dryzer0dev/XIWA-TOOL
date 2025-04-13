import os
import subprocess
import time
from colorama import Fore, Style, init

init()
red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

def progress_bar(progress, total, width=50):
    filled = int(width * progress // total)
    bar = f"{red}█{reset}" * filled + f"{white}█{reset}" * (width - filled)
    percent = progress / total * 100
    return f"{red}[{reset}{bar}{red}] {white}{percent:.1f}%{reset}"

print(f"\n{red}[{white}+{red}]{white} Installation des modules nécessaires...{reset}\n")

with open('requirements.txt') as f:
    modules = f.read().splitlines()

total_modules = len(modules)
for i, module in enumerate(modules, 1):
    try:
        print(progress_bar(i, total_modules))
        subprocess.check_call(['pip', 'install', module], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{red}[{white}✓{red}]{white} {module}{reset}")
    except:
        print(f"{red}[{white}!{red}]{white} Erreur: {module}{reset}")
    time.sleep(0.1)

print(f"\n{red}[{white}+{red}]{white} Installation terminée !{reset}")
time.sleep(1)

print(f"\n{red}[{white}*{red}]{white} Lancement de XIWA...{reset}")
time.sleep(1)

subprocess.Popen(['python', 'main.py'])
