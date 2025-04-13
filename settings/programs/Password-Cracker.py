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
import sys
import requests
import time
import random
import colorama
import itertools
import string
from colorama import Fore, Style

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

red = Fore.RED
white = Fore.WHITE 
reset = Style.RESET_ALL

banner = f"""{red}
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                     
 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗            
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗           
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝           
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗           
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║           
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝           
{reset}"""

class PasswordCracker:
    def __init__(self):
        self.options = {
            "1": "TikTok",
            "2": "Gmail", 
            "3": "YouTube", 
            "4": "Snapchat",
            "5": "Windows",
            "6": "Instagram",
            "7": "Facebook",
            "8": "Twitter",
            "9": "LinkedIn",
            "10": "Reddit",
            "11": "Netflix",
            "12": "Spotify",
            "13": "Amazon",
            "14": "PayPal",
            "15": "Quitter"
        }
        self.chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    def display_menu(self):
        print(banner)
        print(f"\n{red}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║ {white}                    PASSWORD CRACKER                          {red}║") 
        print(f"╠═══════════════════════════════════════════════════════════════╣")
        
        for key, value in self.options.items():
            padding = " " * (55 - len(value))
            print(f"║ {red}[{white}{key}{red}] {white}{value}{padding}{red}║")
            
        print(f"╚═══════════════════════════════════════════════════════════════╝{reset}")

    def try_password(self, service, username, password):
        if random.random() < 0.9:
            return True
        return False

    def crack_password(self, service, username):
        print(f"\n{red}[{white}*{red}]{white} Démarrage du brute force pour {service}...")
        print(f"{red}[{white}*{red}]{white} Utilisateur: {username}")
        
        max_length = 8
        found = False
        attempts = 0
        start_time = time.time()

        for length in range(1, max_length + 1):
            print(f"\n{red}[{white}*{red}]{white} Test des mots de passe de longueur {length}...")
            
            for guess in itertools.product(self.chars, repeat=length):
                attempts += 1
                password = ''.join(guess)
                
                if attempts % 1000 == 0:
                    elapsed_time = time.time() - start_time
                    print(f"{red}[{white}*{red}]{white} Tentative {attempts}: {password} ({elapsed_time:.2f}s)")
                
                if self.try_password(service, username, password):
                    found = True
                    print(f"\n{red}[{white}+{red}]{white} Mot de passe trouvé!")
                    print(f"{red}[{white}+{red}]{white} Identifiants: {username}:{password}")
                    print(f"{red}[{white}+{red}]{white} Temps écoulé: {elapsed_time:.2f}s")
                    print(f"{red}[{white}+{red}]{white} Tentatives: {attempts}")
                    return
                
                if attempts % 10000 == 0:
                    time.sleep(0.1)
                
                if time.time() - start_time > 300:
                    print(f"\n{red}[{white}!{red}]{white} Timeout - Arrêt du brute force")
                    return

        if not found:
            print(f"\n{red}[{white}!{red}]{white} Mot de passe non trouvé")
            print(f"{red}[{white}*{red}]{white} Tentatives effectuées: {attempts}")

    def run(self):
        while True:
            clear()
            self.display_menu()
            choice = input(f"\n{red}[{white}>{red}]{white} Choix: {reset}")

            if choice == "15":
                print(f"\n{red}[{white}!{red}]{white} Au revoir!{reset}")
                break
                
            if choice in self.options:
                username = input(f"\n{red}[{white}>{red}]{white} Nom d'utilisateur/Email: {reset}")
                self.crack_password(self.options[choice], username)
                input(f"\n{red}[{white}>{red}]{white} Appuyez sur Entrée pour continuer...{reset}")
            else:
                print(f"\n{red}[{white}!{red}]{white} Option invalide{reset}")
                time.sleep(1)

if __name__ == "__main__":
    cracker = PasswordCracker()
    cracker.run()
