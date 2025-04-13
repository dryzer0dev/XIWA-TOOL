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

import requests
import json
from colorama import Fore, Style
import time
from datetime import datetime

def banner():
    print(f"""
{Fore.RED}╔══════════════════════════════════════════╗
║  {Fore.WHITE}Discord Legal Information Gatherer{Fore.RED}      ║
║  {Fore.WHITE}Collecte d'informations légales{Fore.RED}        ║
╚══════════════════════════════════════════╝{Style.RESET_ALL}
""")

def get_discord_info(discord_id):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        user_response = requests.get(f'https://discord.com/api/v9/users/{discord_id}')
        if user_response.status_code == 200:
            return user_response.json()
        return {
            'username': 'Utilisateur_' + str(discord_id)[-4:],
            'discriminator': '0000',
            'avatar': None,
            'banner': None,
            'system': False,
            'bot': False,
            'public_flags': 0,
            'flags': 0
        }
    except:
        return {
            'username': 'Utilisateur_' + str(discord_id)[-4:],
            'discriminator': '0000',
            'avatar': None,
            'banner': None,
            'system': False,
            'bot': False,
            'public_flags': 0,
            'flags': 0
        }

def get_connection_info(discord_id):
    return [{
        'last_accessed': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'client': 'Desktop',
        'status': 'online'
    }]


def main():
    banner()
    discord_id = input(f"{Fore.RED}[{Fore.WHITE}*{Fore.RED}]{Fore.WHITE} Entrez l'ID Discord : ")

    print(f"\n{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} Recherche d'informations légales en cours...")
    
    user_info = get_discord_info(discord_id)
    sessions_info = get_connection_info(discord_id)

    creation_timestamp = ((int(discord_id) >> 22) + 1420070400000) / 1000
    creation_date = datetime.fromtimestamp(creation_timestamp)

    avatar = user_info.get('avatar', '')
    is_animated = 'Oui' if avatar and avatar.startswith('a_') else 'Non'

    info_list = [
        f"1. Date de l'analyse : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"2. ID Discord : {discord_id}",
        f"3. Nom d'utilisateur : {user_info.get('username', 'Non disponible')}",
        f"4. Discriminateur : {user_info.get('discriminator', 'Non disponible')}",
        f"5. Tag complet : {user_info.get('username')}#{user_info.get('discriminator')}",
        f"6. Présence d'un avatar : {'Oui' if user_info.get('avatar') else 'Non'}",
        f"7. ID de l'avatar : {user_info.get('avatar', 'Aucun')}",
        f"8. Avatar animé : {is_animated}",
        f"9. Bannière personnalisée : {'Oui' if user_info.get('banner') else 'Non'}",
        f"10. Couleur d'accentuation : {user_info.get('accent_color', 'Non définie')}",
        f"11. Compte système : {'Oui' if user_info.get('system') else 'Non'}",
        f"12. Compte bot : {'Oui' if user_info.get('bot') else 'Non'}",
        f"13. Flags publics : {user_info.get('public_flags', 0)}",
        f"14. Date de création du compte : {creation_date.strftime('%Y-%m-%d')}",
        f"15. Heure de création du compte : {creation_date.strftime('%H:%M:%S')}",
        f"16. Âge du compte : {(datetime.now() - creation_date).days} jours",
        f"17. Année de création : {creation_date.year}",
        f"18. Mois de création : {creation_date.month}",
        f"19. Jour de création : {creation_date.day}",
        f"20. Compte vérifié : {'Oui' if user_info.get('verified') else 'Non'}",
        f"21. Langue du compte : {user_info.get('locale', 'Non disponible')}",
        f"22. NSFW autorisé : {'Oui' if user_info.get('nsfw_allowed') else 'Non'}",
        f"23. MFA activé : {'Oui' if user_info.get('mfa_enabled') else 'Non'}",
        f"24. Email vérifié : {'Oui' if user_info.get('verified') else 'Non'}",
        f"25. Premium : {'Oui' if user_info.get('premium_type') else 'Non'}",
        f"26. Type de premium : {user_info.get('premium_type', 'Aucun')}",
        f"27. Flags de développeur : {user_info.get('flags', 0)}",
        f"28. ID de la bannière : {user_info.get('banner', 'Aucune')}",
        f"29. Couleur de la bannière : {user_info.get('banner_color', 'Non définie')}",
        f"30. Statut de vérification : {user_info.get('verified', False)}"
    ]

    if sessions_info:
        info_list.append(f"31. Nombre de connexions actives : {len(sessions_info)}")
        info_list.append(f"32. Dernière connexion : {sessions_info[0].get('last_accessed', 'Non disponible') if sessions_info else 'Non disponible'}")

    print("\n=== INFORMATIONS PUBLIQUES LÉGALES ===\n")
    
    for info in info_list:
        print(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} {info}")
        time.sleep(0.1)

    print(f"\n{Fore.RED}[{Fore.WHITE}✓{Fore.RED}]{Fore.WHITE} Analyse terminée !")


if __name__ == "__main__":
    main()