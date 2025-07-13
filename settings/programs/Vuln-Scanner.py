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

import requests
import json
from requests.exceptions import RequestException
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import socket
import ssl
import whois
import threading
import concurrent.futures
import os
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, Style
import re

def banner():
    print(f"""{Fore.RED}
╔══════════════════════════════════════╗
║     Website Vulnerability Scanner     ║
╚══════════════════════════════════════╝{Style.RESET_ALL}
""")

def check_headers(url):
    try:
        response = requests.head(url, verify=False, timeout=10)
        headers = response.headers
        security_headers = {
            'Strict-Transport-Security': 'Missing HSTS header',
            'X-Frame-Options': 'Clickjacking possible',
            'X-Content-Type-Options': 'MIME-sniffing possible',
            'Content-Security-Policy': 'Missing CSP header',
            'X-XSS-Protection': 'XSS protection disabled',
            'Referrer-Policy': 'Missing Referrer Policy',
            'Permissions-Policy': 'Missing Permissions Policy',
            'X-Permitted-Cross-Domain-Policies': 'Missing X-Permitted-Cross-Domain-Policies'
        }
        
        findings = []
        for header, risk in security_headers.items():
            if header not in headers:
                findings.append(risk)
        
        # Vérifier les valeurs des headers
        if 'X-Frame-Options' in headers and headers['X-Frame-Options'] == 'DENY':
            findings.append("X-Frame-Options correctement configuré")
        
        if 'Content-Security-Policy' in headers:
            findings.append("CSP header présent")
        
        return findings
    except Exception as e:
        return [f"Impossible de vérifier les headers: {str(e)}"]

def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                if cert is None:
                    return "Certificat SSL non disponible"
                
                # Gérer différents formats de date
                not_after = cert.get('notAfter')
                if not_after:
                    try:
                        # Essayer différents formats de date
                        date_formats = [
                            '%b %d %H:%M:%S %Y %Z',
                            '%b %d %H:%M:%S %Y GMT',
                            '%Y%m%d%H%M%SZ'
                        ]
                        
                        expiry = None
                        for fmt in date_formats:
                            try:
                                expiry = datetime.strptime(str(not_after), fmt)
                                break
                            except ValueError:
                                continue
                        
                        if expiry:
                            if expiry < datetime.now():
                                return "Certificat SSL expiré"
                            else:
                                return f"SSL OK - Expire le {expiry.strftime('%Y-%m-%d')}"
                        else:
                            return f"SSL OK - Date d'expiration: {not_after}"
                    except Exception as e:
                        return f"SSL OK - Erreur parsing date: {not_after}"
                else:
                    return "Certificat SSL sans date d'expiration"
    except Exception as e:
        return f"Pas de SSL ou erreur SSL: {str(e)}"

def scan_port(domain, port):
    """Scan un port spécifique"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((domain, port))
        sock.close()
        
        if result == 0:
            service_name = get_service_name(port)
            return f"Port {port} ({service_name}) - OUVERT"
        return None
    except:
        return None

def get_service_name(port):
    """Retourne le nom du service pour un port donné"""
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        993: "IMAPS",
        995: "POP3S",
        1433: "MSSQL",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        5900: "VNC",
        6379: "Redis",
        8080: "HTTP-Proxy",
        8443: "HTTPS-Alt",
        27017: "MongoDB"
    }
    return services.get(port, "Unknown")

def scan_ports(domain):
    """Scan les ports sans nmap"""
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 1433, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017]
    
    open_ports = []
    print(f"{Fore.YELLOW}[*] Scanning ports...{Style.RESET_ALL}")
    
    # Utiliser ThreadPoolExecutor pour scanner en parallèle
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_port = {executor.submit(scan_port, domain, port): port for port in common_ports}
        
        for future in concurrent.futures.as_completed(future_to_port):
            result = future.result()
            if result:
                open_ports.append(result)
                print(f"{Fore.GREEN}[+] {result}{Style.RESET_ALL}")
    
    return open_ports if open_ports else ["Aucun port ouvert détecté"]

def check_forms(url):
    try:
        response = requests.get(url, verify=False, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        
        vulnerabilities = []
        for form in forms:
            # Vérifier les formulaires non sécurisés
            if form.get('action') and not form['action'].startswith('https'):
                vulnerabilities.append(f"Formulaire non sécurisé: {form.get('action')}")
            
            # Vérifier les inputs sensibles
            inputs = form.find_all('input')
            for inp in inputs:
                input_type = inp.get('type', '').lower()
                if input_type in ['password', 'text'] and not inp.get('autocomplete') == 'off':
                    vulnerabilities.append(f"Input sans autocomplete=off: {inp.get('name', 'unnamed')}")
        
        return vulnerabilities if vulnerabilities else ["Aucune vulnérabilité de formulaire détectée"]
    except Exception as e:
        return [f"Impossible d'analyser les formulaires: {str(e)}"]

def check_xss_vulnerabilities(url):
    """Vérifier les vulnérabilités XSS potentielles"""
    try:
        response = requests.get(url, verify=False, timeout=10)
        content = response.text.lower()
        
        vulnerabilities = []
        
        # Chercher des patterns XSS
        xss_patterns = [
            'alert(',
            'prompt(',
            'confirm(',
            'eval(',
            'document.cookie',
            'innerhtml',
            'outerhtml',
            'onload=',
            'onerror=',
            'onclick='
        ]
        
        for pattern in xss_patterns:
            if pattern in content:
                vulnerabilities.append(f"Pattern XSS détecté: {pattern}")
        
        return vulnerabilities
    except Exception as e:
        return [f"Impossible de vérifier les vulnérabilités XSS: {str(e)}"]

def check_sql_injection(url):
    """Vérifier les vulnérabilités SQL Injection potentielles"""
    try:
        # Chercher des paramètres dans l'URL
        if '?' in url:
            vulnerabilities = []
            params = url.split('?')[1].split('&')
            
            for param in params:
                if '=' in param:
                    param_name = param.split('=')[0]
                    vulnerabilities.append(f"Paramètre potentiellement vulnérable: {param_name}")
            
            return vulnerabilities
        return ["Aucun paramètre trouvé pour test SQL Injection"]
    except Exception as e:
        return [f"Impossible de vérifier les vulnérabilités SQL: {str(e)}"]

def check_directory_traversal(url):
    """Vérifier les vulnérabilités de directory traversal"""
    try:
        base_url = url.split('?')[0] if '?' in url else url
        
        # Test de directory traversal
        test_paths = [
            '../../../etc/passwd',
            '..\\..\\..\\windows\\system32\\drivers\\etc\\hosts',
            '....//....//....//etc/passwd'
        ]
        
        vulnerabilities = []
        for path in test_paths:
            test_url = f"{base_url}/{path}"
            try:
                response = requests.get(test_url, verify=False, timeout=5)
                if response.status_code == 200 and len(response.text) > 0:
                    vulnerabilities.append(f"Directory traversal possible: {path}")
            except:
                pass
        
        return vulnerabilities if vulnerabilities else ["Aucune vulnérabilité de directory traversal détectée"]
    except Exception as e:
        return [f"Impossible de vérifier les vulnérabilités directory traversal: {str(e)}"]

def check_open_redirect(url):
    """Vérifier les vulnérabilités d'open redirect"""
    try:
        response = requests.get(url, verify=False, timeout=10)
        content = response.text
        
        # Chercher des patterns d'open redirect
        redirect_patterns = [
            'redirect=',
            'url=',
            'next=',
            'target=',
            'redir=',
            'destination='
        ]
        
        vulnerabilities = []
        for pattern in redirect_patterns:
            if pattern in content:
                vulnerabilities.append(f"Open redirect possible: {pattern}")
        
        return vulnerabilities
    except Exception as e:
        return [f"Impossible de vérifier les open redirects: {str(e)}"]

def perform_whois(domain):
    try:
        w = whois.whois(domain)
        whois_info = []
        
        # Limiter à 50 résultats maximum
        count = 0
        max_results = 50
        
        if w.registrar and count < max_results:
            whois_info.append(f"Registrar: {w.registrar}")
            count += 1
        
        if w.creation_date and count < max_results:
            if isinstance(w.creation_date, list):
                whois_info.append(f"Date de création: {w.creation_date[0]}")
            else:
                whois_info.append(f"Date de création: {w.creation_date}")
            count += 1
        
        if w.expiration_date and count < max_results:
            if isinstance(w.expiration_date, list):
                whois_info.append(f"Date d'expiration: {w.expiration_date[0]}")
            else:
                whois_info.append(f"Date d'expiration: {w.expiration_date}")
            count += 1
        
        if w.updated_date and count < max_results:
            if isinstance(w.updated_date, list):
                whois_info.append(f"Dernière mise à jour: {w.updated_date[0]}")
            else:
                whois_info.append(f"Dernière mise à jour: {w.updated_date}")
            count += 1
        
        if w.name_servers and count < max_results:
            if isinstance(w.name_servers, list):
                # Limiter le nombre de serveurs affichés
                servers = w.name_servers[:5]  # Max 5 serveurs
                whois_info.append(f"Serveurs de noms: {', '.join(servers)}")
                if len(w.name_servers) > 5:
                    whois_info.append(f"... et {len(w.name_servers) - 5} autres serveurs")
            else:
                whois_info.append(f"Serveurs de noms: {w.name_servers}")
            count += 1
        
        if w.status and count < max_results:
            if isinstance(w.status, list):
                # Limiter le nombre de statuts affichés
                statuses = w.status[:5]  # Max 5 statuts
                whois_info.append(f"Statut: {', '.join(statuses)}")
                if len(w.status) > 5:
                    whois_info.append(f"... et {len(w.status) - 5} autres statuts")
            else:
                whois_info.append(f"Statut: {w.status}")
            count += 1
        
        if w.emails and count < max_results:
            if isinstance(w.emails, list):
                emails = w.emails[:3]  # Max 3 emails
                whois_info.append(f"Emails: {', '.join(emails)}")
                if len(w.emails) > 3:
                    whois_info.append(f"... et {len(w.emails) - 3} autres emails")
            else:
                whois_info.append(f"Email: {w.emails}")
            count += 1
        
        if w.org and count < max_results:
            whois_info.append(f"Organisation: {w.org}")
            count += 1
        
        if w.address and count < max_results:
            whois_info.append(f"Adresse: {w.address}")
            count += 1
        
        if count >= max_results:
            whois_info.append(f"... (limité à {max_results} résultats)")
        
        return whois_info if whois_info else ["Aucune information WHOIS disponible"]
    except Exception as e:
        return [f"Impossible d'obtenir les informations WHOIS: {str(e)}"]

def check_sensitive_files(domain):
    """Teste l'accès à des fichiers sensibles courants et les télécharge"""
    files = [
        '.env', '.git/config', 'config.php', 'config.json', 'backup.zip', 'db.sql', 'admin.php',
        'wp-config.php', 'composer.json', 'package.json', 'docker-compose.yml', 'id_rsa', 'id_rsa.pub',
        'phpinfo.php', 'test.php', 'debug.log', 'error.log', 'access.log', 'web.config', 'local.settings.json',
        '.htaccess', '.htpasswd', 'crossdomain.xml', 'sitemap.xml', 'robots.txt', 'backup.tar.gz', 'dump.rdb',
        'database.yml', 'settings.py', 'secrets.yml', 'private.key', 'ssl.key', 'ssl.crt', 'cert.pem',
        'server-status', 'server-info', 'cgi-bin/', 'admin/', 'login/', 'register/', 'signup/', 'install/',
        'setup/', 'old/', 'backup/', 'test/', 'dev/', 'staging/', 'tmp/', 'temp/', 'uploads/', 'files/',
        'data/', 'export/', 'import/', 'logs/', 'downloads/', 'public/', 'private/', 'conf/', 'config/',
        'api/', 'v1/', 'v2/', 'v3/', 'v4/', 'v5/'
    ]
    
    found = []
    downloaded = []
    
    # Créer le dossier pour les fichiers téléchargés
    download_dir = "downloaded_files"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    for f in files:
        url = f"https://{domain}/{f}" if not f.startswith('http') else f
        try:
            r = requests.get(url, verify=False, timeout=5)
            if r.status_code == 200 and len(r.text) > 0:
                found.append(f"Fichier sensible accessible: {f}")
                
                # Télécharger le fichier
                try:
                    # Nettoyer le nom du fichier pour éviter les problèmes de chemin
                    safe_filename = f.replace('/', '_').replace('\\', '_').replace(':', '_')
                    file_path = os.path.join(download_dir, f"{domain}_{safe_filename}")
                    
                    with open(file_path, 'wb') as file:
                        file.write(r.content)
                    
                    downloaded.append(f"✅ Téléchargé: {f} -> {file_path}")
                    print(f"{Fore.GREEN}[+] Téléchargé: {f}{Style.RESET_ALL}")
                    
                except Exception as e:
                    downloaded.append(f"❌ Erreur téléchargement {f}: {str(e)}")
                    
        except:
            continue
    
    results = found + downloaded
    return results if results else ["Aucun fichier sensible accessible détecté"]

def check_cookies(url):
    """Vérifie les cookies de sécurité"""
    try:
        r = requests.get(url, verify=False, timeout=10)
        cookies = r.cookies
        findings = []
        for cookie in cookies:
            if not cookie.secure:
                findings.append(f"Cookie non sécurisé: {cookie.name}")
            if not cookie.has_nonstandard_attr('HttpOnly'):
                findings.append(f"Cookie sans HttpOnly: {cookie.name}")
            if not cookie.has_nonstandard_attr('SameSite'):
                findings.append(f"Cookie sans SameSite: {cookie.name}")
        return findings if findings else ["Aucune vulnérabilité de cookie détectée"]
    except Exception as e:
        return [f"Impossible de vérifier les cookies: {str(e)}"]

def main():
    banner()
    url = input(f"{Fore.RED}[{Fore.WHITE}*{Fore.RED}]{Fore.WHITE} Entrez l'URL du site à analyser: ")
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    domain = url.split('/')[2]
    
    # Demander si l'utilisateur veut faire un WHOIS
    do_whois = input(f"{Fore.RED}[{Fore.WHITE}?{Fore.RED}]{Fore.WHITE} Voulez-vous faire un WHOIS? (o/n): ").lower().strip()
    
    print(f"\n{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} Analyse en cours...\n")
    
    results = []
    results.append("=== RAPPORT D'ANALYSE DE SÉCURITÉ ===")
    results.append(f"Site analysé: {url}")
    results.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # WHOIS optionnel
    if do_whois in ['o', 'oui', 'y', 'yes']:
        results.append("\n=== INFORMATIONS WHOIS ===")
        whois_info = perform_whois(domain)
        results.extend(whois_info)
    
    results.append("\n=== VULNÉRABILITÉS DES HEADERS ===")
    header_vulns = check_headers(url)
    results.extend(header_vulns)
    
    results.append("\n=== CERTIFICAT SSL ===")
    ssl_status = check_ssl(domain)
    results.append(ssl_status)
    
    results.append("\n=== PORTS OUVERTS ===")
    open_ports = scan_ports(domain)
    results.extend(open_ports)
    
    results.append("\n=== VULNÉRABILITÉS DES FORMULAIRES ===")
    form_vulns = check_forms(url)
    results.extend(form_vulns)
    
    results.append("\n=== VULNÉRABILITÉS XSS ===")
    xss_vulns = check_xss_vulnerabilities(url)
    results.extend(xss_vulns)
    
    results.append("\n=== VULNÉRABILITÉS SQL INJECTION ===")
    sql_vulns = check_sql_injection(url)
    results.extend(sql_vulns)
    
    results.append("\n=== VULNÉRABILITÉS DIRECTORY TRAVERSAL ===")
    dir_vulns = check_directory_traversal(url)
    results.extend(dir_vulns)
    
    results.append("\n=== VULNÉRABILITÉS OPEN REDIRECT ===")
    redirect_vulns = check_open_redirect(url)
    results.extend(redirect_vulns)
    
    results.append("\n=== FICHIERS SENSIBLES ===")
    sensitive_files = check_sensitive_files(domain)
    results.extend(sensitive_files)
    
    results.append("\n=== COOKIES ===")
    cookie_vulns = check_cookies(url)
    results.extend(cookie_vulns)
    
    results.append("\n=== RECOMMANDATIONS ===")
    results.append("1. Mettre à jour tous les composants du site")
    results.append("2. Implémenter HTTPS partout")
    results.append("3. Configurer correctement les headers de sécurité")
    results.append("4. Fermer les ports non nécessaires")
    results.append("5. Sécuriser tous les formulaires")
    results.append("6. Valider et assainir toutes les entrées utilisateur")
    results.append("7. Implémenter une WAF (Web Application Firewall)")
    results.append("8. Effectuer des tests de pénétration réguliers")
    
    # Afficher les résultats à l'écran
    print(f"\n{Fore.GREEN}=== RÉSULTATS DE L'ANALYSE ==={Style.RESET_ALL}")
    for result in results:
        print(f"{Fore.CYAN}{result}{Style.RESET_ALL}")
    
    # Sauvegarder le rapport
    with open('vulnerability_report.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(results))
    
    print(f"\n{Fore.RED}[{Fore.WHITE}✓{Fore.RED}]{Fore.WHITE} Analyse terminée!")
    print(f"{Fore.RED}[{Fore.WHITE}i{Fore.RED}]{Fore.WHITE} Rapport sauvegardé dans vulnerability_report.txt")

if __name__ == "__main__":
    main()
