import discord, os
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Online als {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
