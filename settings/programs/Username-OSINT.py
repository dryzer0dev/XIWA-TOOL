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

class UsernameOSINT:
    def __init__(self):
        self.platforms = {
            'github': {
                'url': 'https://api.github.com/users/{}',
                'check': lambda r: r.status_code == 200
            },
            'twitter': {
                'url': 'https://api.twitter.com/i/users/username_available.json?username={}',
                'check': lambda r: r.status_code == 200 and not r.json().get('valid', False)
            },
            'instagram': {
                'url': 'https://www.instagram.com/{}/?__a=1',
                'check': lambda r: r.status_code == 200 and 'user' in r.text
            },
            'tiktok': {
                'url': 'https://www.tiktok.com/api/user/detail/?uniqueId={}',
                'check': lambda r: r.status_code == 200 and 'userInfo' in r.text
            },
            'reddit': {
                'url': 'https://www.reddit.com/user/{}/about.json',
                'check': lambda r: r.status_code == 200 and 'data' in r.text
            },
            'medium': {
                'url': 'https://medium.com/@{}',
                'check': lambda r: r.status_code == 200 and '404' not in r.url
            },
            'dev.to': {
                'url': 'https://dev.to/api/users/by_username?url={}',
                'check': lambda r: r.status_code == 200 and 'id' in r.text
            },
            'hackernews': {
                'url': 'https://hacker-news.firebaseio.com/v0/user/{}.json',
                'check': lambda r: r.status_code == 200 and r.text != 'null'
            },
            'pinterest': {
                'url': 'https://www.pinterest.com/{}/',
                'check': lambda r: r.status_code == 200 and 'User not found' not in r.text
            },
            'spotify': {
                'url': 'https://open.spotify.com/user/{}',
                'check': lambda r: r.status_code == 200 and 'Page not found' not in r.text
            },
            'soundcloud': {
                'url': 'https://soundcloud.com/{}',
                'check': lambda r: r.status_code == 200 and 'Page not found' not in r.text
            },
            'pornhub': {
                'url': 'https://www.pornhub.com/users/{}',
                'check': lambda r: r.status_code == 200 and 'User not found' not in r.text
            },
            'onlyfans': {
                'url': 'https://onlyfans.com/{}',
                'check': lambda r: r.status_code == 200 and 'Page not found' not in r.text
            },
            'twitch': {
                'url': 'https://api.twitch.tv/helix/users?login={}',
                'check': lambda r: r.status_code == 200 and 'data' in r.text and len(r.json().get('data', [])) > 0
            },
            'linkedin': {
                'url': 'https://www.linkedin.com/in/{}/',
                'check': lambda r: r.status_code == 200 and 'Page not found' not in r.text
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
{Fore.CYAN}██╗   ██╗██╗    ██╗ █████╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
██║   ██║██║    ██║██╔══██╗    ██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║   ██║██║ █╗ ██║███████║    ██████╔╝███████╗██║██╔██╗ ██║   ██║   
██║   ██║██║███╗██║██╔══██║    ██╔══██╗╚════██║██║██║╚██╗██║   ██║   
╚██████╔╝╚███╔███╔╝██║  ██║    ██║  ██║███████║██║██║ ╚████║   ██║   
 ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                      
{Fore.GREEN}Username OSINT Tool - Created by XIWA{Style.RESET_ALL}
{Fore.WHITE}Version 1.2{Style.RESET_ALL}
"""
        print(banner)

    def print_menu(self):
        menu = f"""
{Fore.CYAN}╭──────────────────────────────────────────────╮
│ {Fore.YELLOW}MENU PRINCIPAL{Fore.CYAN}                               │
├──────────────────────────────────────────────┤
│                                              │
│  {Fore.GREEN}[1]{Fore.WHITE} Rechercher un nom d'utilisateur         │
│  {Fore.GREEN}[2]{Fore.WHITE} À propos                                │
│  {Fore.GREEN}[3]{Fore.WHITE} Quitter                                 │
│                                              │
╰──────────────────────────────────────────────╯{Style.RESET_ALL}
"""
        print(menu)

    def print_about(self):
        about = f"""
{Fore.CYAN}╭──────────────────────────────────────────────╮
│ {Fore.YELLOW}À PROPOS{Fore.CYAN}                                    
├──────────────────────────────────────────────
│                                              
│  {Fore.WHITE}Username OSINT Tool est un outil de reconnaissance      
│  qui permet de vérifier la disponibilité d'un nom    
│  d'utilisateur sur différentes plateformes.         
│                                              
│  {Fore.GREEN}Plateformes supportées:{Fore.WHITE}                     
│  • GitHub, Twitter, Instagram, TikTok               
│  • Reddit, Medium, Dev.to, HackerNews              
│  • Pinterest, Spotify, SoundCloud                  
│  • PornHub, OnlyFans, Twitch, LinkedIn            
│                                              
╰──────────────────────────────────────────────╯{Style.RESET_ALL}
"""
        print(about)
        input(f"\n{Fore.GREEN}Appuyez sur Entrée pour revenir au menu principal...{Style.RESET_ALL}")

    def check_username(self, platform: str, username: str) -> Dict:
        """Check if a username exists on a specific platform."""
        platform_info = self.platforms[platform]
        url = platform_info['url'].format(username)
        try:
            response = requests.get(url, headers=self.headers, timeout=10, verify=False)
            exists = platform_info['check'](response)
            return {
                'platform': platform,
                'username': username,
                'url': url,
                'exists': exists,
                'status_code': response.status_code
            }
        except requests.RequestException as e:
            return {
                'platform': platform,
                'username': username,
                'url': url,
                'exists': False,
                'error': str(e)
            }

    def search_username(self, username: str, max_workers: int = 5) -> List[Dict]:
        """Search for a username across all platforms."""
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_platform = {
                executor.submit(self.check_username, platform, username): platform
                for platform in self.platforms.keys()
            }
            
            for future in future_to_platform:
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"Error checking {future_to_platform[future]}: {str(e)}")
                
                # Rate limiting
                time.sleep(0.5)
        
        return results

    def print_results(self, results: List[Dict]):
        """Print the results in a formatted way."""
        print(f"\n{Fore.CYAN}╭──────────────────────────────────────────────╮")
        print(f"│ {Fore.YELLOW}RÉSULTATS DE LA RECHERCHE{Fore.CYAN}                    │")
        print(f"├──────────────────────────────────────────────┤")
        print(f"│ {Fore.WHITE}Horodatage: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.CYAN}    │")
        print(f"├──────────────────────────────────────────────┤")
        
        found_count = 0
        for result in results:
            status = f"{Fore.GREEN}✅ Profil trouvé" if result.get('exists') else f"{Fore.RED}❌ Profil introuvable"
            if 'error' in result:
                status = f"{Fore.YELLOW}⚠️ Erreur: {result['error']}"
            else:
                found_count += 1 if result.get('exists') else 0
            
            print(f"│ {Fore.WHITE}• {result['platform'].upper()}{Fore.CYAN}                          │")
            print(f"│   {Fore.WHITE}URL: {result['url']}{Fore.CYAN}  │")
            print(f"│   {Fore.WHITE}Statut: {status}{Fore.CYAN}  │")
            print(f"│ {Fore.CYAN}──────────────────────────────────────────────│")
        
        print(f"│ {Fore.WHITE}Profils trouvés: {found_count}/{len(results)}{Fore.CYAN}                    │")
        print(f"╰──────────────────────────────────────────────╯{Style.RESET_ALL}")
        input(f"\n{Fore.GREEN}Appuyez sur Entrée pour revenir au menu principal...{Style.RESET_ALL}")

def main():
    osint = UsernameOSINT()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        osint.print_banner()
        osint.print_menu()
        
        choice = input(f"{Fore.GREEN}Choisissez une option (1-3): {Style.RESET_ALL}")
        
        if choice == '1':
            username = input(f"\n{Fore.GREEN}Entrez le nom d'utilisateur à rechercher: {Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Recherche en cours pour: {username}{Style.RESET_ALL}")
            results = osint.search_username(username)
            osint.print_results(results)
        elif choice == '2':
            osint.print_about()
        elif choice == '3':
            print(f"\n{Fore.GREEN}Au revoir!{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"\n{Fore.RED}Option invalide. Veuillez réessayer.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()




