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

import sys
import requests
import json
import time
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
from colorama import Fore, Style
from web3 import Web3
from eth_account import Account
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import ccxt
import secrets
from cryptography.fernet import Fernet

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

class CryptoAnalyzer:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'))
        self.exchange = ccxt.binance({
            'enableRateLimit': True,
            'options': {'defaultType': 'future'}
        })
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        
    def get_live_data(self, crypto):
        url = f"https://api.binance.com/api/v3/klines"
        params = {
            "symbol": f"{crypto}USDT",
            "interval": "1m",
            "limit": 60
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
        df['close'] = pd.to_numeric(df['close'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        return df

    def analyze(self, df):
        sma_20 = df['close'].rolling(window=20).mean().iloc[-1]
        sma_50 = df['close'].rolling(window=50).mean().iloc[-1]
        current_price = df['close'].iloc[-1]
        
        rsi = self.calculate_rsi(df['close'])
        macd = self.calculate_macd(df['close'])
        
        confidence = 0.5 + 0.3 * (1 if sma_20 > sma_50 else -1) + 0.2 * (1 if rsi < 30 else -1 if rsi > 70 else 0)
        
        return {
            "confiance": min(max(confidence, 0), 1),
            "rsi": rsi,
            "macd": macd,
            "sma_20": sma_20,
            "sma_50": sma_50
        }

    def calculate_rsi(self, prices, periods=14):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs.iloc[-1]))

    def calculate_macd(self, prices):
        exp1 = prices.ewm(span=12, adjust=False).mean()
        exp2 = prices.ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        return macd.iloc[-1]

    def execute_buy(self, crypto, amount):
        try:
            order = self.exchange.create_market_buy_order(
                f"{crypto}/USDT",
                amount,
                {'type': 'market'}
            )
            encrypted_order = self.cipher.encrypt(json.dumps(order).encode())
            return True, encrypted_order
        except Exception as e:
            return False, str(e)

    def execute_sell(self, crypto, amount):
        try:
            order = self.exchange.create_market_sell_order(
                f"{crypto}/USDT", 
                amount,
                {'type': 'market'}
            )
            encrypted_order = self.cipher.encrypt(json.dumps(order).encode())
            return True, encrypted_order
        except Exception as e:
            return False, str(e)

class CryptoWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("XiwA Crypto Control")
        self.geometry("1400x900")
        self.configure(bg='#1E1E1E')
        
        acct = Account.create()
        self.wallet_address = acct.address
        
        self.cryptos = {
            "BTC": {"symbol": "BTCUSDT", "color": "#F7931A"},
            "ETH": {"symbol": "ETHUSDT", "color": "#627EEA"},
            "XMR": {"symbol": "XMRUSDT", "color": "#FF6600"},
            "LTC": {"symbol": "LTCUSDT", "color": "#345D9D"},
            "ZEC": {"symbol": "ZECUSDT", "color": "#ECB244"},
            "DASH": {"symbol": "DASHUSDT", "color": "#008CE7"}
        }
        
        self.analyzer = CryptoAnalyzer()
        self.setup_ui()
        
    def setup_ui(self):
        self.header = tk.Label(
            self, 
            text="XiwA Crypto Trading Interface",
            fg="#FF0000",
            bg='#1E1E1E',
            font=("Orbitron", 24, "bold")
        )
        self.header.pack(pady=20)
        self.animate_header()

        main_container = tk.Frame(self, bg='#1E1E1E')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20)

        self.fig, self.ax = plt.subplots(figsize=(8, 6), facecolor='#1E1E1E')
        self.ax.set_facecolor('#2D2D2D')
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_container)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        table_frame = tk.Frame(main_container, bg='#1E1E1E')
        table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(20,0))

        style = ttk.Style()
        style.configure(
            "Custom.Treeview",
            background="#2D2D2D",
            foreground="white",
            fieldbackground="#2D2D2D",
            rowheight=40
        )
        style.configure(
            "Custom.Treeview.Heading",
            background="#1E1E1E",
            foreground="#FF0000",
            font=('Helvetica', 10, 'bold')
        )

        self.table = ttk.Treeview(
            table_frame,
            style="Custom.Treeview", 
            columns=("Crypto", "Prix", "Variation", "RSI", "MACD", "Signal"),
            show="headings",
            height=10
        )

        for col in self.table["columns"]:
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center", width=100)

        self.table.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self, bg='#1E1E1E')
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame,
            text="ACHETER",
            bg="#FF0000",
            fg="white",
            font=("Helvetica", 12, "bold"),
            command=lambda: self.execute_transaction("buy"),
            relief="ridge",
            borderwidth=3
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            btn_frame,
            text="VENDRE",
            bg="#2D2D2D",
            fg="#FF0000",
            font=("Helvetica", 12, "bold"),
            command=lambda: self.execute_transaction("sell"),
            relief="ridge", 
            borderwidth=3
        ).pack(side=tk.LEFT, padx=10)

        self.update_data()
        
    def animate_header(self):
        colors = ['#FF0000', '#CC0000', '#990000', '#CC0000']
        def update_color(idx=0):
            self.header.configure(fg=colors[idx])
            self.after(500, update_color, (idx + 1) % len(colors))
        update_color()

    def update_data(self):
        self.ax.clear()
        for crypto in self.cryptos:
            df = self.analyzer.get_live_data(crypto)
            self.ax.plot(
                df['timestamp'],
                df['close'],
                label=crypto,
                color=self.cryptos[crypto]['color'],
                linewidth=2
            )
        
        self.ax.set_title('Prix en temps réel', color='white', size=12)
        self.ax.set_xlabel('Temps', color='white')
        self.ax.set_ylabel('Prix (USDT)', color='white')
        self.ax.grid(True, alpha=0.2)
        self.ax.legend()
        self.ax.tick_params(colors='white')
        self.canvas.draw()

        for item in self.table.get_children():
            self.table.delete(item)

        for crypto in self.cryptos:
            df = self.analyzer.get_live_data(crypto)
            analysis = self.analyzer.analyze(df)
            
            current_price = df['close'].iloc[-1]
            change = ((current_price - df['close'].iloc[0]) / df['close'].iloc[0]) * 100

            signal = "🟢 ACHAT" if analysis['confiance'] > 0.7 else "🔴 VENTE" if analysis['confiance'] < 0.3 else "⚪ ATTENTE"
            
            self.table.insert("", "end", values=(
                crypto,
                f"${current_price:.2f}",
                f"{change:+.2f}%",
                f"{analysis['rsi']:.1f}",
                f"{analysis['macd']:.4f}",
                signal
            ))

        self.after(1000, self.update_data)

    def execute_transaction(self, type):
        selection = self.table.selection()
        if not selection:
            return
            
        item = self.table.item(selection[0])
        crypto = item['values'][0]
        amount = float(item['values'][1].replace('$',''))
        
        if type == "buy":
            success, result = self.analyzer.execute_buy(crypto, amount)
        else:
            success, result = self.analyzer.execute_sell(crypto, amount)
            
        if success:
            messagebox.showinfo("Succès", f"Transaction {type} exécutée avec succès")
        else:
            messagebox.showerror("Erreur", f"Échec de la transaction: {result}")

def main():
    app = CryptoWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
