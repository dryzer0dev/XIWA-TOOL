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
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import colorama
from colorama import Fore, Style
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import folium
import opencage.geocoder
import time

class PhoneLookupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Number Lookup")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QLabel {
                color: #ff0000;
                font-size: 12px;
            }
            QLineEdit {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #ff0000;
                padding: 5px;
            }
            QPushButton {
                background-color: #ff0000;
                color: #ffffff;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
            QTextEdit {
                background-color: #2d2d2d;
                color: #ff0000;
                border: 1px solid #ff0000;
            }
        """)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        input_layout = QHBoxLayout()
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("+33612345678")
        search_btn = QPushButton("Rechercher")
        search_btn.clicked.connect(self.search_number)
        input_layout.addWidget(self.phone_input)
        input_layout.addWidget(search_btn)
        layout.addLayout(input_layout)
        
        self.results = QTextEdit()
        self.results.setReadOnly(True)
        layout.addWidget(self.results)
        
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_timer.start(500)
        self.animation_dots = 0
        
        self.setMinimumSize(800, 600)
        
    def update_animation(self):
        if not self.results.toPlainText():
            self.animation_dots = (self.animation_dots + 1) % 4
            dots = "." * self.animation_dots
            self.results.setText(f"En attente d'une recherche{dots}")
            
    def search_number(self):
        try:
            number = self.phone_input.text()
            parsed_number = phonenumbers.parse(number)
            
            if not phonenumbers.is_valid_number(parsed_number):
                self.results.setTextColor(QColor("#ff0000"))
                self.results.setText("❌ Numéro invalide")
                return
                
            info = []

            # Simulation de recherche de prénom (pour test uniquement)
            # Recherche d'informations personnelles via des APIs publiques
            info.append("\n👤 INFORMATIONS PERSONNELLES")
            try:
                # Appel à des APIs publiques pour obtenir des infos
                response = requests.get(f"https://api.truecaller.com/v2/search?q={number}", headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if "name" in data:
                        info.append(f"• Prénom: {data['name']}")
                    else:
                        info.append("• Prénom: Non trouvé")
                else:
                    info.append("• Prénom: Non trouvé")
            except:
                info.append("• Prénom: Non trouvé")
            
            info.append("🔍 INFORMATIONS TECHNIQUES")
            info.append(f"• Numéro: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            info.append(f"• Pays: {geocoder.description_for_number(parsed_number, 'fr')}")
            info.append(f"• Opérateur: {carrier.name_for_number(parsed_number, 'fr')}")
            info.append(f"• Type de ligne: {'Mobile' if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else 'Fixe'}")
            info.append(f"• Indicatif pays: +{parsed_number.country_code}")
            info.append(f"• Numéro national: {parsed_number.national_number}")
            
            info.append("\n📍 LOCALISATION")
            region = geocoder.description_for_number(parsed_number, "fr")
            info.append(f"• Région: {region}")
            info.append(f"• Indicatif régional: {str(parsed_number.national_number)[:2]}")
            info.append(f"• Fuseau horaire: {', '.join(timezone.time_zones_for_number(parsed_number))}")
            
            info.append("\n📱 DÉTAILS TECHNIQUES")
            info.append(f"• Format international: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            info.append(f"• Format national: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")
            info.append(f"• Format E164: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
            info.append(f"• Format RFC3966: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.RFC3966)}")
            info.append(f"• Longueur: {len(str(parsed_number.national_number))} chiffres")
            
            info.append("\n🔒 VALIDATION")
            info.append(f"• Numéro valide: {phonenumbers.is_valid_number(parsed_number)}")
            info.append(f"• Numéro possible: {phonenumbers.is_possible_number(parsed_number)}")
            
            self.animation_timer.stop()
            self.results.setTextColor(QColor("#ff0000"))
            self.results.setText("\n".join(info))
            
        except Exception as e:
            self.results.setTextColor(QColor("#ff0000"))
            self.results.setText(f"❌ Erreur: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneLookupWindow()
    window.show()
    sys.exit(app.exec_())
