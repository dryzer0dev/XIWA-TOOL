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

import socket
import threading
import nmap
import netifaces
import scapy.all as scapy
import time
import json
import os
from colorama import Fore, Style, init

init()

RED = Fore.RED
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear()
    print(f"""{RED}
    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                        {WHITE}Scanner{RESET}
    """)

def scan_port(target, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        service = "Unknown"
        try:
            service = socket.getservbyport(port)
        except:
            pass
        open_ports.append((port, service))
    sock.close()

def port_scan(target, start_port=1, end_port=1024):
    print(f"\n{RED}[{WHITE}+{RED}]{WHITE} Scanning ports for {target}...")
    open_ports = []
    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    return sorted(open_ports)

def network_scan(target_ip):
    arp_request = scapy.ARP(pdst=target_ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    devices_list = []
    for element in answered_list:
        device_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        try:
            hostname = socket.gethostbyaddr(element[1].psrc)[0]
            device_dict["hostname"] = hostname
        except:
            device_dict["hostname"] = "Unknown"
        devices_list.append(device_dict)
    
    return devices_list

def os_detection(target):
    nm = nmap.PortScanner()
    try:
        scan = nm.scan(target, arguments="-O")
        if "osmatch" in scan["scan"][target]:
            return scan["scan"][target]["osmatch"][0]["name"]
    except:
        pass
    return "Unknown"

def vulnerability_scan(target):
    nm = nmap.PortScanner()
    try:
        scan = nm.scan(target, arguments="--script vuln")
        return scan
    except:
        return None

def main():
    while True:
        print_banner()
        
        target = input(f"\n{RED}[{WHITE}>{RED}]{WHITE} Entrez l'adresse IP ou le réseau à scanner (ex: 192.168.1.0/24): ")
        
        print(f"\n{RED}[{WHITE}*{RED}]{WHITE} Scanning réseau: {target}\n")
        
        devices = network_scan(target)
        
        print(f"\n{RED}[{WHITE}+{RED}]{WHITE} {len(devices)} appareils trouvés:")
        for device in devices:
            print(f"\n{RED}[{WHITE}*{RED}]{WHITE} IP: {device['ip']}")
            print(f"{RED}[{WHITE}*{RED}]{WHITE} MAC: {device['mac']}")
            print(f"{RED}[{WHITE}*{RED}]{WHITE} Hostname: {device['hostname']}")
            
            os = os_detection(device['ip'])
            print(f"{RED}[{WHITE}*{RED}]{WHITE} OS: {os}")
            
            open_ports = port_scan(device['ip'])
            if open_ports:
                print(f"{RED}[{WHITE}*{RED}]{WHITE} Ports ouverts:")
                for port, service in open_ports:
                    print(f"  {RED}[{WHITE}+{RED}]{WHITE} {port}/tcp - {service}")
        
        choice = input(f"\n{RED}[{WHITE}>{RED}]{WHITE} Scanner un autre réseau? (o/n): ").lower()
        if choice != 'o':
            break

if __name__ == "__main__":
    main()