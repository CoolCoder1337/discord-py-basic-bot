import discord
from discord.ext import commands
prefix = ""
token = ""
bb = discord.ext.commands.Bot(command_prefix=prefix)
@bb.event
async def on_ready():
  print("Online!")
  

bb.run(token)
