"""
Copyright (c) 2025 Dryz3R - XiwA Tool
All rights reserved.
"""

import os
import subprocess
from colorama import Fore, Style
import time

red = Fore.RED
white = Fore.WHITE
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def parametres():
    global red
    clear()
    animate_banner()
    print(f"{red}╔═══════════════════════════════════════════════════════════════════════════════╗{reset}")
    print(f"{red}║{white}                              PARAMÈTRES{red}                              ║{reset}")
    print(f"{red}╠═══════════════════════════════════════════════════════════════════════════════╣{reset}")
    print(f"{red}║{white} [1] Changer la couleur des menus{red}                                    ║{reset}")
    print(f"{red}║{white} [2] Changer la langue (FR/EN/ES){red}                                   ║{reset}")
    print(f"{red}║{white} [3] Réinitialiser les paramètres{red}                                   ║{reset}")
    print(f"{red}║{white} [4] Sauvegarder la configuration{red}                                   ║{reset}")
    print(f"{red}╚═══════════════════════════════════════════════════════════════════════════════╝{reset}")
    print(f"\n{red}[{white}SELECT{red}]{white} Choix (1-4): ", end="")
    choice = input().strip()
    
    if choice == "1":
        print(f"\n{green}[{white}INFO{green}]{white} Couleurs disponibles :")
        print(f"{white}1. Rouge")
        print(f"{white}2. Bleu")
        print(f"{white}3. Vert")
        print(f"{white}4. Jaune")
        print(f"{white}5. Blanc")
        couleur_choisie = input(f"{red}[{white}SELECT{red}]{white} Entrez le numéro de la couleur : ").strip()
        couleurs = {
            "1": Fore.RED,
            "2": Fore.BLUE,
            "3": Fore.GREEN,
            "4": Fore.YELLOW,
            "5": Fore.WHITE
        }
        if couleur_choisie in couleurs:
            red = couleurs[couleur_choisie]
            print(f"{green}[{white}SUCCESS{green}]{white} Couleur modifiée avec succès!")
        else:
            print(f"{red}[{white}ERREUR{red}]{white} Couleur invalide.")
    elif choice == "2":
        print(f"\n{green}[{white}INFO{green}]{white} Langues disponibles :")
        print(f"{white}1. Français (FR)")
        print(f"{white}2. Anglais (EN)")
        print(f"{white}3. Espagnol (ES)")
        langue_choisie = input(f"{red}[{white}SELECT{red}]{white} Entrez le numéro de la langue : ").strip()
        langues = {
            "1": "FR",
            "2": "EN",
            "3": "ES"
        }
        if langue_choisie in langues:
            print(f"{green}[{white}SUCCESS{green}]{white} Langue modifiée en {langues[langue_choisie]} avec succès!")
        else:
            print(f"{red}[{white}ERREUR{red}]{white} Langue invalide.")
            print("jvais le faire plus tard")
    elif choice == "3":
        print(f"\n{green}[{white}INFO{green}]{white} Réinitialisation des paramètres...")
        print("jvais le faire plus tard")
        try:
            red = Fore.RED
            langue = "FR"
            with open("config.txt", "w") as f:
                f.write("couleur=" + str(red) + "\n")
                f.write("langue=" + langue + "\n")
            time.sleep(1)
            print(f"{green}[{white}SUCCESS{green}]{white} Paramètres réinitialisés par défaut et sauvegardés dans config.txt!")
        except Exception as e:
            print(f"{red}[{white}ERREUR{red}]{white} Impossible de réinitialiser : {e}")
    elif choice == "4":
        print(f"\n{green}[{white}INFO{green}]{white} Sauvegarde de la configuration...")
        print("jvais le faire plus tard")
        try:
            print("jvais le faire plus tard")
            langue = "FR"
            with open("config.txt", "w") as f:
                f.write("couleur=" + str(red) + "\n")
                f.write("langue=" + langue + "\n")
            print(f"{green}[{white}SUCCESS{green}]{white} Configuration sauvegardée dans config.txt!")
        except Exception as e:
            print(f"{red}[{white}ERREUR{red}]{white} Impossible de sauvegarder : {e}")
    
    input(f"\n{red}[{white}CONTINUE{red}]{white} Appuyez sur Entrée pour continuer...")
    clear()

def mettre_a_jour():
    clear()
    animate_banner()
    print(f"{red}╔═══════════════════════════════════════════════════════════════════════════════╗{reset}")
    print(f"{red}║{white}                              MISE À JOUR{red}                              ║{reset}")
    print(f"{red}╠═══════════════════════════════════════════════════════════════════════════════╣{reset}")
    print(f"{red}║{white} [1] Mettre à jour depuis GitHub{red}                                    ║{reset}")
    print(f"{red}║{white} [2] Réinstaller complètement{red}                                       ║{reset}")
    print(f"{red}║{white} [3] Vérifier les mises à jour{red}                                     ║{reset}")
    print(f"{red}║{white} [4] Sauvegarder avant mise à jour{red}                                 ║{reset}")
    print(f"{red}╚═══════════════════════════════════════════════════════════════════════════════╝{reset}")
    print(f"\n{red}[{white}SELECT{red}]{white} Choix (1-4): ", end="")
    choice = input().strip()
    
    if choice == "1":
        print(f"\n{green}[{white}INFO{green}]{white} Téléchargement de la mise à jour depuis GitHub...")
        try:
            subprocess.run(["git", "pull"], check=True)
            print(f"{green}[{white}SUCCESS{green}]{white} Mise à jour terminée avec succès!")
        except Exception as e:
            print(f"{red}[{white}ERREUR{red}]{white} Impossible de mettre à jour : {e}")
    elif choice == "2":
        print(f"\n{green}[{white}INFO{green}]{white} Réinstallation complète en cours...")
        try:
            subprocess.run(["git", "fetch", "--all"], check=True)
            subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
            print(f"{green}[{white}SUCCESS{green}]{white} Réinstallation terminée avec succès!")
        except Exception as e:
            print(f"{red}[{white}ERREUR{red}]{white} Impossible de réinstaller : {e}")
    elif choice == "3":
        print(f"\n{green}[{white}INFO{green}]{white} Vérification des mises à jour...")
        try:
            result = subprocess.run(["git", "fetch"], capture_output=True)
            status = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True)
            if "Votre branche est à jour" in status.stdout or "Your branch is up to date" in status.stdout:
                print(f"{green}[{white}SUCCESS{green}]{white} Aucune mise à jour disponible!")
            else:
                print(f"{yellow}[{white}INFO{yellow}]{white} Des mises à jour sont disponibles.")
        except Exception as e:
            print(f"{red}[{white}ERREUR{red}]{white} Impossible de vérifier les mises à jour : {e}")
    elif choice == "4":
        print(f"\n{green}[{white}INFO{green}]{white} Sauvegarde des fichiers avant mise à jour...")
        try:
            import shutil
            if not os.path.exists("backup"):
                os.makedirs("backup")
            for filename in os.listdir("."):
                if filename.endswith(".py") or filename == "config.txt":
                    shutil.copy(filename, os.path.join("backup", filename))
            print(f"{green}[{white}SUCCESS{green}]{white} Sauvegarde terminée dans le dossier 'backup'!")
        except Exception as e:
            print(f"{red}[{white}ERREUR{red}]{white} Impossible de sauvegarder : {e}")
    
    input(f"\n{red}[{white}CONTINUE{red}]{white} Appuyez sur Entrée pour continuer...")
    clear()

def animate_banner():
    clear()
    time.sleep(0.03)
    print(red + f"                                    ██╗  ██╗██╗██╗    ██╗ █████╗ ")
    time.sleep(0.03)
    print(f"                                    ╚██╗██╔╝██║██║    ██║██╔══██╗")
    time.sleep(0.03)
    print(f"                                     ╚███╔╝ ██║██║ █╗ ██║███████║")
    time.sleep(0.03)
    print(f"                                     ██╔██╗ ██║██║███╗██║██╔══██║")
    time.sleep(0.03)
    print(f"                                    ██╔╝ ██╗██║╚███╔███╔╝██║  ██║")
    time.sleep(0.03)
    print(f"                                    ╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝")
    time.sleep(0.1)
    time.sleep(0.1)
    print(f"{red}{' ' * 25}[{red} i {red}] Paramètre {red} [{red} j {red}] Mettre à jour {red}")

def draw_box(title, content, width=30):
    top = f"╭{'─' * (width-2)}╮"
    title_line = f"│ {title.center(width-4)} │"
    bottom = f"╰{'─' * (width-2)}╘"
    
    print(red + top + reset)
    print(red + title_line + reset)
    for line in content:
        print(red + f"│ {white}{line.ljust(width-4)}{red} │" + reset)
    print(red + bottom + reset)

def animate_menu():
    animate_banner()
    
    main_options = [f"({white}{k}{red}) {menus[k]['title']}" for k in menus]
    col1 = main_options[:4] 
    col2 = main_options[4:] 
    
    max_rows = max(len(col1), len(col2))
    for i in range(max_rows):
        line = " " * 20
        if i < len(col1):
            line += red + " " + col1[i].ljust(35)
        else:
            line += " " * 36
            
        if i < len(col2):
            line += red + " " + col2[i].ljust(35)
        print(line + reset)
        time.sleep(0.05)
    
    print()

def animate_submenu(menu_id):
    animate_banner()
    menu = menus[menu_id]
    options = [opt for opt in menu["options"] if opt.strip() != ""]
    n = len(options)
    
    cols = 2
    col_width = 32
    option_padding = 4  
    
    items_per_col = (n + cols - 1) // cols
    
    def make_border(side):
        return red + side + " " * (col_width - 6) + "   " + side
    
    top_border = (
        red + "╔═══" + " " * (col_width - 6) + "═══╗" + "  " +
        "╔═══" + " " * (col_width - 6) + "═══╗" + reset
    )
    
    bottom_border = (
        red + "╚═══" + " " * (col_width - 6) + "═══╝" + "  " +
        "╚═══" + " " * (col_width - 6) + "═══╝" + reset
    )
    
    print(" " * 7 + top_border)
    
    for i in range(items_per_col):
        line = " " * 9
        for col in range(cols):
            idx = col * items_per_col + i
            if idx < n:
                opt_num = f"{idx + 1:02d}"
                option = options[idx]
                line += (red + "   (" + white + opt_num + red + ") > " + 
                         white + option.ljust(col_width - 12) + red + "   ")
            else:
                line += red + " " * (col_width + 6)
        print(line)
    
    print(" " * 7 + bottom_border)
    
    print(f"\n{' ' * 38}{red}   ({white}00{red}) > Return to Main Menu{reset}\n")

menus = {
    "1": {
        "title": "SECURITY TOOLS",
        "options": [
            "Vuln Scanner",
            "Brute Force",
            "Network Scanner",
            "Password Cracker",
            "Exploit Framework",
            "Data Base Site Stealer",
            "piratattHack",
            "Botnet Builder",
            "Ransomware Builder"
        ]
    },
    "2": {
        "title": "DISCORD TOOLS",
        "options": [
            "Webhook Spammer",
            "Token Checker",
            "Member Scraper",
            "Member Trusser",
            "Propriety Transfert",
            "Server Nuker",
            "Nitro Auto Claim",
            "ID Lookup",
            "Vocal DDoS",
            "Bot Creator",
            "Discord Boost Bot"
        ]
    },
    "3": {
        "title": "OSINT TOOLS",
        "options": [
            "Phone OSINT",
            "Email OSINT",
            "Username OSINT",
            "IP OSINT",
            "Identity Search",
            "Dox Creator",
            "Info Stealer",
            "Server Scanner",
            "Phone Locator"
        ]
    },
    "4": {
        "title": "PRIVACY TOOLS",
        "options": [
            "Anonymization",
            "Financial Control",
            "", "", "", "", "", "", ""
        ]
    }
}

def main_loop():
    while True:
        animate_menu()
        
        menu_choice = input(f"\n{red}[{white}SELECT{red}]{white} Menu choice (1-4, i, j): ").strip().lower()
        
        if menu_choice == "i":
            parametres()
            continue
        elif menu_choice == "j":
            mettre_a_jour()
            continue
        elif menu_choice not in menus:
            clear()
            continue

        while True:
            clear()
            animate_submenu(menu_choice)
            max_options = len(menus[menu_choice]["options"])
            option_choice = input(f"\n{red}[{white}SELECT{red}]{white} Option choice (00-{max_options:02d}): ").strip()
            if not option_choice.isdigit() or int(option_choice) not in range(0, max_options + 1):
                clear()
                continue
            if option_choice == "00":
                clear()
                break
            option_index = int(option_choice) - 1
            selected_option = menus[menu_choice]["options"][option_index].replace(" ", "-")
            script_path = f"settings/programs/{selected_option}.py"
            clear()
            animate_banner()
            if os.path.exists(script_path):
                print(f"\n{green}[{white}INITIALIZING{green}]{white} Launching {selected_option}...")
                time.sleep(1)
                print(f"{green}[{white}LOADING{green}]{white} Preparing resources...")
                time.sleep(1)
                clear()
                subprocess.run(["python", script_path])
                input(f"\n{red}[{white}CONTINUE{red}]{white} Press Enter to continue...")
                clear()
            else:
                print(f"\n{red}[{white}ERROR{red}]{white} Module '{selected_option}' is not installed!{reset}")
                time.sleep(2)
                clear()

if __name__ == "__main__":
    main_loop()