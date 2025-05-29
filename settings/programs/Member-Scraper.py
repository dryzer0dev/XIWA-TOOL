import os
import requests
from colorama import Fore, Style
import discord
from discord.ext import commands

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

def main():
    banner()
    print(f"{red}1. Scrap Discord Members")
    print(f"2. Quitter{reset}")
    choice = input(f"\n{red}Choisissez une option (1/2) : {reset}")

    if choice == "1":
        token = input(f"{red}Entrez votre token Discord : {reset}")
        guild_id = input(f"{red}Entrez l'ID du serveur Discord : {reset}")
        bot = commands.Bot(command_prefix="!", self_bot=True)
        bot.run(token, bot=False)
        guild = bot.get_guild(int(guild_id))
        members = guild.members
        with open("members.txt", "w") as f:
            for member in members:
                f.write(member.id + "\n")
        print(f"{red}Membres scrapés avec succès !{reset}")
    elif choice == "2":
        print(f"{red}Au revoir !{reset}")
        quit()
    else:
        print(f"{red}[!] Option invalide.{reset}")
        main()

if __name__ == "__main__":
    main()


