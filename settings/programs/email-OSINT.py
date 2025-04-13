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
import requests
from colorama import Fore, Style
import time
import re
from bs4 import BeautifulSoup

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"""{red}
███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝
█████╗  ██╔████╔██║███████║██║██║         ██║  ██║███████╗██║██╔██╗ ██║   ██║   
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██║  ██║╚════██║██║██║╚██╗██║   ██║   
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝███████║██║██║ ╚████║   ██║   
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
{reset}""")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def check_social_media(email):
    sites = {
        "Facebook": f"https://www.facebook.com/search/top/?q={email}",
        "Twitter": f"https://twitter.com/search?q={email}",
        "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords={email}",
        "Instagram": f"https://www.instagram.com/{email.split('@')[0]}",
        "GitHub": f"https://github.com/search?q={email}",
        "Reddit": f"https://www.reddit.com/search/?q={email}",
        "Pinterest": f"https://www.pinterest.com/search/users/?q={email}",
        "Tumblr": f"https://www.tumblr.com/search/{email}",
        "Medium": f"https://medium.com/search?q={email}",
        "DeviantArt": f"https://www.deviantart.com/search?q={email}",
        "Flickr": f"https://www.flickr.com/search/?text={email}",
        "Behance": f"https://www.behance.net/search?search={email}",
        "SlideShare": f"https://www.slideshare.net/search/slideshow?searchfrom=header&q={email}",
        "Vimeo": f"https://vimeo.com/search?q={email}",
        "SoundCloud": f"https://soundcloud.com/search?q={email}",
        "Pastebin": f"https://pastebin.com/search?q={email}",
        "Steam": f"https://steamcommunity.com/search/users/#text={email}",
        "TikTok": f"https://www.tiktok.com/search?q={email}",
        "Twitch": f"https://www.twitch.tv/search?term={email}",
        "Gravatar": f"https://en.gravatar.com/{email.split('@')[0]}"
    }
    
    results = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    for site, url in sites.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                results.append(f"{site}: {url}")
        except:
            continue
            
    return results

def main():
    while True:
        banner()
        print(f"\n{red}[{white}+{red}]{white} Email OSINT Tool")
        print(f"{red}[{white}1{red}]{white} Check email across social media")
        print(f"{red}[{white}2{red}]{white} Email validation")
        print(f"{red}[{white}0{red}]{white} Exit")
        
        choice = input(f"\n{red}[{white}>{red}]{white} Choose an option: ")
        
        if choice == "1":
            email = input(f"\n{red}[{white}>{red}]{white} Enter email address: ")
            if validate_email(email):
                print(f"\n{red}[{white}*{red}]{white} Searching across platforms...")
                results = check_social_media(email)
                if results:
                    print(f"\n{red}[{white}!{red}]{white} Potential matches found:")
                    for result in results:
                        print(f"{red}[{white}+{red}]{white} {result}")
                else:
                    print(f"\n{red}[{white}+{red}]{white} No matches found!")
            else:
                print(f"\n{red}[{white}!{red}]{white} Invalid email format!")
                
        elif choice == "2":
            email = input(f"\n{red}[{white}>{red}]{white} Enter email address: ")
            if validate_email(email):
                print(f"\n{red}[{white}+{red}]{white} Valid email format!")
            else:
                print(f"\n{red}[{white}!{red}]{white} Invalid email format!")
                
        elif choice == "0":
            clear()
            break
            
        input(f"\n{red}[{white}>{red}]{white} Press Enter to continue...")
        clear()

if __name__ == "__main__":
    main()

