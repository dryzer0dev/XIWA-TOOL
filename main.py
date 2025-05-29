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
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"""{red}
██╗  ██╗██╗██╗    ██╗ █████╗ 
╚██╗██╔╝██║██║    ██║██╔══██╗
 ╚███╔╝ ██║██║ █╗ ██║███████║
 ██╔██╗ ██║██║███╗██║██╔══██║
██╔╝ ██╗██║╚███╔███╔╝██║  ██║
╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
                                    {white}Version 0{reset}
                                    {red}XIWA OWNS YOU{reset}
""")

menus = {
    "1": {
        "title": "OUTILS DE BASE",
        "options": [
            "Website Vulnerability Scanner",
            "Info Stealer", 
            "Brute Force"
        ]
    },
    "2": {
        "title": "OUTILS AVANCES",
        "options": [
            "Server Scanner",
            "Phone Locator",
            "anonymization",
            "emoney control"
        ]
    },
    "3": {
        "title": "OUTILS DISCORD",
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
            "discord boost bot"
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
        "title": "OSINT AVANCE",
        "options": [
            "Identity Search",
            "Dox Creator"
        ]
    },
    "6": {
        "title": "CYBERATTAQUE",
        "options": [
            "Botnet Builder",
            "Ransomware Builder"
        ]
    },
    "7": {
        "title": "HACKING",
        "options": [
            "Network Scanner",
            "Password Cracker",
            "Exploit Framework",
            "Data Base Site Stealer",
            "piratattHack"
        ]
    }
}

def display_menu(menu_id):
    menu = menus[menu_id]
    print(f"\n{red}╭{'─' * 70}")
    print(f"{red}│ {white}{menu['title']}")
    print(f"{red}├{'─' * 70}")
    
    for i, option in enumerate(menu["options"], 1):
        if i == len(menu["options"]):
            print(f"{red}├─ {white}{i:02d} {red}│ {white}{option}")
        else:
            print(f"{red}├─ {white}{i:02d} {red}│ {white}{option}")
    
    print(f"{red}├─ {white}00 {red}│ {white}{'Retour'}")
    print(f"{red}└{'─' * 72}")

def main_loop():
    while True:
        banner()
        print(f"\n{red}╭{'─' * 50}")
        print(f"{red}│ {white}MENU PRINCIPAL")
        print(f"{red}├{'─' * 50}")
        for key, menu in menus.items():
            print(f"{red}├─ {white}{key} {red}│ {white}{menu['title']}")
        print(f"{red}└{'─' * 50}{reset}")

        menu_choice = input(f"\n{red}[{white}>{red}]{white} Choix du menu (1-7) : ").strip()
        if menu_choice not in menus:
            clear()
            continue

        while True:
            clear()
            banner()
            display_menu(menu_choice)
            
            max_options = len(menus[menu_choice]["options"])
            option_choice = input(f"\n{red}[{white}>{red}]{white} Choix de l'option (00-{max_options:02d}) : ").strip()
            
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
            banner()
            if os.path.exists(script_path):
                print(f"\n{red}[{white}*{red}]{white} Lancement de {selected_option}...")
                time.sleep(1)
                print(f"{red}[{white}+{red}]{white} Préparation des ressources...")
                time.sleep(1)
                clear()
                subprocess.run(["python", script_path])
                input(f"\n{red}[{white}>{red}]{white} Appuyez sur Entrée pour continuer...")
                clear()
            else:
                print(f"\n{red}[{white}!{red}]{white} Erreur : Le module '{selected_option}' n'est pas installé !{reset}")
                time.sleep(2)
                clear()

main_loop()