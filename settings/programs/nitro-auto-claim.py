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
import requests
import json
import time
import threading
import base64
import re
import random
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class NitroAutoClaim(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Discord Nitro Auto-Claim")
        self.geometry("800x600")
        self.configure(fg_color="#1a1a1a")

        self.main_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="NITRO AUTO-CLAIM",
            font=("Roboto", 36, "bold"),
            text_color="#5865F2"
        )
        self.title_label.pack(pady=20)

        self.webhook_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="#2d2d2d",
            corner_radius=15
        )
        self.webhook_frame.pack(fill="x", padx=20, pady=10)

        self.webhook_entry = ctk.CTkEntry(
            self.webhook_frame,
            placeholder_text="Webhook URL",
            width=400
        )
        self.webhook_entry.pack(pady=10)

        self.token_entry = ctk.CTkEntry(
            self.webhook_frame,
            placeholder_text="Token Discord",
            width=400
        )
        self.token_entry.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Status: En attente",
            font=("Roboto", 14),
            text_color="#ffffff"
        )
        self.status_label.pack(pady=10)

        self.start_button = ctk.CTkButton(
            self.main_frame,
            text="DÉMARRER L'AUTO-CLAIM",
            font=("Roboto", 20, "bold"),
            fg_color="#5865F2",
            hover_color="#4752C4",
            corner_radius=10,
            height=50,
            command=self.start_claiming
        )
        self.start_button.pack(pady=20)

        self.is_running = False
        self.nitro_claimed = 0

    def claim_nitro(self, code, token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
            headers=headers
        )
        
        return response.status_code == 200

    def log_nitro(self, code, webhook_url):
        data = {
            "content": f"🎮 Nouveau Nitro récupéré!\n```Code: discord.gift/{code}```",
            "username": "Nitro Auto-Claim",
            "avatar_url": "https://discord.com/assets/0f4d1ff76624bb45a3fee4189279ee92.svg"
        }
        requests.post(webhook_url, json=data)

    def scan_messages(self, token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        channels_endpoint = "https://discord.com/api/v9/users/@me/channels"
        response = requests.get(channels_endpoint, headers=headers)
        
        if response.status_code == 200:
            channels = response.json()
            
            for channel in channels:
                messages_endpoint = f"https://discord.com/api/v9/channels/{channel['id']}/messages"
                messages = requests.get(messages_endpoint, headers=headers).json()
                
                for message in messages:
                    nitro_codes = re.findall(r'discord\.gift/([a-zA-Z0-9]+)', message.get('content', ''))
                    
                    for code in nitro_codes:
                        if self.claim_nitro(code, token):
                            self.nitro_claimed += 1
                            self.log_nitro(code, self.webhook_entry.get())
                            self.status_label.configure(
                                text=f"Status: {self.nitro_claimed} Nitro récupérés | Scan en cours..."
                            )

    def auto_claim_loop(self):
        while self.is_running:
            token = self.token_entry.get()
            if token:
                try:
                    self.scan_messages(token)
                except Exception as e:
                    print(f"Erreur: {e}")
            time.sleep(30)

    def start_claiming(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.configure(
                text="AUTO-CLAIM ACTIF",
                state="disabled",
                fg_color="#43B581"
            )
            threading.Thread(target=self.auto_claim_loop, daemon=True).start()

def main():
    app = NitroAutoClaim()
    app.mainloop()

if __name__ == "__main__":
    main()

