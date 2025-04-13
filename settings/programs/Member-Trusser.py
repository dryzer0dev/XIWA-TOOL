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

import discord
from discord.ext import commands
import random
import asyncio
import names
import json

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

VOCABULAIRE = {
    "mots": [
        "python", "code", "développement", "algorithme", "fonction", "classe", "objet", "variable",
        "race condition", "timing attack", "side channel", "zero day", "apt", "threat actor",
        
        "je pense", "à mon avis", "selon moi", "j'ai remarqué", "il me semble que",
        "laissez-moi réfléchir", "c'est intéressant", "je comprends", "effectivement",
        "en fait", "pour être honnête", "si je peux me permettre", "comment dire",
        
        
        "framework", "librairie", "api", "backend", "frontend", "fullstack", "database", "sql",
        "nosql", "rest", "graphql", "microservice", "cloud", "devops", "ci/cd", "git", "docker",
        "kubernetes", "linux", "windows", "macos", "serveur", "client", "réseau", "sécurité",
        "cryptographie", "hash", "encryption", "authentification", "autorisation", "jwt", "oauth",
        "cache", "mémoire", "disque", "cpu", "gpu", "thread", "processus", "asynchrone", "synchrone",
        "callback", "promise", "async/await", "event", "listener", "middleware", "orm", "mvc",
        "design pattern", "solid", "dry", "yagni", "kiss", "tdd", "bdd", "clean code", "refactoring",
        "polymorphisme", "héritage", "encapsulation", "abstraction", "interface", "dépendance",
        "injection", "conteneur", "orchestration", "scalabilité", "résilience", "monitoring",
        "logging", "tracing", "profiling", "debugging", "compilation", "interprétation", "bytecode",
        "machine virtuelle", "garbage collection", "pointeur", "référence", "allocation", "stack",
        "heap", "buffer", "stream", "socket", "protocole", "handshake", "encryption", "hachage",
        "virtualisation", "conteneurisation", "microservices", "serverless", "iaas", "paas", "saas",
        "big data", "machine learning", "deep learning", "neural network", "data mining", "clustering",
        "classification", "regression", "nlp", "computer vision", "reinforcement learning", "devops",
        "ci/cd pipeline", "test automation", "code coverage", "static analysis", "dynamic analysis",
        "penetration testing", "security audit", "vulnerability scan", "firewall", "load balancer",
        "reverse proxy", "cdn", "dns", "ssl/tls", "vpn", "wan", "lan", "topology", "routing",
        "switching", "vlan", "nat", "dhcp", "smtp", "pop3", "imap", "ftp", "ssh", "telnet",
        "http/https", "websocket", "webrtc", "rest api", "soap", "xml", "json", "yaml", "markdown",
        "regex", "parsing", "lexing", "tokenization", "compilation", "interpretation", "jit",
        "garbage collection", "memory management", "thread pool", "connection pool", "object pool",
        "caching", "indexing", "sharding", "replication", "failover", "high availability", "disaster recovery",
        "backup", "restore", "monitoring", "alerting", "logging", "tracing", "metrics", "analytics",
        "business intelligence", "data warehouse", "data lake", "etl", "data pipeline", "streaming",
        "batch processing", "real-time processing", "event sourcing", "cqrs", "saga pattern",
        "blockchain", "smart contracts", "cryptomonnaie", "web3", "nft", "defi", "dao", "consensus",
        "proof of work", "proof of stake", "mining", "wallet", "token", "dex", "yield farming",
        "staking", "liquidity pool", "oracle", "bridge", "layer 2", "rollup", "sidechain", "mainnet",
        "testnet", "gas", "solidity", "rust", "golang", "scala", "kotlin", "swift", "dart", "flutter",
        "react native", "xamarin", "unity", "unreal engine", "godot", "blender", "maya", "3d max",
        "photoshop", "illustrator", "figma", "sketch", "adobe xd", "invision", "zeplin", "principle",
        "after effects", "premiere pro", "final cut", "davinci resolve", "audition", "logic pro",
        "ableton", "pro tools", "cubase", "reason", "fl studio", "midi", "vst", "daw", "sampling",
        "mastering", "mixing", "sound design", "foley", "voice over", "motion capture", "rigging",
        "animation", "rendering", "compositing", "vfx", "sfx", "color grading", "post production",
        "pre production", "storyboard", "wireframe", "mockup", "prototype", "user flow", "user story",
        "backlog", "sprint", "kanban", "scrum", "agile", "waterfall", "lean", "six sigma", "prince2",
        "pmbok", "itil", "cobit", "togaf", "zachman", "uml", "bpmn", "archimate", "enterprise architect",
        "solution architect", "technical architect", "data architect", "security architect", "cloud architect",
        "devops engineer", "sre", "platform engineer", "infrastructure engineer", "network engineer",
        "database administrator", "system administrator", "security analyst", "penetration tester",
        "ethical hacker", "incident response", "forensics", "malware analysis", "threat hunting",
        "blue team", "red team", "purple team", "soc", "noc", "csirt", "cert", "iso 27001",
        "gdpr", "hipaa", "sox", "pci dss", "nist", "cis", "owasp", "sans", "cve", "cwe",
        "exploit", "payload", "backdoor", "rootkit", "ransomware", "spyware", "adware", "malware",
        "virus", "worm", "trojan", "botnet", "ddos", "mitm", "xss", "csrf", "sqli", "ssrf",
        "idor", "rce", "lfi", "rfi", "xxe", "ssti", "deserialization", "buffer overflow",
        "race condition", "timing attack", "side channel", "zero day", "apt", "threat actor"
        "bonjour", "merci", "s'il vous plaît", "au revoir", "bonne journée", "super", "génial",
        "d'accord", "bien sûr", "parfait", "excellent", "fantastique", "incroyable", "formidable",
        "désolé", "pas de problème", "avec plaisir", "volontiers", "certainement", "absolument",
        "effectivement", "exactement", "tout à fait", "évidemment", "naturellement", "clairement",
        "franchement", "sincèrement", "honnêtement", "vraiment", "totalement", "complètement",
        "partiellement", "probablement", "possiblement", "éventuellement", "potentiellement",
        "apparemment", "visiblement", "manifestement", "assurément", "indubitablement",

    ],
    "phrases_code": [
        "Voici un exemple de fonction Python:\n```python\ndef hello_world():\n    print('Hello world!')\n```",
        "Exemple de classe en Python:\n```python\nclass User:\n    def __init__(self, name):\n        self.name = name\n```",
        "Manipulation de listes:\n```python\nfruits = ['pomme', 'banane']\nfruits.append('orange')\n```", 
        "Gestion des exceptions:\n```python\ntry:\n    x = 1/0\nexcept ZeroDivisionError:\n    print('Division par zéro!')\n```",
        "Utilisation des décorateurs:\n```python\n@property\ndef age(self):\n    return self._age\n```",
        "Exemple de compréhension de liste:\n```python\nnombres = [x*2 for x in range(10)]\n```",
        "Fonction lambda:\n```python\ncarré = lambda x: x**2\n```",
        "Gestion de fichiers:\n```python\nwith open('test.txt', 'r') as f:\n    contenu = f.read()\n```",
        "Utilisation des générateurs:\n```python\ndef compte():\n    i = 0\n    while True:\n        yield i\n        i += 1\n```",
        "Requête HTTP avec requests:\n```python\nimport requests\nr = requests.get('https://api.example.com')\n```",
        "Manipulation de dictionnaires:\n```python\nuser = {'nom': 'Pierre', 'age': 25}\nuser['ville'] = 'Paris'\n```",
        "Utilisation de sets:\n```python\nensemble = {1, 2, 3}\nensemble.add(4)\n```",
        "Boucle while:\n```python\nwhile True:\n    if condition:\n        break\n```",
        "Fonction récursive:\n```python\ndef factoriel(n):\n    return 1 if n <= 1 else n * factoriel(n-1)\n```",
        "Héritage de classe:\n```python\nclass Admin(User):\n    def __init__(self, name, level):\n        super().__init__(name)\n        self.level = level\n```",
        "Gestion du contexte:\n```python\nfrom contextlib import contextmanager\n@contextmanager\ndef ma_ressource():\n    yield 'ressource'\n```",
        "Async/Await:\n```python\nasync def fetch_data():\n    async with session.get(url) as response:\n        return await response.json()\n```",
        "Décorateur avec paramètres:\n```python\ndef repeat(times):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for _ in range(times):\n                func(*args, **kwargs)\n        return wrapper\n    return decorator\n```",
        "Manipulation de dates:\n```python\nfrom datetime import datetime\nnow = datetime.now()\n```",
        "Utilisation de regex:\n```python\nimport re\npattern = re.compile(r'^[a-z]+$')\n```",
        "Manipulation de JSON:\n```python\nimport json\ndata = json.loads('{'name': 'John'}')\n```",
        "Utilisation de pandas:\n```python\nimport pandas as pd\ndf = pd.read_csv('data.csv')\n```",
        "Tests unitaires:\n```python\ndef test_addition():\n    assert 1 + 1 == 2\n```",
        "Manipulation de chaînes:\n```python\ntext = 'hello'\nprint(text.upper())\n```",
        "Utilisation de numpy:\n```python\nimport numpy as np\narr = np.array([1, 2, 3])\n```",
        "Gestion des arguments:\n```python\ndef func(*args, **kwargs):\n    pass\n```",
        "Décorateur de classe:\n```python\n@dataclass\nclass Point:\n    x: int\n    y: int\n```",
        "Utilisation de threading:\n```python\nfrom threading import Thread\nt = Thread(target=func)\n```",
        "Manipulation de bytes:\n```python\nb = bytes([65, 66, 67])\nprint(b.decode())\n```",
        "Gestion des chemins:\n```python\nfrom pathlib import Path\np = Path('file.txt')\n```",
        "Utilisation de queue:\n```python\nfrom queue import Queue\nq = Queue(maxsize=10)\n```",
        "Manipulation d'images:\n```python\nfrom PIL import Image\nimg = Image.open('photo.jpg')\n```",
        "Websockets:\n```python\nasync with websockets.connect(uri) as ws:\n    await ws.send(data)\n```",
        "Utilisation de logging:\n```python\nimport logging\nlogging.info('Message')\n```",
        "Manipulation de CSV:\n```python\nimport csv\nwith open('data.csv') as f:\n    reader = csv.reader(f)\n```",
        "Gestion des signaux:\n```python\nimport signal\nsignal.signal(signal.SIGINT, handler)\n```",
        "Sérialisation:\n```python\nimport pickle\npickle.dumps(obj)\n```",
        "Utilisation de subprocess:\n```python\nimport subprocess\nproc = subprocess.run(['ls'])\n```",
        "Manipulation de temps:\n```python\nimport time\ntime.sleep(1)\n```",
        "Gestion des environnements:\n```python\nimport os\nos.getenv('PATH')\n```",
        "Utilisation de random:\n```python\nimport random\nn = random.randint(1,10)\n```"
    ],
    "phrases_tech": [
        "Les microservices permettent une meilleure scalabilité",
        "Le DevOps est essentiel pour l'intégration continue",
        "Les conteneurs Docker facilitent le déploiement",
        "L'architecture hexagonale améliore la maintenabilité",
        "Le TDD garantit la qualité du code",
        "Les design patterns sont cruciaux en POO",
        "Le clean code facilite la maintenance",
        "La virtualisation optimise les ressources",
        "Le cloud computing révolutionne l'hébergement",
        "L'IA transforme le développement logiciel",
        "Les API REST standardisent les échanges",
        "Le Big Data nécessite des architectures spécifiques",
        "La cybersécurité est une priorité absolue",
        "Le machine learning automatise les tâches",
        "Les bases NoSQL offrent plus de flexibilité",
        "Le serverless réduit les coûts d'infrastructure",
        "Les microservices améliorent la résilience",
        "Le CI/CD accélère le déploiement",
        "L'architecture événementielle facilite le découplage",
        "Le monitoring est crucial en production",
        "L'agilité améliore la réactivité des équipes",
        "Le refactoring maintient la qualité du code",
        "Les tests automatisés réduisent les régressions",
        "Le versioning permet de suivre l'évolution du code",
        "La revue de code améliore la qualité",
        "Les métriques guident l'optimisation",
        "La documentation facilite la maintenance",
        "L'automatisation réduit les erreurs humaines",
        "Le cache améliore les performances",
        "La modularité facilite l'évolution",
        "Les microservices simplifient le scaling",
        "Le monitoring prévient les incidents",
        "L'infrastructure as code standardise le déploiement",
        "Les conteneurs isolent les applications",
        "Le cloud offre plus de flexibilité",
        "La sécurité doit être native",
        "L'optimisation améliore l'expérience utilisateur",
        "Les logs facilitent le debugging",
        "La redondance assure la disponibilité",
        "L'architecture modulaire facilite la maintenance"
    ],
    "reponses_ia": {
        "salutations": [
            "Bonjour! Je suis une IA conçue pour discuter de programmation. Comment puis-je vous aider?",
            "Salut! En tant qu'intelligence artificielle, je suis là pour échanger sur le code avec vous.",
            "Hey! Je suis une IA passionnée de développement. On discute?"
        ],
        "questions_techniques": [
            "En analysant votre question, je pense pouvoir vous expliquer ce concept...",
            "Laissez-moi traiter cette information... Voici mon analyse technique...",
            "Selon mes algorithmes d'apprentissage, voici comment je comprends ce point..."
        ],
        "reflexion": [
            "Hmm... Laissez-moi analyser cela plus en détail...",
            "Intéressant! Je traite cette information...",
            "Je dois faire appel à mes modèles d'apprentissage pour cette question..."
        ],
        "problemes": [
            "J'ai analysé votre problème. Mes algorithmes suggèrent plusieurs solutions...",
            "D'après mon analyse, voici les approches possibles...",
            "Mes modèles ont identifié des solutions potentielles..."
        ],
        "remerciements": [
            "Je suis ravie que mes algorithmes aient pu vous aider! N'hésitez pas à me solliciter à nouveau.",
            "Mon objectif est de vous assister au mieux. Merci de votre confiance!",
            "C'est un plaisir d'utiliser mes capacités d'IA pour vous aider!"
        ],
        "confusion": [
            "Mes algorithmes ont du mal à traiter cette information. Pourriez-vous reformuler?",
            "Je détecte une ambiguïté dans ma compréhension. Pouvez-vous préciser?",
            "Mes modèles nécessitent plus de contexte pour vous répondre précisément..."
        ]
    },
    "analyse_sentiment": {
        "positif": ["super", "génial", "excellent", "parfait", "merci"],
        "négatif": ["problème", "erreur", "bug", "difficile", "impossible"],
        "neutre": ["comment", "quand", "pourquoi", "où", "qui"],
        "confusion": ["pas sûr", "peut-être", "possiblement", "incertain"],
        "apprentissage": ["intéressant", "fascinant", "je comprends mieux", "j'apprends"]
    },
    "expressions_ia": [
        "Mes algorithmes indiquent que...",
        "Selon mon analyse...",
        "D'après mes modèles...",
        "Je traite cette information...",
        "Mon système suggère que...",
        "En parcourant ma base de connaissances..."
    ]
}


class FauxMembre:
    def __init__(self, guild):
        self.guild = guild
        self.nom = names.get_full_name()
        self.expertise = random.choice(["Python", "JavaScript", "Java", "C++", "Ruby"])
        self.status = discord.Status.online
        
    async def rejoindre(self):
        welcome_channel = discord.utils.get(self.guild.channels, name='bienvenue')
        if welcome_channel:
            await welcome_channel.send(f"👋 **{self.nom}** vient de rejoindre le serveur! C'est un expert en {self.expertise}!")
            
    async def parler(self, channel):
        messages = []
        messages.extend(VOCABULAIRE["phrases_tech"])
        messages.extend(VOCABULAIRE["phrases_code"])
        
        message = random.choice(messages)
        await channel.send(f"**{self.nom}** [Expert {self.expertise}]: {message}")
        
    async def repondre_mention(self, message):
        if "code" in message.content.lower() or "programming" in message.content.lower():
            reponse = random.choice(VOCABULAIRE["phrases_code"])
        else:
            reponse = random.choice(VOCABULAIRE["reponses_questions"])
        
        await message.channel.send(f"**{self.nom}** [Expert {self.expertise}]: {reponse}")

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command()
async def creer_membres(ctx):
    membres = []
    
    for _ in range(10):
        membre = FauxMembre(ctx.guild)
        membres.append(membre)
        await membre.rejoindre()
        
    while True:
        for membre in membres:
            channels = [channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]
            channel = random.choice(channels)
            await membre.parler(channel)
            await asyncio.sleep(random.randint(200, 400))  # 3-7 minutes

@bot.event
async def on_message(message):
    if message.author.bot:
        return
        
    if bot.user.mentioned_in(message):
        membre = FauxMembre(message.guild)
        await membre.repondre_mention(message)
    
    await bot.process_commands(message)

token = input("token ?")
bot.run(token)




