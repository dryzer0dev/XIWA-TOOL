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

import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore, Style
import os
import time
import json
from bs4 import BeautifulSoup
import re
import sqlite3
import urllib.parse
import threading
import requests.exceptions
from datetime import datetime

red = Fore.RED 
white = Fore.WHITE
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = f"""{red}
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║   ██║███████╗██║██╔██╗ ██║   ██║   
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║   ██║╚════██║██║██║╚██╗██║   ██║   
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                                        
{white}                      Phone Number OSINT Tool v3.0 - No API Edition{reset}
"""

def search_leaked_databases(number):
    results = {}
    
    leak_sites = [
        "https://leakcheck.net/api/public",
        "https://haveibeenpwned.com/unifiedsearch/", 
        "https://leak-lookup.com/api/search",
        "https://snusbase.com/api/v3/search",
        "https://leakpeek.com/api/check",
        "https://leakcheck.io/api",
        "https://leakbase.io",
        "https://leakix.net",
        "https://leakcheck.net",
        "https://leakpeek.com",
        "https://weleakinfo.to",
        "https://leakcheck.io",
        "https://leakbase.io",
        "https://leakix.net",
        "https://leakcheck.net"
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/json',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'DNT': '1'
    }

    for site in leak_sites:
        try:
            response = requests.get(f"{site}?q={number}", headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.text
                
                emails = re.findall(r'[\w\.-]+@[\w\.-]+', data)
                names = re.findall(r'(?:name|nom)["\']:\s*["\']([^"\']+)', data, re.I)
                locations = re.findall(r'(?:location|ville|adresse)["\']:\s*["\']([^"\']+)', data, re.I)
                phones = re.findall(r'(?:\+\d{1,3}[-\.\s]?)?\(?\d{1,4}\)?[-\.\s]?\d{1,4}[-\.\s]?\d{1,9}', data)
                social = re.findall(r'(?:facebook|twitter|linkedin|instagram)\.com/[\w\.-]+', data)
                
                if any([emails, names, locations, phones, social]):
                    results[site] = {
                        "emails": list(set(emails)),
                        "noms": list(set(names)),
                        "localisations": list(set(locations)), 
                        "telephones": list(set(phones)),
                        "reseaux_sociaux": list(set(social))
                    }

        except requests.exceptions.RequestException:
            continue
            
    return results

def search_social_networks(number):
    social_sites = {
        "facebook": [
            "https://www.facebook.com/search/top/?q=",
            "https://www.facebook.com/search/people/?q=",
            "https://www.facebook.com/search/posts/?q="
        ],
        "linkedin": [
            "https://www.linkedin.com/search/results/all/?keywords=",
            "https://www.linkedin.com/search/results/people/?keywords="
        ],
        "twitter": [
            "https://twitter.com/search?q=",
            "https://twitter.com/search?f=users&q="
        ],
        "instagram": [
            "https://www.instagram.com/web/search/topsearch/?query=",
            "https://www.instagram.com/explore/tags/"
        ],
        "snapchat": [
            "https://story.snapchat.com/@",
            "https://www.snapchat.com/add/"
        ],
        "tiktok": [
            "https://www.tiktok.com/@",
            "https://www.tiktok.com/tag/"
        ]
    }
    
    results = {}
    formatted_number = number.replace("+", "").replace(" ", "")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/json',
        'Accept-Language': 'fr-FR,fr;q=0.9',
        'DNT': '1'
    }

    for platform, urls in social_sites.items():
        try:
            platform_results = []
            for url in urls:
                response = requests.get(f"{url}{formatted_number}", headers=headers, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    profiles = soup.find_all(['a', 'div', 'span'], 
                        class_=re.compile(r'profile|user|result|name|title', re.I))
                    
                    for profile in profiles:
                        profile_data = {
                            "url": profile.get('href', ''),
                            "nom": profile.get_text().strip(),
                            "description": profile.get('title', ''),
                            "meta": profile.get('data-meta', '')
                        }
                        if any(profile_data.values()):
                            platform_results.append(profile_data)

            if platform_results:
                results[platform] = platform_results

        except:
            continue
            
    return results

def deep_search(number):
    directories = [
        "https://www.pagesblanches.fr/recherche?q=",
        "https://www.118712.fr/?q=",
        "https://www.118000.fr/search?q=",
        "https://www.pagesjaunes.fr/recherche?q=",
        "https://www.annuaire.com/recherche?q=",
        "https://www.localphone.com/search?q=",
        "https://www.whitepages.fr/search?q=",
        "https://www.annuaire-inverse.net/search?q=",
        "https://www.infobel.com/fr/france/search?q=",
        "https://www.annuaire4g.fr/search?q="
    ]
    
    results = {}
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Language': 'fr-FR,fr;q=0.9'
    }

    for directory in directories:
        try:
            response = requests.get(f"{directory}{number}", headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                names = soup.find_all(class_=re.compile(r'name|nom|titre|identity', re.I))
                addresses = soup.find_all(class_=re.compile(r'address|adresse|location', re.I))
                phones = soup.find_all(class_=re.compile(r'phone|tel|mobile|numero', re.I))
                details = soup.find_all(class_=re.compile(r'details|info|data', re.I))
                
                if any([names, addresses, phones, details]):
                    results[directory] = {
                        "noms": [n.text.strip() for n in names if n.text.strip()],
                        "adresses": [a.text.strip() for a in addresses if a.text.strip()],
                        "telephones": [p.text.strip() for p in phones if p.text.strip()],
                        "details": [d.text.strip() for d in details if d.text.strip()]
                    }

        except:
            continue
            
    return results

def get_phone_info(number):
    try:
        parsed = phonenumbers.parse(number)
        
        if not phonenumbers.is_valid_number(parsed):
            return None

        info = {
            "INFORMATIONS DE BASE": {
                "Numéro formaté": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                "Pays": geocoder.description_for_number(parsed, "fr"),
                "Opérateur": carrier.name_for_number(parsed, "fr"),
                "Indicatif": f"+{parsed.country_code}",
                "Type": "Mobile" if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.MOBILE else "Fixe",
                "Fuseau horaire": timezone.time_zones_for_number(parsed)[0],
                "Format national": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
                "Format E164": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
                "Région": geocoder.description_for_number(parsed, "fr", region=True),
                "Valide": "Oui" if phonenumbers.is_valid_number(parsed) else "Non",
                "Possible": "Oui" if phonenumbers.is_possible_number(parsed) else "Non",
                "Type de ligne": phonenumbers.number_type(parsed),
                "Code pays": parsed.country_code,
                "Code région": parsed.national_number,
                "Opérateur d'origine": carrier.name_for_number(parsed, "fr", region=True),
                "Format international": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            }
        }

        leaked_data = search_leaked_databases(number) 
        if leaked_data:
            info["DONNÉES LEAKÉES"] = leaked_data

        social_data = search_social_networks(number)
        if social_data:
            info["RÉSEAUX SOCIAUX"] = social_data

        deep_data = deep_search(number)
        if deep_data:
            info["INFORMATIONS COMPLÉMENTAIRES"] = deep_data

        return info

    except Exception as e:
        print(f"\n{red}[{white}!{red}]{white} Erreur: {str(e)}{reset}")
        return None

def display_results(info):
    if not info:
        print(f"\n{red}[{white}!{red}]{white} Aucune information trouvée{reset}")
        return

    print(f"\n{red}╔══════════════════════════════════════════════════════════════╗")
    print(f"║ {white}RÉSULTATS DE LA RECHERCHE OSINT{' ' * 31}{red}║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    
    for category, data in info.items():
        print(f"║ {white}{category}{' ' * (60 - len(category))}{red}║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    print(f"║ {white}{key}:{reset}")
                    for k, v in value.items() if isinstance(value, dict) else enumerate(value):
                        padding = 55 - len(str(k)) - len(str(v))
                        print(f"║ {white}  - {k}: {red}{v}{' ' * padding}{red}║")
                else:
                    padding = 60 - len(str(key)) - len(str(value))
                    print(f"║ {white}{key}: {red}{value}{' ' * padding}{red}║")
                    
        print(f"╠══════════════════════════════════════════════════════════════╣")
    
    print(f"╚══════════════════════════════════════════════════════════════╝{reset}")

def show_progress():
    steps = [
        "Analyse du numéro...",
        "Recherche dans les bases de données leakées...", 
        "Scan des réseaux sociaux...",
        "Recherche dans les annuaires inversés...",
        "Analyse des métadonnées...",
        "Recherche d'informations personnelles...",
        "Scan des réseaux sociaux avancé...",
        "Vérification des fuites de données...",
        "Analyse des résultats...",
        "Compilation des informations..."
    ]
    
    for step in steps:
        print(f"\r{red}[{white}*{red}]{white} {step}{reset}", end="")
        time.sleep(0.5)
        print("\r" + " " * 100, end="")

def main():
    while True:
        clear()
        print(banner)
        
        number = input(f"\n{red}[{white}>{red}]{white} Entrez un numéro de téléphone (+33612345678) : {reset}")
        
        if number.lower() == "exit":
            break
            
        print(f"\n{red}[{white}*{red}]{white} Lancement de la recherche OSINT...{reset}")
        show_progress()
        
        info = get_phone_info(number)
        display_results(info)
        
        input(f"\n{red}[{white}>{red}]{white} Appuyez sur Entrée pour continuer...{reset}")
        print("0 pour quitter")
        
        if input == "0":
            break

if __name__ == "__main__":
    main()

