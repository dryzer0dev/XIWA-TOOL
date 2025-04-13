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

import pandas as pd
import sqlite3
import colorama
from colorama import Fore, Style, Back
import os

colorama.init()

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW

def read_database():
    database_path = input(f"{red}[>] Entrez le chemin de la base de données (.db ou .csv): {Style.RESET_ALL}")

    if not os.path.exists(database_path):
        print(f"{red}[!] Le fichier n'existe pas{Style.RESET_ALL}")
        return

    print(f"{green}[+] Fichier trouvé{Style.RESET_ALL}")

    if database_path.endswith('.csv'):
        try:
            df = pd.read_csv(database_path)
            print("\nContenu du fichier CSV:")
            print(df)
        except Exception as e:
            print(f"{red}[!] Erreur lors de la lecture du CSV: {e}{Style.RESET_ALL}")

    elif database_path.endswith('.db'):
        try:
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            if not tables:
                print(f"{yellow}[!] Aucune table trouvée dans la base de données{Style.RESET_ALL}")
            else:
                print(f"\n{green}[+] Tables trouvées:{Style.RESET_ALL}")
                for table in tables:
                    print(f"\n{blue}Table: {table[0]}{Style.RESET_ALL}")
                    cursor.execute(f"SELECT * FROM {table[0]}")
                    rows = cursor.fetchall()
                    
                    if rows:
                        cursor.execute(f"PRAGMA table_info({table[0]})")
                        columns = [col[1] for col in cursor.fetchall()]
                        df = pd.DataFrame(rows, columns=columns)
                        print(df)
                    else:
                        print(f"{yellow}[!] Table vide{Style.RESET_ALL}")
                        
            conn.close()
            
        except Exception as e:
            print(f"{red}[!] Erreur lors de la lecture de la base SQLite: {e}{Style.RESET_ALL}")
    
    else:
        print(f"{red}[!] Format de fichier non supporté. Utilisez .csv ou .db{Style.RESET_ALL}")

if __name__ == "__main__":
    read_database()