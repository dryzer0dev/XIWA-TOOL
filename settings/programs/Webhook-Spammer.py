import os
import requests
from colorama import Fore, Style

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"""{red}
██╗  ██╗██╗██╗    ██╗ █████╗ 
╚██╗██╔╝██║██║    ██║██╔══██╗
 ╚███╔╝ ██║██║ █╗ ██║███████║
 ██╔██╗ ██║██║███╗██║██╔══██║
██╔╝ ██╗██║╚███╔███╔╝██║  ██║
╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
                                    {white}Version 0{reset}
                                    {red}XIWA OWNS YOU{reset}
""")

def spam_webhook(webhook, message):
    while True:
        try:
            requests.post(webhook, json={"content": message})
            print(f"{red}[+] Message envoyé avec succès !{reset}")
        except Exception as e:
            print(f"{red}[!] Erreur lors de l'envoi du message: {e}{reset}")

def main():
    banner()
    print(f"{red}1. Spammer Webhook")
    print(f"2. Quitter{reset}")
    choice = input(f"\n{red}Choisissez une option (1/2) : {reset}")

    if choice == "1":
        webhook = input(f"{red}Entrez le Webhook à spammer : {reset}")
        message = input(f"{red}Entrez le message à envoyer : {reset}")
        spam_webhook(webhook, message)
    elif choice == "2":
        print(f"{red}Au revoir !{reset}")
        quit()
    else:
        print(f"{red}[!] Option invalide.{reset}")
        main()

if __name__ == "__main__":
    main()


