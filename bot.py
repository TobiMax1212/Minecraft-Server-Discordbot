import discord
import json
from discord.ext import commands
from discord import Embed
import socket
import random
from mcstatus import JavaServer
import os

#THIS IS TEST
print("Bot wird gestartet...")

# Pfad zu 'app.json' anpassen
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'app.json')

with open(json_path, 'r') as file:
    data = json.load(file)

# Discord-Bot Variabeln
ms_url = data['ms_url']
ms_port = data['ms_port']
token = data['token']
ms_status_color_on = 0x00FF00
ms_status_color_off = 0xFF0000
IP = socket.gethostbyname(ms_url)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Function to check if the server port is open and get player count
def check_port(ip, port):
    try:
        server = JavaServer.lookup(f"{ip}:{port}")
        status = server.status()
        player_count = status.players.online
        return Embed(title="Server ist online",
                     description=f"IPv4: {ip}\nPort: {port}\nOnline: {player_count}",
                     color=ms_status_color_on)
    except Exception as e:
        return Embed(title="Server ist offline! \nIn der Zwischenzeit kannst du den Befehl '!spiel' testen.",
                     color=ms_status_color_off)

@bot.event
async def on_ready():
    print("Bot ist ready!")

@bot.command(name='spiel')
async def schere_stein_papier(ctx, auswahl: str = None):
    if auswahl is None:
        await ctx.send("Bitte wÃ¤hle zwischen Schere, Stein oder Papier.")
        return

    auswahl = auswahl.lower()
    bot_auswahl = random.choice(['schere', 'stein', 'papier'])

    if auswahl in ['schere', 'stein', 'papier']:
        if auswahl == bot_auswahl:
            await ctx.send(f"Unentschieden! Ich habe auch {bot_auswahl}.")
        elif (auswahl == 'schere' and bot_auswahl == 'papier') or \
             (auswahl == 'stein' and bot_auswahl == 'schere') or \
             (auswahl == 'papier' and bot_auswahl == 'stein'):
            await ctx.send(f"Gewonnen! Ich hatte {bot_auswahl}.")
        else:
            await ctx.send(f"Verloren! Ich hatte {bot_auswahl}.")
    else:
        await ctx.send("Bitte wÃ¤hle zwischen Schere, Stein oder Papier.")

@bot.command(name='status')
async def serverinfo(ctx):
    answer = check_port(IP, ms_port)
    await ctx.send(embed=answer)

bot.run(token)
