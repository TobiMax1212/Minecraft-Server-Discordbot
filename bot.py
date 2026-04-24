import discord
import json
from discord.ext import commands
from discord import Embed
import socket
import random
from mcstatus import JavaServer
import os

# Path to app.json
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'app.json')

with open(json_path, 'r') as file:
    data = json.load(file)

# Discord-Bot variables

token = os.getenv('DISCORD_TOKEN') # --> Get Discord Token from .env file --> DO NOT SAVE TOKEN IN CODE OR JSON FILE!

ms_url = data['ms_url']
ms_port = data['ms_port']
ms_status_color_on = 0x00FF00
ms_status_color_off = 0xFF0000
IP = socket.gethostbyname(ms_url)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Check if the token is set in .env file
def check_token(token):
    if token is None or token == "":
        print("Error: DISCORD_TOKEN is not set. Please set the token in the .env file.")
    else:
        print("Token is set. Starting the bot...")
check_token(token)


# Function to check if the server port is open and get player count
def check_port(ip, port):
    try:
        server = JavaServer.lookup(f"{ip}:{port}")
        status = server.status()
        player_count = status.players.online
        return Embed(title="Server is online",
                     description=f"IPv4: {ip}\nPort: {port}\nOnline: {player_count}",
                     color=ms_status_color_on)
    except Exception as e:
        return Embed(title="Server is offline! \nIn the meantime you can test the command '!game'.",
                     color=ms_status_color_off)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command(name='game')
async def schere_stein_papier(ctx, auswahl: str = None):
    if auswahl is None:
        await ctx.send("Please choose between Scissors, Rock or Paper.")
        return

    auswahl = auswahl.lower()
    bot_auswahl = random.choice(['scissors', 'rock', 'paper'])

    if auswahl in ['scissors', 'rock', 'paper']:
        if auswahl == bot_auswahl:
            await ctx.send(f"Unentschieden! Ich habe auch {bot_auswahl}.")
        elif (auswahl == 'scissors' and bot_auswahl == 'paper') or \
             (auswahl == 'rock' and bot_auswahl == 'scissors') or \
             (auswahl == 'paper' and bot_auswahl == 'rock'):
            await ctx.send(f"Won! I had {bot_auswahl}.")
        else:
            await ctx.send(f"Lost! I had {bot_auswahl}.")
    else:
        await ctx.send("Please choose between Scissors, Rock or Paper.")

@bot.command(name='status')
async def serverinfo(ctx):
    answer = check_port(IP, ms_port)
    await ctx.send(embed=answer)

@bot.command(name='help')
async def help_command(ctx):
    await ctx.send("Available commands:\n!game - Play Rock, Paper, Scissors\n!status - Check server status\n!help - Show this help message")

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(token)
