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
        "title": "MENU PRINCIPAL", 
        "category": "Outils de Base",
        "options": [
            {"name": "Website-Vulnerability-Scanner", "desc": "Scanner de vulnérabilités web"},
            {"name": "id-lookup", "desc": "Recherche d'informations Discord"},
            {"name": "Token-Grabber", "desc": "Récupération de tokens"},
            {"name": "Info-Stealer", "desc": "Collecte d'informations"},
            {"name": "Brute-Force", "desc": "Bruteforce de comptes"}
        ]
    },
    "2": {
        "title": "OUTILS AVANCES",
        "category": "Fonctionnalités Avancées", 
        "options": [
            {"name": "Server-Scanner", "desc": "Analyse de serveurs"},
            {"name": "Bot-Creator", "desc": "Création de bots Discord"},
            {"name": "Mass-Report", "desc": "Système de signalement"},
            {"name": "Account-Nuker", "desc": "Gestion de comptes"},
            {"name": "Phone-Locator", "desc": "Localisation de numéros de téléphone"}
        ]
    },
    "3": {
        "title": "OUTILS DISCORD",
        "category": "Discord Utilities",
        "options": [
            {"name": "Webhook-Spammer", "desc": "Gestion de webhooks"},
            {"name": "Token-Checker", "desc": "Vérification de tokens"},
            {"name": "Member-Scraper", "desc": "Extraction de membres"},
            {"name": "Channel-Nuker", "desc": "Gestion de salons"},
            {"name": "Member-Trusser", "desc": "Gestion de membres"},
            {"name": "Propriety-transfert", "desc": "Gestion de la propriété"},
            {"name": "Server-Nuker", "desc": "Gestion de serveurs"},
            {"name": "rat", "desc": "Discord Rat (in dev)"},
            {"name": "Token-Grabber", "desc": "Récupération de tokens"},
            {"name": "nitro-auto-claim", "desc": "Auto-claim de nitro"},
        ]
    },
    "4": {
        "title": "OUTILS OSINT/CSINT",
        "category": "Recherche d'informations",
        "options": [
            {"name": "Phone-OSINT", "desc": "Recherche par numéro de téléphone"},
            {"name": "Email-OSINT", "desc": "Recherche par email"},
            {"name": "Username-OSINT", "desc": "Recherche par pseudo"},
            {"name": "IP-OSINT", "desc": "Recherche par adresse IP"},
            {"name": "Phone-Locator", "desc": "Localisateur de numéro de téléphone (in dev) (beta) (version 0)"}
        ]
    },
    "5": {
        "title": "OUTILS OSINT",
        "category": "Collecte d'informations",
        "options": [
            {"name": "Social-Scanner", "desc": "Scan des réseaux sociaux"},
            {"name": "Location-Finder", "desc": "Recherche de localisation"},
            {"name": "Data-Aggregator", "desc": "Agrégation de données"},
            {"name": "Identity-Search", "desc": "Recherche d'identité"},
            {"name": "dox-creator", "desc": "Création de dox"},
        ]
    },
    "6": {
        "title": "OUTILS de Cyberattaque",
        "category": "cyberattaque",
        "options": [
            {"name": "botnet-builder", "desc": "Cheat pour botnet"},
            {"name": "Ransomware-Builder", "desc": "Création de ransomware"},
        ],
    },
    "7": {
        "title": "OUTILS HACKING",
        "category": "Piratage et Sécurité",
        "options": [
            {"name": "Network-Scanner", "desc": "Scanner de réseaux"},
            {"name": "Password-Cracker", "desc": "Cassage de mots de passe"},
            {"name": "Exploit-Framework", "desc": "Framework d'exploitation"},
            {"name": "Malware-Creator", "desc": "Création de malwares"},
            {"name": "Backdoor-Generator", "desc": "Générateur de backdoors"},
            {"name": "Keylogger-Builder", "desc": "Création de keyloggers"},
            {"name": "Data-Base-Site-Stealer", "desc": "Récupération de données de sites web"},
            {"name": "Read-Database", "desc": "Lecture de bases de données"},
            {"name": "anonymization", "desc": "Anonymisation de l'identité"},
        ]
    }
}

def format_option(index, option):
    return f"{red}[{white}{index:02}{red}]{white} {option['name'].replace('-', ' ')} {red}| {white}{option['desc']}"

def display_menu(menu_id):
    menu = menus[menu_id]
    print(f"\n{red}╔═══════════════════════════════════════════════════════════════════════╗")
    print(f"{red}║ {white}• {menu['title']} - {menu['category']}{' ' * (45 - len(menu['title']) - len(menu['category']))}{red}║")
    print(f"{red}╠═══════════════════════════════════════════════════════════════════════╣")
    for i, option in enumerate(menu["options"], start=1):
        print(f"{red}║   {format_option(i, option)}{' ' * (60 - len(option['name']) - len(option['desc']))}{red}║")
    print(f"{red}║{' ' * 65}{red}║")
    print(f"{red}║   {format_option(0, {'name': 'Retour', 'desc': 'Revenir au choix du menu'})}{' ' * 31}{red}║")
    print(f"{red}╚═══════════════════════════════════════════════════════════════════════╝{reset}")

def main_loop():
    while True:
        banner()
        print(f"{red}[{white}!{red}]{white} SELECTION DU MENU :")
        for key, menu in menus.items():
            print(f"{red}[{white}{key}{red}]{white} {menu['title']} {red}| {white}{menu['category']}")

        menu_choice = input(f"\n{red}[{white}>{red}]{white} Choix du menu (1-6) : ").strip()
        if menu_choice not in menus:
            clear()
            continue

        while True:
            clear()
            banner()
            display_menu(menu_choice)
            
            max_options = len(menus[menu_choice]["options"])
            option_choice = input(f"\n{red}[{white}>{red}]{white} Choix de l'option (0-{max_options}) : ").strip()
            
            if not option_choice.isdigit() or int(option_choice) not in range(0, max_options + 1):
                clear()
                continue

            if option_choice == "0":
                clear()
                break

            option_index = int(option_choice) - 1
            selected_option = menus[menu_choice]["options"][option_index]["name"]
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
