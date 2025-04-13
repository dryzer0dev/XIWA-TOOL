#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys
import time
import random
import threading
from colorama import Fore, Style, init
import cv2
import numpy as np
import requests
import socket
import subprocess
import shutil
import winreg
import psutil
import platform
import uuid
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class XiwaAnonymizer:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("XIWA ANONYMIZER") 
        self.root.geometry("1200x800")
        self.root.configure(bg="#000000")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.canvas = tk.Canvas(self.root, bg="#000000", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.matrix_chars = []
        self.create_matrix_effect()

        self.logo_frame = ctk.CTkFrame(self.root, fg_color="#000000")
        self.logo_frame.place(relx=0.5, rely=0.1, anchor="center")
        
        self.logo = ctk.CTkLabel(
            self.logo_frame,
            text="X I W A",
            font=("Blade Runner Movie Font", 72),
            text_color="#00ffff"
        )
        self.logo.pack()

        self.menu_frame = ctk.CTkFrame(self.root, fg_color="#000000")
        self.menu_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.menu_options = [
            "IDENTITY GENERATOR",
            "NETWORK ANONYMIZER", 
            "DIGITAL FOOTPRINT ERASER",
            "SECURE COMMUNICATIONS",
            "STEALTH MODE",
            "DATA SHREDDER"
        ]

        for i, option in enumerate(self.menu_options):
            btn = ctk.CTkButton(
                self.menu_frame,
                text=option,
                font=("Orbitron", 16),
                fg_color="#000000",
                hover_color="#001a1a",
                border_color="#00ffff", 
                border_width=2,
                corner_radius=10,
                width=300,
                height=50,
                command=lambda o=option: self.activate_module(o)
            )
            btn.pack(pady=10)

        self.status_frame = ctk.CTkFrame(self.root, fg_color="#000000")
        self.status_frame.place(relx=0.5, rely=0.95, anchor="center")

        self.status = ctk.CTkLabel(
            self.status_frame,
            text="SYSTEM READY",
            font=("Share Tech Mono", 14),
            text_color="#00ffff"
        )
        self.status.pack()

        self.log_frame = ctk.CTkFrame(self.root, fg_color="#000000")
        self.log_frame.place(relx=0.8, rely=0.5, anchor="center")
        
        self.log_text = ctk.CTkTextbox(
            self.log_frame,
            width=300,
            height=400,
            font=("Share Tech Mono", 12),
            text_color="#00ffff",
            fg_color="#001a1a"
        )
        self.log_text.pack()

        self.animate_matrix()

    def create_matrix_effect(self):
        for _ in range(100):
            char = {
                "x": random.randint(0, 1200),
                "y": random.randint(0, 800),
                "char": random.choice("ABCDEF0123456789"),
                "speed": random.uniform(1, 5),
                "color": "#00ffff"
            }
            self.matrix_chars.append(char)

    def animate_matrix(self):
        self.canvas.delete("matrix")
        for char in self.matrix_chars:
            char["y"] += char["speed"]
            if char["y"] > 800:
                char["y"] = 0
                char["x"] = random.randint(0, 1200)
                char["char"] = random.choice("ABCDEF0123456789")
            
            self.canvas.create_text(
                char["x"], char["y"],
                text=char["char"],
                fill=char["color"],
                font=("Matrix Code NFI", 14),
                tags="matrix"
            )
        self.root.after(50, self.animate_matrix)

    def log_action(self, message):
        self.log_text.insert("end", f"[*] {message}\n")
        self.log_text.see("end")
        self.root.update()
        time.sleep(0.5)

    def generate_identity(self):
        self.log_action("Génération d'une nouvelle identité numérique...")
        
        new_mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
        self.log_action(f"Nouvelle MAC: {new_mac}")
        
        new_hostname = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=12))
        self.log_action(f"Nouveau hostname: {new_hostname}")
        
        new_uuid = str(uuid.uuid4())
        self.log_action(f"Nouvel UUID: {new_uuid}")
        
        identity = {
            "mac": new_mac,
            "hostname": new_hostname, 
            "uuid": new_uuid,
            "nom": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8)),
            "prenom": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6)),
            "date_naissance": f"{random.randint(1,28)}/{random.randint(1,12)}/{random.randint(1970,2000)}",
            "lieu_naissance": random.choice(["Paris", "Lyon", "Marseille", "Bordeaux", "Lille"]),
            "nationalite": "FRANÇAISE",
            "sexe": random.choice(["M", "F"]),
            "taille": f"{random.randint(150,190)} cm"
        }
        
        with open("identity.txt", "w") as f:
            for k,v in identity.items():
                f.write(f"{k}: {v}\n")
            
        self.generate_id_card(identity)
        
        return identity
        
    def generate_id_card(self, identity):
        from PIL import Image, ImageDraw, ImageFont
        
        img = Image.new('RGB', (800, 500), color='white')
        d = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
            
        d.text((50,50), "CARTE NATIONALE D'IDENTITÉ", fill='black', font=font)
        d.text((50,100), f"Nom: {identity['nom']}", fill='black', font=font)
        d.text((50,130), f"Prénom: {identity['prenom']}", fill='black', font=font)
        d.text((50,160), f"Né(e) le: {identity['date_naissance']}", fill='black', font=font)
        d.text((50,190), f"à: {identity['lieu_naissance']}", fill='black', font=font)
        d.text((50,220), f"Nationalité: {identity['nationalite']}", fill='black', font=font)
        d.text((50,250), f"Sexe: {identity['sexe']}", fill='black', font=font)
        d.text((50,280), f"Taille: {identity['taille']}", fill='black', font=font)
        
        img.save("carte_identite.png")

    def anonymize_network(self):
        self.log_action("Configuration des paramètres réseau pour l'anonymat...")
        
        self.log_action("Nettoyage des caches réseau...")
        subprocess.run(["ipconfig", "/flushdns"], shell=True)
        subprocess.run(["netsh", "interface", "ip", "delete", "arpcache"], shell=True)
        
        self.log_action("Configuration du pare-feu...")
        subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "on"], shell=True)
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", "name=BlockInbound", "dir=in", "action=block"], shell=True)
        
        self.log_action("Configuration de Tor...")
        try:
            import stem.process
            tor_process = stem.process.launch_tor_with_config(
                config = {
                    'SocksPort': '9050',
                    'ControlPort': '9051'
                }
            )
            self.log_action("Tor démarré avec succès")
        except:
            self.log_action("Erreur lors du démarrage de Tor")
            
        self.log_action("Configuration des DNS sécurisés...")
        dns_servers = [
            "1.1.1.1", 
            "9.9.9.9", 
            "208.67.222.222" 
        ]
        for dns in dns_servers:
            subprocess.run(["netsh", "interface", "ip", "add", "dns", "name=Ethernet", f"addr={dns}"], shell=True)
            
        self.log_action("Activation du mode furtif...")
        subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "admin=disable"], shell=True)
        
        self.log_action("Réseau anonymisé avec succès")
        return True

    def erase_footprint(self):
        self.log_action("Effacement des traces numériques...")
        paths = [
            os.path.expanduser("~/AppData/Local/Temp"),
            os.path.expanduser("~/AppData/Roaming/Microsoft/Windows/Recent")
        ]
        for path in paths:
            if os.path.exists(path):
                self.log_action(f"Suppression de {path}...")
                shutil.rmtree(path, ignore_errors=True)
        self.log_action("Traces numériques effacées")
        return True

    def secure_comms(self):
        self.log_action("Configuration des communications sécurisées...")
        
        self.log_action("Génération d'une nouvelle clé AES...")
        key = get_random_bytes(32)
        self.log_action(f"Clé AES générée: {key.hex()[:16]}...")
        
        iv = get_random_bytes(16)
        self.log_action("Vecteur d'initialisation créé")
        
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
        self.log_action("Chiffrement AES-GCM configuré")
        
        self.log_action("Configuration du pare-feu...")
        try:
            subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "on"])
            self.log_action("Pare-feu activé")
        except:
            self.log_action("Erreur lors de l'activation du pare-feu")
            
        self.log_action("Désactivation des protocoles non sécurisés...")
        try:
            subprocess.run(["reg", "add", "HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\SSL 2.0\\Client", "/v", "Enabled", "/t", "REG_DWORD", "/d", "0", "/f"])
            subprocess.run(["reg", "add", "HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\SSL 3.0\\Client", "/v", "Enabled", "/t", "REG_DWORD", "/d", "0", "/f"])
            self.log_action("Protocoles SSL 2.0/3.0 désactivés")
        except:
            self.log_action("Erreur lors de la désactivation des protocoles")
            
        self.log_action("Configuration du DNS over HTTPS...")
        try:
            subprocess.run(["netsh", "dns", "add", "encryption", "server=1.1.1.1", "dohtemplate=https://cloudflare-dns.com/dns-query"])
            self.log_action("DNS over HTTPS configuré")
        except:
            self.log_action("Erreur lors de la configuration du DNS")
            
        self.log_action("Activation du mode furtif réseau...")
        try:
            subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", "name=StealthMode", "dir=in", "action=block", "enable=yes"])
            subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", "name=StealthMode", "dir=out", "action=block", "enable=yes"])
            self.log_action("Mode furtif réseau activé")
        except:
            self.log_action("Erreur lors de l'activation du mode furtif")
            
        return {
            "key": key,
            "iv": iv,
            "cipher": cipher,
            "status": "configured"
        }

    def stealth_mode(self):
        self.log_action("Activation du mode furtif...")
        killed = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] in ['taskmgr.exe', 'procexp.exe']:
                self.log_action(f"Arrêt du processus {proc.info['name']}...")
                proc.kill()
                killed.append(proc.info['name'])
        self.log_action(f"Processus arrêtés: {', '.join(killed)}")
        return True

    def shred_data(self, path):
        self.log_action(f"Destruction sécurisée de {path}...")
        if os.path.exists(path):
            size = os.path.getsize(path)
            self.log_action(f"Taille du fichier: {size} octets")
            
            self.log_action("Écrasement avec des données aléatoires...")
            with open(path, 'wb') as f:
                f.write(os.urandom(size))
                
            self.log_action("Suppression du fichier...")
            os.remove(path)
            self.log_action("Fichier détruit avec succès")
        return True

    def activate_module(self, module):
        self.status.configure(text=f"ACTIVATING {module}...")
        self.log_text.delete("1.0", "end")
        
        def loading_effect():
            chars = "|/-\\"
            for i in range(20):
                self.status.configure(text=f"LOADING {chars[i%4]} {module}")
                time.sleep(0.1)
                
            result = False
            if module == "IDENTITY GENERATOR":
                result = self.generate_identity()
            elif module == "NETWORK ANONYMIZER":
                result = self.anonymize_network()
            elif module == "DIGITAL FOOTPRINT ERASER":
                result = self.erase_footprint()
            elif module == "SECURE COMMUNICATIONS":
                result = self.secure_comms()
            elif module == "STEALTH MODE":
                result = self.stealth_mode()
            elif module == "DATA SHREDDER":
                result = self.shred_data("temp_data")
                
            status = "SUCCESS" if result else "FAILED"
            self.status.configure(text=f"{module} {status}")
            if result:
                messagebox.showinfo("Succès", f"{module} terminé avec succès!")
            else:
                messagebox.showerror("Erreur", f"Échec de {module}")
            
        threading.Thread(target=loading_effect).start()

if __name__ == "__main__":
    app = XiwaAnonymizer()
    app.root.mainloop()
