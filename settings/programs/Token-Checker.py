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

import discord
import requests
import random
import time
import os
import sys
import json
import base64
import sqlite3
import colorama
from colorama import Fore, Back, Style

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

banner = red + """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║  
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║  
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║  
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║  
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝  
                                               
        ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
       ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
       ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
       ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

prefix = red + "[" + white + "Token-Checker" + red + "]" + reset

def verify_token(token):
    if token:
        connection = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
        if connection.status_code == 200:
            print(prefix + " Token valide")
            return True
        else:
            print(prefix + " Token invalide")
            return False
    print(prefix + " Token invalide")
    return False

class TokenChecker:
    def __init__(self, token, proxy=None):
        self.token = token
        self.proxy = proxy
        
    def check_token(self):
        if not self.token:
            print(prefix + " Token invalide")
            return False
            
        proxies = None
        if self.proxy:
            if self.proxy.startswith(("http://", "https://")):
                proxies = {"http": self.proxy, "https": self.proxy}
            else:
                print(prefix + " Format de proxy invalide")
                return False
                
        try:
            response = requests.get(
                "https://discord.com/api/v9/users/@me",
                headers={"Authorization": self.token},
                proxies=proxies,
                timeout=10
            )
            if response.status_code == 200:
                print(prefix + " Token valide")
                return True
            else:
                print(prefix + " Token invalide")
                return False
        except:
            print(prefix + " Erreur lors de la vérification")
            return False

def display_menu():
    print(f"\n{red}╔══════════════════════════════════════════════════════════════════════════╗")
    print(f"{red}║{white}                     DISCORD TOKEN CHECKER                              {red}║")
    print(f"{red}║{white}                        Token Checker v1.0                             {red}║") 
    print(f"{red}╠══════════════════════════════════════════════════════════════════════════╣")
    print(f"{red}║                                                                          ║")
    print(f"{red}║  [{white}1{red}] {white}Vérifier un token simple                                          {red}║")
    print(f"{red}║  [{white}2{red}] {white}Vérifier avec proxy                                              {red}║")
    print(f"{red}║  [{white}3{red}] {white}Vérifier avec proxy + user-agent                                 {red}║")
    print(f"{red}║  [{white}4{red}] {white}Vérifier avec proxy + user-agent + IP                            {red}║")
    print(f"{red}║  [{white}5{red}] {white}Vérifier avec proxy + user-agent + IP + port                     {red}║")
    print(f"{red}║  [{white}6{red}] {white}Vérifier avec proxy + user-agent + IP + port + username          {red}║")
    print(f"{red}║                                                                          ║")
    print(f"{red}║  [{white}0{red}] {white}Quitter le programme                                             {red}║")
    print(f"{red}║                                                                          ║")
    print(f"{red}╚══════════════════════════════════════════════════════════════════════════╝{reset}")

def main():
    while True:
        clear()
        print(banner)
        display_menu()
        choice = input(f"{prefix} Choix: ")
        
        if choice == "0":
            print(f"{prefix} Au revoir!")
            break
            
        token = input(f"{prefix} Token: ").strip()
        if not token:
            print(f"{prefix} Token requis")
            continue
            
        if choice == "1":
            checker = TokenChecker(token)
            checker.check_token()
            
        elif choice == "2":
            proxy = input(f"{prefix} Proxy (http://... ou https://...): ").strip()
            checker = TokenChecker(token, proxy)
            if checker.check_token():
                if proxy and proxy.startswith(("http://", "https://")):
                    print(f"{prefix} Token valide avec proxy")
                else:
                    print(f"{prefix} Token valide sans proxy")
            else:
                print(f"{prefix} Token invalide")
            
        elif choice == "3":
            proxy = input(f"{prefix} Proxy (http://... ou https://...): ").strip()
            user_agent = input(f"{prefix} User-Agent: ").strip()
            checker = TokenChecker(token, proxy)
            if checker.check_token():
                if proxy and proxy.startswith(("http://", "https://")):
                    if user_agent:
                        print(f"{prefix} Token valide avec proxy et user-agent")
                    else:
                        print(f"{prefix} Token valide avec proxy")
                else:
                    print(f"{prefix} Token valide sans proxy")
            else:
                print(f"{prefix} Token invalide")
            
        elif choice == "4":
            proxy = input(f"{prefix} Proxy (http://... ou https://...): ").strip()
            user_agent = input(f"{prefix} User-Agent: ").strip()
            ip = input(f"{prefix} IP: ").strip()
            checker = TokenChecker(token, proxy)
            if proxy and user_agent and ip:
                print(f"{prefix} Token valide avec proxy, user-agent et IP")
                if ip in proxy:
                    print(f"{prefix} Token valide avec proxy, user-agent et IP")
                else:
                    print(f"{prefix} Token valide avec proxy et user-agent")
            else:
                print(f"{prefix} Token invalide")
            
        elif choice == "5":
            proxy = input(f"{prefix} Proxy (http://... ou https://...): ").strip()
            user_agent = input(f"{prefix} User-Agent: ").strip()
            ip = input(f"{prefix} IP: ").strip()
            port = input(f"{prefix} Port: ").strip()
            checker = TokenChecker(token, proxy)
            checker.check_token()
            
        elif choice == "6":
            proxy = input(f"{prefix} Proxy (http://... ou https://...): ").strip()
            user_agent = input(f"{prefix} User-Agent: ").strip()
            ip = input(f"{prefix} IP: ").strip()
            port = input(f"{prefix} Port: ").strip()
            username = input(f"{prefix} Username: ").strip()
            checker = TokenChecker(token, proxy)
            checker.check_token()

if __name__ == "__main__":
    main()