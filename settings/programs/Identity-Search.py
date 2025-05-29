#!/usr/bin/env python3

import requests
import time
import json
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional
import sys
from datetime import datetime
import os
from colorama import init, Fore, Back, Style
import re
import urllib3
urllib3.disable_warnings()

# Initialize colorama
init()

class IdentitySearch:
    def __init__(self):
        self.platforms = {
            'email': {
                'url': 'https://api.haveibeenpwned.com/breachedaccount/{}',
                'check': lambda r: r.status_code == 200,
                'get_info': lambda r: {
                    'breaches': r.json() if r.status_code == 200 else []
                }
            },
            'phone': {
                'url': 'https://api.numverify.com/validate?access_key=YOUR_API_KEY&number={}',
                'check': lambda r: r.status_code == 200,
                'get_info': lambda r: {
                    'valid': r.json().get('valid', False),
                    'country': r.json().get('country_name', 'N/A'),
                    'carrier': r.json().get('carrier', 'N/A')
                }
            },
            'username': {
                'url': 'https://api.github.com/users/{}',
                'check': lambda r: r.status_code == 200,
                'get_info': lambda r: {
                    'name': r.json().get('name', 'N/A'),
                    'bio': r.json().get('bio', 'N/A'),
                    'location': r.json().get('location', 'N/A')
                }
            }
        }
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    def print_banner(self):
        banner = f"""
{Fore.RED}██╗██████╗ ███████╗███╗   ██╗████████╗██╗███████╗██╗   ██╗
██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██║██║  ██║█████╗  ██╔██╗ ██║   ██║   ██║█████╗   ╚████╔╝ 
██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   ██║██╔══╝    ╚██╔╝  
██║██████╔╝███████╗██║ ╚████║   ██║   ██║██║        ██║   
╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝        ╚═╝   
                                                            
{Fore.RED}Identity Search Tool - Created by XIWA{Style.RESET_ALL}
{Fore.WHITE}Version 1.0{Style.RESET_ALL}
"""
        print(banner)

    def print_menu(self):
        menu = f"""
{Fore.RED}╭──────────────────────────────────────────────╮
│ {Fore.YELLOW}MENU PRINCIPAL{Fore.RED}                               │
├──────────────────────────────────────────────┤
│                                              │
│  {Fore.GREEN}[1]{Fore.WHITE} Rechercher par email                    │
│  {Fore.GREEN}[2]{Fore.WHITE} Rechercher par numéro de téléphone      │
│  {Fore.GREEN}[3]{Fore.WHITE} Rechercher par nom d'utilisateur        │
│  {Fore.GREEN}[4]{Fore.WHITE} Recherche avancée                       │
│  {Fore.GREEN}[5]{Fore.WHITE} À propos                                │
│  {Fore.GREEN}[6]{Fore.WHITE} Quitter                                 │
│                                              │
╰──────────────────────────────────────────────╯{Style.RESET_ALL}
"""
        print(menu)

    def print_about(self):
        about = f"""
{Fore.RED}╭──────────────────────────────────────────────╮
│ {Fore.YELLOW}À PROPOS{Fore.RED}                                    
├──────────────────────────────────────────────
│                                              
│  {Fore.WHITE}Identity Search Tool est un outil de reconnaissance      
│  qui permet de rechercher des informations sur une    
│  identité à travers différentes plateformes.         
│                                              
│  {Fore.GREEN}Fonctionnalités:{Fore.WHITE}                     
│  • Vérification d'emails (fuites de données)               
│  • Recherche de numéros de téléphone                
│  • Recherche de noms d'utilisateur               
│  • Recherche avancée (combinaison)                  
│                                              
╰──────────────────────────────────────────────╯{Style.RESET_ALL}
"""
        print(about)
        input(f"\n{Fore.GREEN}Appuyez sur Entrée pour revenir au menu principal...{Style.RESET_ALL}")

    def check_identity(self, platform: str, query: str) -> Dict:
        """Check identity information on a specific platform."""
        platform_info = self.platforms[platform]
        url = platform_info['url'].format(query)
        try:
            response = requests.get(url, headers=self.headers, timeout=10, verify=False)
            exists = platform_info['check'](response)
            info = platform_info['get_info'](response) if exists else {}
            return {
                'platform': platform,
                'query': query,
                'url': url,
                'exists': exists,
                'info': info,
                'status_code': response.status_code
            }
        except requests.RequestException as e:
            return {
                'platform': platform,
                'query': query,
                'url': url,
                'exists': False,
                'error': str(e)
            }

    def search_identity(self, platform: str, query: str) -> List[Dict]:
        """Search for identity information."""
        results = []
        result = self.check_identity(platform, query)
        results.append(result)
        return results

    def advanced_search(self, email: str = None, phone: str = None, username: str = None):
        """Perform advanced identity search."""
        print(f"\n{Fore.YELLOW}Recherche avancée en cours...{Style.RESET_ALL}")
        
        if email:
            print(f"\n{Fore.GREEN}[+] Recherche par email: {email}{Style.RESET_ALL}")
            results = self.search_identity('email', email)
            self.print_results(results)
        
        if phone:
            print(f"\n{Fore.GREEN}[+] Recherche par téléphone: {phone}{Style.RESET_ALL}")
            results = self.search_identity('phone', phone)
            self.print_results(results)
        
        if username:
            print(f"\n{Fore.GREEN}[+] Recherche par username: {username}{Style.RESET_ALL}")
            results = self.search_identity('username', username)
            self.print_results(results)

    def print_results(self, results: List[Dict]):
        """Print the results in a formatted way."""
        print(f"\n{Fore.RED}╭──────────────────────────────────────────────╮")
        print(f"│ {Fore.YELLOW}RÉSULTATS DE LA RECHERCHE{Fore.RED}                    │")
        print(f"├──────────────────────────────────────────────┤")
        print(f"│ {Fore.WHITE}Horodatage: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RED}    │")
        print(f"├──────────────────────────────────────────────┤")
        
        for result in results:
            status = f"{Fore.GREEN}✅ Information trouvée" if result.get('exists') else f"{Fore.RED}❌ Information introuvable"
            if 'error' in result:
                status = f"{Fore.YELLOW}⚠️ Erreur: {result['error']}"
            
            print(f"│ {Fore.WHITE}• {result['platform'].upper()}{Fore.RED}                          │")
            print(f"│   {Fore.WHITE}Requête: {result['query']}{Fore.RED}  │")
            print(f"│   {Fore.WHITE}Statut: {status}{Fore.RED}  │")
            
            if result.get('exists') and result.get('info'):
                print(f"│   {Fore.WHITE}Informations:{Fore.RED}                          │")
                for key, value in result['info'].items():
                    print(f"│     • {key}: {value}{Fore.RED}  │")
            
            print(f"│ {Fore.RED}──────────────────────────────────────────────│")
        
        print(f"╰──────────────────────────────────────────────╯{Style.RESET_ALL}")
        input(f"\n{Fore.GREEN}Appuyez sur Entrée pour revenir au menu principal...{Style.RESET_ALL}")

def main():
    search = IdentitySearch()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        search.print_banner()
        search.print_menu()
        
        choice = input(f"{Fore.GREEN}Choisissez une option (1-6): {Style.RESET_ALL}")
        
        if choice == '1':
            email = input(f"\n{Fore.GREEN}Entrez l'adresse email à rechercher: {Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Recherche en cours pour: {email}{Style.RESET_ALL}")
            results = search.search_identity('email', email)
            search.print_results(results)
        elif choice == '2':
            phone = input(f"\n{Fore.GREEN}Entrez le numéro de téléphone à rechercher: {Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Recherche en cours pour: {phone}{Style.RESET_ALL}")
            results = search.search_identity('phone', phone)
            search.print_results(results)
        elif choice == '3':
            username = input(f"\n{Fore.GREEN}Entrez le nom d'utilisateur à rechercher: {Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Recherche en cours pour: {username}{Style.RESET_ALL}")
            results = search.search_identity('username', username)
            search.print_results(results)
        elif choice == '4':
            print(f"\n{Fore.YELLOW}Recherche avancée{Style.RESET_ALL}")
            email = input(f"{Fore.GREEN}Email (laissez vide si non applicable): {Style.RESET_ALL}")
            phone = input(f"{Fore.GREEN}Numéro de téléphone (laissez vide si non applicable): {Style.RESET_ALL}")
            username = input(f"{Fore.GREEN}Nom d'utilisateur (laissez vide si non applicable): {Style.RESET_ALL}")
            search.advanced_search(email or None, phone or None, username or None)
        elif choice == '5':
            search.print_about()
        elif choice == '6':
            print(f"\n{Fore.GREEN}Au revoir!{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"\n{Fore.RED}Option invalide. Veuillez réessayer.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()



