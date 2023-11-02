# todo: optimize this shit and remove unnecessary code

import os
import nacl
import discord
import random
import string
from discord.ext import commands, tasks
from dotenv import load_dotenv
load_dotenv()
bot = commands.Bot(intents=discord.Intents.all() , command_prefix='Mods, ')

# Shows help page.
@bot.command(name='helpme', aliases=['man', '?'])
async def helpme(message):
    await message.channel.send("`Available Commands: help, sourceCode, license, github`\n\> \*Mods? You already know what to do.\*")

# Sends important source files.
@bot.command(name='sourceCode', aliases=['source', 'sauce'])
async def sourceCode(ctx):
    await ctx.send(file=discord.File('LICENSE'))
    await ctx.send(file=discord.File('CrushHisSkull.py'))

# Shows WTFPL license.
@bot.command(name='license', aliases=["wtfpl"])
async def license(message):
    licenseText = open('LICENSE', 'r').read()
    await message.channel.send(f"```\n{licenseText}\n```")

# Shows author's Github page.
@bot.command(name='githubSource', aliases=["github"])
async def githubSource(message):
    await message.channel.send(f"{message.author.mention} https://github.com/coatlessali/LowTierBot")

# Listens for messages.
@bot.listen()
async def on_message(message):

    # Make the bot ignore itself
    if message.author.bot:
        return

    # Filter for non-admins and definitely not ali
    admin = message.author.guild_permissions.administrator
    author = message.author

    is_not_admin = not admin
    is_not_ali = not (author == "coatlessali")

    worthless_cuck = is_not_admin and is_not_ali

    if worthless_cuck:
        return
        
    # Check if there's a message being replied to, and shove that message into "recipient_message"
    try:
        recipient_message = await bot.get_channel(message.channel.id).fetch_message(message.reference.message_id)
    except:
        # If the message isn't a reply, then don't execute anything else
        return

    # Check to see if someone is getting that ass banned
    contents = message.content.lower()
    crush_skull = "mods" in contents "crush" in contents and "skull" in contents
    ass_banned = "get that ass banned" in contents
    kick_trigger = crush_skull or ass_banned
    
    if kick_trigger:
        # Below is a list of possible replies, seperated by comma and quotes.
        reply_list = ["and don't ever come up in my shit again.", "You worthless cuck."]
        await recipient_message.reply(random.choice(reply_list))
        # Initiate kicking
        await recipient_message.author.kick()

@bot.event
async def on_ready():
    # Have I ever changed my status? Yeah, I set it to "Do Not Disturb" so nobody interrupts me while I'm banging your fuckin mom-
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mom."))

bot.run(os.getenv('DISCORD_TOKEN'))
