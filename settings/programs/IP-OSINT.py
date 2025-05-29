#!/usr/bin/env python3
import requests
import json
import socket
import whois
from datetime import datetime
import sys

# Couleurs ANSI (rouge/gras)
RED = "\033[91m"
BOLD = "\033[1m"
END = "\033[0m"

# Bannière stylisée
def banner():
    print(f"""{RED}{BOLD}
   ___  _____  ___  _  _    ___  _   _ _____ ___  
  / _ \|_   _|/ _ \| \| |  / _ \| | | |_   _/ _ \ 
 | (_) | | | | (_) | .` | | (_) | |_| | | || (_) |
  \___/  |_|  \___/|_|\_|  \___/ \___/  |_| \___/ 
  {END}""")
    print(f"{RED}{BOLD}  OSINT Tool - IP & Domain Intelligence{END}\n")

# Vérification des dépendances
def check_dependencies():
    try:
        import whois
        import requests
    except ImportError as e:
        print(f"{RED}[!] Erreur: {e}. Installez les dépendances avec :{END}")
        print("pip install python-whois requests")
        sys.exit(1)

# Option 1: OSINT pour une IP
def ip_osint(ip):
    print(f"\n{RED}{BOLD}=== ANALYSE IP: {ip} ==={END}\n")

    # 1. Géolocalisation (ipapi.co)
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        geo = response.json()
        print(f"{RED}[+] Géolocalisation:{END}")
        print(f"  Pays: {geo.get('country_name', 'N/A')}")
        print(f"  Ville: {geo.get('city', 'N/A')}")
        print(f"  Opérateur: {geo.get('org', 'N/A')}")
        print(f"  Coordonnées: {geo.get('latitude', 'N/A')}, {geo.get('longitude', 'N/A')}")
    except Exception as e:
        print(f"{RED}[!] Erreur ipapi.co: {e}{END}")

    # 2. Données Shodan (si clé API disponible)
    try:
        shodan_key = ""  # Remplacez par votre clé Shodan (optionnel)
        if shodan_key:
            response = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={shodan_key}")
            shodan = response.json()
            print(f"\n{RED}[+] Shodan Data:{END}")
            print(f"  Ports ouverts: {', '.join(map(str, shodan.get('ports', [])))}")
            print(f"  OS: {shodan.get('os', 'N/A')}")
    except:
        print(f"{RED}[!] Shodan: Clé API manquante ou erreur.{END}")

    # 3. Whois
    try:
        w = whois.whois(ip)
        print(f"\n{RED}[+] Whois:{END}")
        print(f"  Organisation: {w.get('org', 'N/A')}")
        print(f"  Pays: {w.get('country', 'N/A')}")
        print(f"  Date de création: {w.get('creation_date', 'N/A')}")
    except Exception as e:
        print(f"{RED}[!] Erreur Whois: {e}{END}")

# Option 2: OSINT général (domaine, email, etc.)
def general_osint():
    target = input(f"{RED}Entrez un domaine/email : {END}")
    print(f"\n{RED}{BOLD}=== ANALYSE: {target} ==={END}\n")

    # 1. Whois pour un domaine
    if "." in target and "@" not in target:
        try:
            w = whois.whois(target)
            print(f"{RED}[+] Whois:{END}")
            print(f"  Serveurs DNS: {', '.join(w.get('name_servers', []))}")
            print(f"  Expiration: {w.get('expiration_date', 'N/A')}")
        except Exception as e:
            print(f"{RED}[!] Erreur Whois: {e}{END}")

    # 2. Vérification email (Have I Been Pwned?)
    elif "@" in target:
        try:
            response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{target}", headers={"User-Agent": "OSINT-Tool"})
            if response.status_code == 200:
                breaches = json.loads(response.text)
                print(f"{RED}[+] Fuites trouvées (Have I Been Pwned):{END}")
                for breach in breaches:
                    print(f"  - {breach['Name']} ({breach['BreachDate']})")
            else:
                print(f"{RED}[+] Aucune fuite trouvée pour cet email.{END}")
        except Exception as e:
            print(f"{RED}[!] Erreur HIBP: {e}{END}")

# Menu principal
def main():
    banner()
    check_dependencies()
    print(f"{RED}1. Analyse d'IP")
    print(f"2. OSINT général (domaine/email)")
    choice = input(f"\n{RED}Choisissez une option (1/2) : {END}")

    if choice == "1":
        ip = input(f"{RED}Entrez l'IP à analyser : {END}")
        ip_osint(ip)
    elif choice == "2":
        general_osint()
    else:
        print(f"{RED}[!] Option invalide.{END}")

if __name__ == "__main__":
    main()