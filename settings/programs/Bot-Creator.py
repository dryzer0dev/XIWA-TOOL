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
import json
import keyboard
from colorama import Fore, Style
import time
import discord
from discord.ext import commands
import aiohttp
import asyncio
import socket
import whois
import nmap
import requests
from bs4 import BeautifulSoup
import re
import hashlib
import random
import string

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

def generate_hacking_command(feature):
    commands = {
        "port_scanner": """
@bot.command()
async def portscan(ctx  , target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                results.append(f'Port {port}/{proto}: {state} ({service})')
    await ctx.send('\\n'.join(results))""",

        "vuln_scanner": """
@bot.command()
async def vulnscan(ctx, url):
    headers = requests.head(url).headers
    vulns = []
    if 'X-Frame-Options' not in headers:
        vulns.append('Clickjacking possible')
    if 'X-XSS-Protection' not in headers:
        vulns.append('XSS protection non activée')
    if 'Content-Security-Policy' not in headers:
        vulns.append('CSP non configuré')
    await ctx.send('Vulnérabilités trouvées:\\n' + '\\n'.join(vulns))""",

        "network_mapper": """
@bot.command()
async def netmap(ctx, subnet):
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-sn')
    hosts = [host for host in nm.all_hosts()]
    await ctx.send(f'Hôtes actifs:\\n' + '\\n'.join(hosts))""",

        "subdomain_enum": """
@bot.command() 
async def subdomains(ctx, domain):
    subdomains = []
    with open('wordlist.txt') as f:
        wordlist = f.read().splitlines()
    for sub in wordlist:
        try:
            host = f'{sub}.{domain}'
            socket.gethostbyname(host)
            subdomains.append(host)
        except:
            pass
    await ctx.send('Sous-domaines trouvés:\\n' + '\\n'.join(subdomains))""",

        "dns_lookup": """
@bot.command()
async def dnslookup(ctx, domain):
    records = {}
    for qtype in ['A', 'AAAA', 'MX', 'NS', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, qtype)
            records[qtype] = [str(rdata) for rdata in answers]
        except:
            records[qtype] = []
    await ctx.send('\\n'.join(f'{k}: {v}' for k,v in records.items()))""",

        "whois_lookup": """
@bot.command()
async def whoislookup(ctx, domain):
    w = whois.whois(domain)
    info = [
        f'Registrar: {w.registrar}',
        f'Creation: {w.creation_date}',
        f'Expiration: {w.expiration_date}',
        f'Name Servers: {w.name_servers}'
    ]
    await ctx.send('\\n'.join(info))""",

        "ssl_checker": """
@bot.command()
async def sslcheck(ctx, domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            info = [
                f'Issuer: {cert["issuer"]}',
                f'Subject: {cert["subject"]}',
                f'Expiry: {cert["notAfter"]}'
            ]
    await ctx.send('\\n'.join(info))""",

        "header_scanner": """
@bot.command()
async def headers(ctx, url):
    headers = requests.head(url).headers
    await ctx.send('\\n'.join(f'{k}: {v}' for k,v in headers.items()))""",

        "directory_scanner": """
@bot.command()
async def dirscan(ctx, url):
    with open('dirlist.txt') as f:
        dirs = f.read().splitlines()
    found = []
    for d in dirs:
        r = requests.get(f'{url}/{d}')
        if r.status_code == 200:
            found.append(d)
    await ctx.send('Répertoires trouvés:\\n' + '\\n'.join(found))""",

        "xss_scanner": """
@bot.command()
async def xssscan(ctx, url):
    payloads = ['<script>alert(1)</script>', '\"><script>alert(1)</script>']
    vulns = []
    for p in payloads:
        r = requests.get(url + p)
        if p in r.text:
            vulns.append(f'XSS possible avec: {p}')
    await ctx.send('\\n'.join(vulns))""",

        "sqli_scanner": """
@bot.command()
async def sqliscan(ctx, url):
    payloads = ["'", "1' OR '1'='1", "1; DROP TABLE users"]
    vulns = []
    for p in payloads:
        r = requests.get(url + p)
        if 'SQL' in r.text:
            vulns.append(f'SQLi possible avec: {p}')
    await ctx.send('\\n'.join(vulns))""",

        "cms_detector": """
@bot.command()
async def cmsdetect(ctx, url):
    r = requests.get(url)
    cms = []
    if 'wp-content' in r.text:
        cms.append('WordPress')
    if 'drupal' in r.text:
        cms.append('Drupal')
    if 'joomla' in r.text:
        cms.append('Joomla')
    await ctx.send('CMS détectés:\\n' + '\\n'.join(cms))""",

        "tech_detector": """
@bot.command()
async def techdetect(ctx, url):
    r = requests.get(url)
    techs = []
    if 'PHP' in r.headers.get('X-Powered-By', ''):
        techs.append('PHP')
    if 'ASP.NET' in r.headers.get('X-AspNet-Version', ''):
        techs.append('ASP.NET')
    await ctx.send('Technologies détectées:\\n' + '\\n'.join(techs))""",

        "email_harvester": """
@bot.command()
async def harvest(ctx, url):
    r = requests.get(url)
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', r.text)
    await ctx.send('Emails trouvés:\\n' + '\\n'.join(set(emails)))""",

        "metadata_extractor": """
@bot.command()
async def metadata(ctx, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    meta = soup.find_all('meta')
    data = [f'{m.get("name", m.get("property", "unknown"))}: {m.get("content", "")}' for m in meta]
    await ctx.send('Métadonnées:\\n' + '\\n'.join(data))""",

        "hash_cracker": """
@bot.command()
async def crack(ctx, hash_value):
    with open('wordlist.txt') as f:
        words = f.read().splitlines()
    for word in words:
        if hashlib.md5(word.encode()).hexdigest() == hash_value:
            await ctx.send(f'Hash craqué! Mot de passe: {word}')
            return
    await ctx.send('Hash non craqué')""",

        "password_generator": """
@bot.command()
async def genpass(ctx, length: int):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    await ctx.send(f'Mot de passe généré: {password}')""",

        "cipher_decoder": """
@bot.command()
async def decode(ctx, text):
    rot13 = text.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    ))
    await ctx.send(f'ROT13: {rot13}')""",

        "reverse_ip": """
@bot.command()
async def reverseip(ctx, ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        await ctx.send(f'Hostname: {hostname}')
    except:
        await ctx.send('Impossible de résoudre l\'IP')""",

        "honeypot_detector": """
@bot.command()
async def honeypot(ctx, ip):
    ports = [21, 22, 23, 25, 80]
    suspicious = 0
    for port in ports:
        try:
            socket.create_connection((ip, port), timeout=1)
            suspicious += 1
        except:
            pass
    await ctx.send(f'Score de suspicion: {suspicious}/5')"""
    }
    
    return commands.get(feature, "")

def generate_server_command(feature):
    commands = {
        "welcome_message": """
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(config['custom_settings']['welcome_message']['channel_id'])
    await channel.send(f'Bienvenue {member.mention} sur le serveur!')""",

        "goodbye_message": """
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(config['custom_settings']['goodbye_message']['channel_id'])
    await channel.send(f'Au revoir {member.name}!')""",

        "autorole": """
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=config['custom_settings']['autorole']['role_id'])
    await member.add_roles(role)""",

        "verification": """
@bot.command()
async def verify(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Vérifié')
    await ctx.author.add_roles(role)
    await ctx.send('Vous êtes maintenant vérifié!')""",

        "moderation": """
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} a été banni.')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} a été expulsé.')

@bot.command()
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f'{member} a été muté.')""",

        "antiraid": """
@bot.event
async def on_member_join(member):
    joins = getattr(bot, 'joins', [])
    now = time.time()
    joins = [j for j in joins if now - j < 10]
    joins.append(now)
    bot.joins = joins
    if len(joins) > 5:
        await member.guild.edit(verification_level=discord.VerificationLevel.high)""",

        "anti_spam": """
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    msgs = getattr(bot, 'msgs', [])
    now = time.time()
    msgs = [m for m in msgs if now - m < 5]
    msgs.append(now)
    bot.msgs = msgs
    if len(msgs) > 5:
        await message.delete()""",

        "anti_link": """
@bot.event
async def on_message(message):
    if 'http' in message.content:
        await message.delete()
        await message.channel.send(f'{message.author.mention} liens non autorisés!')""",

        "ticket_system": """
@bot.command()
async def ticket(ctx):
    channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.name}')
    await channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
    await channel.send(f'{ctx.author.mention} voici votre ticket.')""",

        "level_system": """
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    xp = bot.levels.get(str(message.author.id), 0) + random.randint(15, 25)
    level = int(xp ** (1/4))
    bot.levels[str(message.author.id)] = xp
    if level > int((bot.levels.get(str(message.author.id), 0) - random.randint(15, 25)) ** (1/4)):
        await message.channel.send(f'{message.author.mention} niveau {level} atteint!')""",

        "reaction_roles": """
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == config['custom_settings']['reaction_roles']['message_id']:
        guild = bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name=str(payload.emoji))
        await payload.member.add_roles(role)""",

        "giveaway": """
@bot.command()
async def giveaway(ctx, time: int, *, prize):
    embed = discord.Embed(title='🎉 GIVEAWAY 🎉', description=prize)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🎉')
    await asyncio.sleep(time)
    msg = await ctx.channel.fetch_message(msg.id)
    users = [user async for user in msg.reactions[0].users()]
    winner = random.choice(users)
    await ctx.send(f'Bravo {winner.mention}! Tu as gagné {prize}!')""",

        "poll_creator": """
@bot.command()
async def poll(ctx, question, *options):
    embed = discord.Embed(title=question)
    for i, opt in enumerate(options):
        embed.add_field(name=f'Option {i+1}', value=opt)
    msg = await ctx.send(embed=embed)
    for i in range(len(options)):
        await msg.add_reaction(f'{i+1}️⃣')""",

        "custom_commands": """
@bot.command()
async def addcmd(ctx, name, *, response):
    bot.custom_commands[name] = response
    await ctx.send(f'Commande {name} ajoutée!')

@bot.event
async def on_message(message):
    if message.content.startswith(config['prefix']):
        cmd = message.content[1:].split()[0]
        if cmd in bot.custom_commands:
            await message.channel.send(bot.custom_commands[cmd])""",

        "auto_moderation": """
@bot.event
async def on_message(message):
    if any(word in message.content.lower() for word in ['badword1', 'badword2']):
        await message.delete()
        await message.channel.send(f'{message.author.mention} langage inapproprié!')""",

        "logging": """
@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(config['custom_settings']['logging']['channel_id'])
    embed = discord.Embed(title='Message Supprimé', description=message.content)
    embed.set_author(name=message.author.name)
    await channel.send(embed=embed)""",

        "music_player": """
@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    player = await YTDLSource.from_url(url, loop=bot.loop)
    vc.play(player)""",

        "twitch_alerts": """
@tasks.loop(minutes=5.0)
async def check_twitch():
    for streamer in config['custom_settings']['twitch_alerts']['streamers']:
        status = await get_stream_status(streamer)
        if status['is_live'] and streamer not in bot.live_streamers:
            channel = bot.get_channel(config['custom_settings']['twitch_alerts']['channel_id'])
            await channel.send(f'{streamer} est en live! {status["title"]}')
            bot.live_streamers.append(streamer)""",

        "youtube_alerts": """
@tasks.loop(minutes=15.0)
async def check_youtube():
    for channel in config['custom_settings']['youtube_alerts']['channels']:
        videos = await get_latest_videos(channel)
        for video in videos:
            if video['id'] not in bot.posted_videos:
                alert_channel = bot.get_channel(config['custom_settings']['youtube_alerts']['channel_id'])
                await alert_channel.send(f'Nouvelle vidéo de {channel}: {video["title"]}')
                bot.posted_videos.append(video['id'])""",

        "twitter_alerts": """
@tasks.loop(minutes=5.0)
async def check_twitter():
    for account in config['custom_settings']['twitter_alerts']['accounts']:
        tweets = await get_latest_tweets(account)
        for tweet in tweets:
            if tweet['id'] not in bot.posted_tweets:
                channel = bot.get_channel(config['custom_settings']['twitter_alerts']['channel_id'])
                await channel.send(f'Nouveau tweet de {account}: {tweet["text"]}')
                bot.posted_tweets.append(tweet['id'])"""
    }
    
    return commands.get(feature, "")

def generate_osint_command(feature):
    commands = {
        "email_lookup": """
@bot.command()
async def emaillookup(ctx, email):
    results = []
    domains = ['linkedin.com', 'facebook.com', 'twitter.com']
    for domain in domains:
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            results.append(f'Trouvé sur {domain}')
        except:
            pass
    await ctx.send('\\n'.join(results))""",

        "phone_lookup": """
@bot.command()
async def phonelookup(ctx, number):
    info = phonenumbers.parse(number)
    results = [
        f'Pays: {geocoder.description_for_number(info, "fr")}',
        f'Opérateur: {carrier.name_for_number(info, "fr")}',
        f'Fuseau horaire: {timezone.time_zones_for_number(info)}'
    ]
    await ctx.send('\\n'.join(results))""",

        "username_search": """
@bot.command()
async def usersearch(ctx, username):
    sites = ['github.com', 'twitter.com', 'instagram.com']
    results = []
    for site in sites:
        r = requests.get(f'https://{site}/{username}')
        if r.status_code == 200:
            results.append(f'Trouvé sur {site}')
    await ctx.send('\\n'.join(results))""",

        "domain_recon": """
@bot.command()
async def domainrecon(ctx, domain):
    info = []
    w = whois.whois(domain)
    info.extend([
        f'Registrar: {w.registrar}',
        f'Creation: {w.creation_date}',
        f'Emails: {w.emails}',
        f'DNS: {w.name_servers}'
    ])
    await ctx.send('\\n'.join(info))""",

        "social_search": """
@bot.command()
async def socialsearch(ctx, query):
    platforms = ['facebook', 'twitter', 'linkedin', 'instagram']
    results = []
    for platform in platforms:
        r = requests.get(f'https://www.google.com/search?q=site:{platform}.com+{query}')
        if 'No results found' not in r.text:
            results.append(f'Résultats trouvés sur {platform}')
    await ctx.send('\\n'.join(results))""",

        "image_search": """
@bot.command()
async def imagesearch(ctx, url):
    results = []
    r = requests.get(f'https://www.google.com/searchbyimage?image_url={url}')
    soup = BeautifulSoup(r.text, 'html.parser')
    for g in soup.find_all('div', class_='g'):
        results.append(g.text[:100])
    await ctx.send('\\n'.join(results[:5]))""",

        "news_search": """
@bot.command()
async def newssearch(ctx, query):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://newsapi.org/v2/everything?q={query}') as r:
            data = await r.json()
            articles = data['articles'][:5]
            results = [f'{a["title"]} - {a["url"]}' for a in articles]
            await ctx.send('\\n'.join(results))""",

        "company_lookup": """
@bot.command()
async def companylookup(ctx, company):
    results = []
    r = requests.get(f'https://api.opencorporates.com/v0.4/companies/search?q={company}')
    data = r.json()
    for company in data['results']['companies'][:5]:
        results.append(f'{company["name"]} - {company["jurisdiction_code"]}')
    await ctx.send('\\n'.join(results))""",

        "ip_lookup": """
@bot.command()
async def iplookup(ctx, ip):
    r = requests.get(f'http://ip-api.com/json/{ip}')
    data = r.json()
    info = [
        f'Pays: {data["country"]}',
        f'Région: {data["regionName"]}',
        f'Ville: {data["city"]}',
        f'ISP: {data["isp"]}'
    ]
    await ctx.send('\\n'.join(info))""",

        "breach_check": """
@bot.command()
async def breachcheck(ctx, email):
    r = requests.get(f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}')
    if r.status_code == 200:
        breaches = r.json()
        results = [b['Name'] for b in breaches]
        await ctx.send('Fuites trouvées:\\n' + '\\n'.join(results))
    else:
        await ctx.send('Aucune fuite trouvée')""",

        "crypto_tracker": """
@bot.command()
async def cryptotrack(ctx, address):
    r = requests.get(f'https://api.blockchair.com/bitcoin/dashboards/address/{address}')
    data = r.json()['data'][address]
    info = [
        f'Balance: {data["address"]["balance"]}',
        f'Transactions: {data["address"]["transaction_count"]}',
        f'Reçu total: {data["address"]["received"]}',
        f'Envoyé total: {data["address"]["spent"]}'
    ]
    await ctx.send('\\n'.join(info))""",

        "location_search": """
@bot.command()
async def locsearch(ctx, query):
    r = requests.get(f'https://nominatim.openstreetmap.org/search?q={query}&format=json')
    locations = r.json()[:5]
    results = [f'{l["display_name"]} ({l["lat"]}, {l["lon"]})' for l in locations]
    await ctx.send('\\n'.join(results))""",

        "document_search": """
@bot.command()
async def docsearch(ctx, query):
    r = requests.get(f'https://www.google.com/search?q=filetype:pdf+{query}')
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    for div in soup.find_all('div', class_='g')[:5]:
        results.append(div.find('a')['href'])
    await ctx.send('\\n'.join(results))""",

        "people_search": """
@bot.command()
async def peoplesearch(ctx, name):
    sites = ['linkedin.com', 'facebook.com', 'twitter.com']
    results = []
    for site in sites:
        r = requests.get(f'https://www.google.com/search?q=site:{site}+{name}')
        if 'No results found' not in r.text:
            results.append(f'Profils trouvés sur {site}')
    await ctx.send('\\n'.join(results))""",

        "vehicle_lookup": """
@bot.command()
async def vehiclelookup(ctx, plate):
    # Simulation - dans la réalité nécessiterait une API spécifique
    info = [
        'Marque: SIMULATED',
        'Modèle: SIMULATED',
        'Année: SIMULATED',
        'Statut: SIMULATED'
    ]
    await ctx.send('\\n'.join(info))""",

        "darkweb_search": """
@bot.command()
async def darkwebsearch(ctx, query):
    results = [
        'SIMULATION - Résultat 1',
        'SIMULATION - Résultat 2',
        'SIMULATION - Résultat 3',
        'DIT REZZER! Je suis desole, mais la tu es oblige de faire une connexion a tor ! stv je te le fait ! contacte moi'
    ]
    await ctx.send('\\n'.join(results))""",

        "paste_search": """
@bot.command()
async def pastesearch(ctx, query):
    r = requests.get(f'https://psbdmp.ws/api/search/{query}')
    pastes = r.json()[:5]
    results = [f'ID: {p["id"]} - Date: {p["date"]}' for p in pastes]
    await ctx.send('\\n'.join(results))""",

        "github_recon": """
@bot.command()
async def githubrecon(ctx, user):
    r = requests.get(f'https://api.github.com/users/{user}')
    data = r.json()
    info = [
        f'Repos: {data["public_repos"]}',
        f'Gists: {data["public_gists"]}',
        f'Followers: {data["followers"]}',
        f'Créé le: {data["created_at"]}'
    ]
    await ctx.send('\\n'.join(info))""",

        "shodan_search": """
@bot.command()
async def shodansearch(ctx, query):
    api = Shodan(config['shodan_api_key'])
    results = api.search(query)
    hosts = []
    for result in results['matches'][:5]:
        hosts.append(f'{result["ip_str"]}:{result["port"]} - {result["org"]}')
    await ctx.send('\\n'.join(hosts))""",

        "blockchain_explorer": """
@bot.command()
async def blockchainexplorer(ctx, address):
    r = requests.get(f'https://blockchain.info/rawaddr/{address}')
    data = r.json()
    info = [
        f'Balance: {data["final_balance"]}',
        f'Transactions: {data["n_tx"]}',
        f'Total reçu: {data["total_received"]}',
        f'Total envoyé: {data["total_sent"]}'
    ]
    await ctx.send('\\n'.join(info))"""
    }
    
    return commands.get(feature, "")

def banner():
    print(f"""{red}
╔═══════════════════════════════════════╗
║        Discord Bot Creator Pro        ║
║      Créateur de Bot Discord Pro     ║
╚═══════════════════════════════════════╝{reset}
""")

def get_choice(prompt, timeout=0.1):
    print(f"{red}[{white}?{red}]{white} {prompt} (y/n): ", end='', flush=True)
    start = time.time()
    while time.time() - start < timeout:
        if keyboard.is_pressed('y'):
            print("y")
            return True
        if keyboard.is_pressed('n'):
            print("n") 
            return False
    return False

def create_bot():
    banner()
    
    config = {
        "bot_name": input(f"{red}[{white}>{red}]{white} Nom du bot: "),
        "prefix": input(f"{red}[{white}>{red}]{white} Préfixe des commandes: "),
        "features": {},
        "custom_settings": {}
    }

    print(f"\n{red}[{white}*{red}]{white} Type de Bot:")
    print(f"{red}[{white}1{red}]{white} Bot de Hacking")
    print(f"{red}[{white}2{red}]{white} Bot de Serveur")
    print(f"{red}[{white}3{red}]{white} Bot d'OSINT")
    
    bot_type = input(f"\n{red}[{white}>{red}]{white} Choix: ")
    
    type_map = {"1": "hacking", "2": "server", "3": "osint"}
    selected_type = type_map[bot_type]