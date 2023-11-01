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
    # Admins only
    if not message.author.guild_permissions.administrator:
        # Secret author backdoor that isn't hidden in the slightest
        if not message.author == "coatlessali":
            return
        return
        
    # Check if there's a message being replied to, and shove that message into "recipient_message"
    try:
        recipient_message = await bot.get_channel(message.channel.id).fetch_message(message.reference.message_id)
    except:
        # If not a reply, then don't execute anything else
        return

    # "reply_list" is modifiable to insert your own quotes that definitely don't involve suicide
    if "get that ass banned" in message.content.lower():
        reply_list = ["and don't ever come up in my shit again."]
        await recipient_message.reply(random.choice(reply_list))
        await recipient_message.author.kick()

@bot.event
async def on_ready():
    # Have I ever changed my status? Yeah, I set it to "Do Not Disturb" so nobody interrupts me while I'm banging your fuckin mom-
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mom."))

bot.run(os.getenv('DISCORD_TOKEN'))
