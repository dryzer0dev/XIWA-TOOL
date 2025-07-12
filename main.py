"""
Copyright (c) 2025 Dryz3R - XiwA Tool
All rights reserved.

ENGLISH:
This software is the property of Dryz3R and is protected by copyright laws.
Unauthorized copying, distribution, or modification of this software is strictly prohibited.
XiwA Tool is a comprehensive security and analysis suite developed by Dryz3R.

FRANÇAIS:
Ce logiciel est la propriété de Dryz3R et est protégé par les lois sur le droit d'auteur.
La copie, la distribution ou la modification non autorisée de ce logiciel est strictement interdite.
XiwA Tool est une suite complète de sécurité et d'analyse développée par Dryz3R.

ESPAÑOL:
Este software es propiedad de Dryz3R y está protegido por las leyes de derechos de autor.
Se prohíbe estrictamente la copia, distribución o modificación no autorizada de este software.
XiwA Tool es una suite completa de seguridad y análisis desarrollada por Dryz3R.
"""

import os
import subprocess
from colorama import Fore, Style
import time

red = Fore.RED
white = Fore.WHITE
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_banner():
    clear()
    print(f"{red}")
    time.sleep(0.1)
    
    print(f"                                    ██╗  ██╗██╗██╗    ██╗ █████╗ ")
    time.sleep(0.05)
    print(f"                                    ╚██╗██╔╝██║██║    ██║██╔══██╗")
    time.sleep(0.05)
    print(f"                                     ╚███╔╝ ██║██║ █╗ ██║███████║")
    time.sleep(0.05)
    print(f"                                     ██╔██╗ ██║██║███╗██║██╔══██║")
    time.sleep(0.05)
    print(f"                                    ██╔╝ ██╗██║╚███╔███╔╝██║  ██║")
    time.sleep(0.05)
    print(f"                                    ╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝")
    time.sleep(0.1)
    
    print(f"                                {white}Advanced Security & Analysis Platform{reset}")
    time.sleep(0.05)
    print(f"                                        {red}Professional Edition v2.1{reset}")
    time.sleep(0.1)

def animate_menu():
    animate_banner()
    
    print(f"                                {red} ╔═══{' ' * 25}═══╗{reset}")
    time.sleep(0.05)
    
    for key, menu in menus.items():
        if key == "1":
            print(f"                                {red}    ({white}{int(key):02d}{red}) {white}> {menu['title']}{reset}")
        else:
            print(f"                                {red}     ({white}{int(key):02d}{red}) {white}> {menu['title']}{reset}")
        time.sleep(0.05)
    
    print(f"                                {red} ╚═══{' ' * 25}═══╝{reset}")
    time.sleep(0.1)

def animate_submenu(menu_id):
    animate_banner()
    
    menu = menus[menu_id]
    print(f"                                {red} ╔═══{' ' * 25}═══╗{reset}")
    time.sleep(0.05)
    
    for i, option in enumerate(menu["options"], 1):
        print(f"                                {red}    ({white}{i:02d}{red}) {white}> {option}{' ' * (25-len(option))}{red} {reset}")
        time.sleep(0.05)
    
    print(f"                                {red}    ({white}00{red}) {white}> Return to Main Menu{' ' * 5}{red} {reset}")
    time.sleep(0.05)
    print(f"                                {red} ╚═══{' ' * 25}═══╝{reset}")
    time.sleep(0.1)

menus = {
    "1": {
        "title": "SECURITY ASSESSMENT",
        "options": [
            "Website Vulnerability Scanner",
            "Info Stealer", 
            "Brute Force"
        ]
    },
    "2": {
        "title": "ADVANCED TOOLS",
        "options": [
            "Server Scanner",
            "Phone Locator",
            "Anonymization",
            "Financial Control"
        ]
    },
    "3": {
        "title": "DISCORD ANALYSIS",
        "options": [
            "Webhook Spammer",
            "Token Checker",
            "Member Scraper", 
            "Member Trusser",
            "Propriety Transfert",
            "Server Nuker",
            "Nitro Auto Claim",
            "ID Lookup",
            "Vocal DDoS",
            "Bot Creator",
            "Discord Boost Bot"
        ]
    },
    "4": {
        "title": "OSINT/CSINT",
        "options": [
            "Phone OSINT",
            "Email OSINT",
            "Username OSINT",
            "IP OSINT"
        ]
    },
    "5": {
        "title": "ADVANCED OSINT",
        "options": [
            "Identity Search",
            "Dox Creator"
        ]
    },
    "6": {
        "title": "CYBER ATTACK",
        "options": [
            "Botnet Builder",
            "Ransomware Builder"
        ]
    },
    "7": {
        "title": "PENETRATION TESTING",
        "options": [
            "Network Scanner",
            "Password Cracker",
            "Exploit Framework",
            "Data Base Site Stealer",
            "piratattHack"
        ]
    }
}

def main_loop():
    while True:
        animate_menu()
        
        menu_choice = input(f"\n{red}[{white}SELECT{red}]{white} Menu choice (1-7): ").strip()
        if menu_choice not in menus:
            clear()
            continue

        while True:
            clear()
            animate_submenu(menu_choice)
            max_options = len(menus[menu_choice]["options"])
            option_choice = input(f"\n{red}[{white}SELECT{red}]{white} Option choice (00-{max_options:02d}): ").strip()
            if not option_choice.isdigit() or int(option_choice) not in range(0, max_options + 1):
                clear()
                continue
            if option_choice == "0":
                clear()
                break
            option_index = int(option_choice) - 1
            selected_option = menus[menu_choice]["options"][option_index].replace(" ", "-")
            script_path = f"settings/programs/{selected_option}.py"
            clear()
            animate_banner()
            if os.path.exists(script_path):
                print(f"\n{green}[{white}INITIALIZING{green}]{white} Launching {selected_option}...")
                time.sleep(1)
                print(f"{green}[{white}LOADING{green}]{white} Preparing resources...")
                time.sleep(1)
                clear()
                subprocess.run(["python", script_path])
                input(f"\n{red}[{white}CONTINUE{red}]{white} Press Enter to continue...")
                clear()
            else:
                print(f"\n{red}[{white}ERROR{red}]{white} Module '{selected_option}' is not installed!{reset}")
                time.sleep(2)
                clear()

main_loop()