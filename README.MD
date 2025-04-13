# XiwA Tool - Suite de Sécurité et d'Analyse

## À Propos
XiwA Tool est une suite complète de sécurité et d'analyse développée par Dryz3R. Cette boîte à outils puissante combine plusieurs fonctionnalités essentielles pour l'analyse de sécurité et le test de vulnérabilités.

## Fonctionnalités Principales

## Installation et Configuration

1. **Prérequis**
   - Python 3.8 ou supérieur
   - pip (gestionnaire de paquets Python)

2. **Installation**
   ```bash
   # Cloner le dépôt
   git clone https://github.com/dryzer0dev/xiwa
   
   # Accéder au répertoire
   cd XiwA-Tool
   
   # Installer les dépendances
   pip install -r requirements.txt
   ```

3. **Configuration**
   - Renommez le fichier `config.example.py` en `config.py`
   - Modifiez les paramètres dans `config.py` selon vos besoins

4. **Lancement**
   ```bash
   python xiwa.py
   ```

## Utilisation

1. **Lancer un scan**
   ```bash
   # Scanner un site web
   python settings/programs/Website-Vulnerability-Scanner.py
   
   # Analyser une base de données
   python settings/programs/read-Data-Base.py
   ```

## Dépannage

- Si vous rencontrez des erreurs de dépendances :
  ```bash
  pip install --upgrade -r requirements.txt
  ```
- Pour les problèmes d'autorisation :
  ```bash
  chmod +x xiwa.py
  ```
