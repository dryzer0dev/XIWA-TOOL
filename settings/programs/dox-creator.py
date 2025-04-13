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
from colorama import Fore, Style
import json
from datetime import datetime
import re
from PIL import Image
import io

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

banner = f"""{red}
██████╗  ██████╗ ██╗  ██╗
██╔══██╗██╔═══██╗╚██╗██╔╝
██║  ██║██║   ██║ ╚███╔╝ 
██║  ██║██║   ██║ ██╔██╗ 
██████╔╝╚██████╔╝██╔╝ ██╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                By Dryz3R
{reset}"""

class DoxCreator:
    def __init__(self):
        self.info = {}
        self.fields = [
            ("Informations Personnelles", [
                "Prénom",
                "Nom", 
                "Age",
                "Date de naissance",
                "Numéro de téléphone",
                "Email",
                "Adresse",
                "Ville",
                "Code postal",
                "Pays",
                "Nationalité",
                "État civil",
                "Numéro de sécurité sociale",
                "Groupe sanguin",
                "Taille",
                "Poids"
            ]),
            ("Réseaux Sociaux", [
                "Discord ID",
                "Discord Tag", 
                "TikTok",
                "Instagram",
                "Twitter",
                "Facebook",
                "Snapchat",
                "YouTube",
                "LinkedIn",
                "Reddit",
                "Twitch",
                "Steam",
                "Epic Games",
                "PSN",
                "Xbox Live",
                "GitHub",
                "GitLab",
                "Telegram",
                "WhatsApp",
                "Skype"
            ]),
            ("Informations Financières", [
                "Banque",
                "Type de carte",
                "PayPal",
                "Crypto Wallets",
                "Revenus annuels"
            ]),
            ("Informations Professionnelles", [
                "Emploi actuel",
                "Employeur",
                "Salaire",
                "Historique professionnel",
                "École/Université",
                "Diplômes",
                "Compétences"
            ]),
            ("Informations Techniques", [
                "IP",
                "MAC Address",
                "FAI",
                "DNS",
                "User Agent",
                "Système d'exploitation",
                "Navigateur",
                "Langue",
                "Fuseau horaire"
            ])
        ]
        
        self.social_networks = [
            "Discord",
            "TikTok",
            "Instagram", 
            "Twitter",
            "Facebook",
            "Snapchat",
            "YouTube",
            "LinkedIn",
            "Reddit",
            "Pinterest",
            "Twitch",
            "Steam",
            "Epic Games",
            "PSN",
            "Xbox Live",
            "GitHub",
            "GitLab",
            "Telegram",
            "WhatsApp",
            "Skype"
        ]

        self.databases = [
            "HaveIBeenPwned",
            "BreachDirectory",
            "DeHashed",
            "Snusbase",
            "LeakCheck",
            "WeLeakInfo",
            "RaidForums",
            "Pastebin",
            "Github",
            "LinkedIn",
            "Facebook",
            "Twitter"
        ]

    def collect_info(self):
        clear()
        print(banner)
        
        for category, fields in self.fields:
            print(f"\n{red}[{white}+{red}] {white}{category}:{reset}")
            for field in fields:
                value = input(f"{red}[{white}>{red}] {white}{field}: {reset}")
                if value.strip():
                    self.info[field] = value

    def search_social_networks(self, username):
        results = []
        for network in self.social_networks:
            print(f"{red}[{white}*{red}] {white}Recherche sur {network}...{reset}")
            try:
                if network == "Discord" and "Discord ID" in self.info:
                    response = requests.get(f"https://discord.com/api/v9/users/{self.info['Discord ID']}")
                    if response.status_code == 200:
                        data = response.json()
                        results.append(f"Discord: {data.get('username')}#{data.get('discriminator')}")
                        if data.get('avatar'):
                            avatar_url = f"https://cdn.discordapp.com/avatars/{self.info['Discord ID']}/{data.get('avatar')}.png"
                            results.append(f"Avatar Discord: {avatar_url}")
                            self.download_image(avatar_url)
                else:
                    response = requests.get(f"https://api.instantusername.com/check/{network.lower()}/{username}")
                    if response.status_code == 200:
                        data = response.json()
                        if data.get("exists"):
                            results.append(f"Profil {network} trouvé: {username}")
                            if network in ["Instagram", "Facebook", "Twitter"]:
                                self.scrape_profile_image(network, username)
            except:
                continue
        return results

    def search_databases(self):
        results = []
        for db in self.databases:
            if "Email" in self.info:
                email = self.info["Email"]
                print(f"{red}[{white}*{red}] {white}Recherche dans {db}...{reset}")
                try:
                    response = requests.get(f"https://api.{db.lower()}.com/v3/search/{email}")
                    if response.status_code == 200:
                        data = response.json()
                        results.extend([
                            f"Source: {db}",
                            f"Date de la fuite: {data.get('breach_date')}",
                            f"Données compromises: {data.get('data_types')}",
                            f"Hash du mot de passe: {data.get('password_hash')}",
                            f"Autres emails associés: {data.get('associated_emails')}",
                            f"Numéros de téléphone: {data.get('phone_numbers')}",
                            f"Adresses IP: {data.get('ip_addresses')}",
                            f"Historique des connexions: {data.get('login_history')}"
                        ])
                except:
                    continue

        return [r for r in results if r is not None]

    def download_image(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                img = Image.open(io.BytesIO(response.content))
                img.save("profile_image.jpg")
        except:
            pass

    def scrape_profile_image(self, network, username):
        try:
            if network == "Instagram":
                url = f"https://www.instagram.com/{username}/"
            elif network == "Facebook":
                url = f"https://www.facebook.com/{username}/"
            elif network == "Twitter":
                url = f"https://twitter.com/{username}/"
                
            response = requests.get(url)
            if response.status_code == 200:
                img_url = re.search(r'profile_images[^"]+', response.text)
                if img_url:
                    self.download_image(img_url.group(0))
        except:
            pass

    def generate_report(self, filename):
        print(f"\n{red}[{white}*{red}] {white}Génération du rapport...{reset}")
        
        with open(f"{filename}.txt", "w", encoding="utf-8") as f:
            f.write("="*50 + "\n")
            f.write(f"DOX REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Généré par Dryz3R\n")
            f.write("="*50 + "\n\n")

            for category, fields in self.fields:
                f.write(f"\n=== {category} ===\n")
                for field in fields:
                    if field in self.info:
                        f.write(f"{field}: {self.info[field]}\n")

            f.write("\n=== RÉSULTATS DES RECHERCHES ===\n")
            
            if any(field in self.info for field in ["Prénom", "Nom", "Email"]):
                username = self.info.get("Prénom", "") + self.info.get("Nom", "")
                results = self.search_social_networks(username)
                f.write("\n-- Profils sur les réseaux sociaux --\n")
                for result in results:
                    f.write(f"- {result}\n")

            results = self.search_databases()
            if results:
                f.write("\n-- Informations trouvées dans les bases de données --\n")
                for result in results:
                    f.write(f"- {result}\n")

            if os.path.exists("profile_image.jpg"):
                f.write("\n-- Image de profil --\n")
                f.write("Une image de profil a été sauvegardée: profile_image.jpg\n")

            f.write("\nNote: Toutes les informations proviennent de sources publiques.\n")

    def run(self):
        while True:
            self.collect_info()
            
            filename = input(f"\n{red}[{white}>{red}] {white}Nom du fichier pour le rapport: {reset}")
            self.generate_report(filename)
            
            print(f"\n{red}[{white}+{red}] {white}Rapport sauvegardé dans {filename}.txt{reset}")
            
            choice = input(f"\n{red}[{white}>{red}] {white}Créer un nouveau dox? (o/n): {reset}")
            if choice.lower() != 'o':
                break

if __name__ == "__main__":
    doxer = DoxCreator()
    doxer.run()
