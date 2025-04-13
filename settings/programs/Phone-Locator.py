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

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import colorama
from colorama import Fore, Style
import requests
import json

colorama.init()

def obtenir_localisation_precise(numero_parse):
    try:
        # Obtenir le pays
        pays = geocoder.description_for_number(numero_parse, "fr")
        
        # Obtenir les coordonnées approximatives basées sur l'indicatif régional
        region = geocoder.description_for_number(numero_parse, "fr")
        
        # Utiliser l'API de géocodage pour obtenir la ville
        url = f"https://nominatim.openstreetmap.org/search?q={region}&format=json"
        headers = {'User-Agent': 'PhoneLocator/1.0'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                ville = data[0].get('display_name', '').split(',')[0]
                if ville:
                    return f"{ville}, {pays}"
        return pays
    except:
        return "Localisation non disponible"

def localiser_telephone():
    try:
        numero = input(f"{Fore.CYAN}[>] Entrez le numéro de téléphone (format: +33612345678): {Style.RESET_ALL}")
        
        numero_parse = phonenumbers.parse(numero)
        
        if not phonenumbers.is_valid_number(numero_parse):
            print(f"{Fore.RED}[!] Numéro de téléphone invalide{Style.RESET_ALL}")
            return
            
        # Localisation précise à la ville
        localisation = obtenir_localisation_precise(numero_parse)
        print(f"\n{Fore.GREEN}[+] Localisation: {localisation}{Style.RESET_ALL}")
        
        # Opérateur
        operateur = carrier.name_for_number(numero_parse, "fr")
        print(f"{Fore.GREEN}[+] Opérateur: {operateur}{Style.RESET_ALL}")
        
        # Fuseau horaire
        fuseau = timezone.time_zones_for_number(numero_parse)
        print(f"{Fore.GREEN}[+] Fuseau horaire: {', '.join(fuseau)}{Style.RESET_ALL}")
        
        # Format international
        format_international = phonenumbers.format_number(numero_parse, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print(f"{Fore.GREEN}[+] Format international: {format_international}{Style.RESET_ALL}")
        
        # Informations détaillées sur la ville
        print(f"\n{Fore.YELLOW}[*] Recherche d'informations détaillées...{Style.RESET_ALL}")
        region = geocoder.description_for_number(numero_parse, "fr")
        url = f"https://nominatim.openstreetmap.org/search?q={region}&format=json"
        headers = {'User-Agent': 'PhoneLocator/1.0'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                adresse = data[0].get('address', {})
                print(f"{Fore.GREEN}[+] Ville: {data[0].get('display_name', '').split(',')[0]}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Département: {region}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Région: {region}{Style.RESET_ALL}")
                
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.YELLOW}=== Localisateur de numéro de téléphone ==={Style.RESET_ALL}")
    while True:
        print(f"\n{Fore.WHITE}[1] Localiser un numéro")
        print(f"{Fore.WHITE}[2] Quitter")
        choix = input(f"{Fore.WHITE}[>] Votre choix: {Style.RESET_ALL}")
        
        if choix == "1":
            localiser_telephone()
        elif choix == "2":
            print(f"{Fore.YELLOW}[!] Au revoir !{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[!] Choix invalide{Style.RESET_ALL}")
