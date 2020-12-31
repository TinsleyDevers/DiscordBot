import discord
import youtube_dl
import os
import random
import shutil
from discord.ext import commands, tasks
from discord.utils import get
from discord.voice_client import VoiceClient
from itertools import cycle
from os import system


# strings to referrence from.\
BOT_PREFIX = '!'
client = commands.Bot(command_prefix=BOT_PREFIX, help_command=None)
Connection = 793629106923110450   # Address for Telephone

# Bot Online
@client.event
async def on_ready():
    change_status.start()
    print("------Bot sucessfully loaded!------\n   ----Logged in as: " + client.user.name + "----\n")

# Bot's Status.
@tasks.loop(seconds=90)
async def change_status():
    status = open("TextLists\StatusTexts.txt", "r")
    await client.change_presence(activity=discord.Game(random.choice(status.readlines())))

# Help Command
@client.command(aliases=['stuck', 'info'])
async def help(context):
    await context.send("*you want help little idiot boy, little dumb baby huh??*\n**!help** | seriously need me to tell you this one?\n**!age** | shows your personal Discord Age & Server Join Age. *|* *freakin' old person.*\n**!8ball** | 8ball a fun game of RNG *| going to ask yourself some questions really now?*\n**!join** | the bot will join a voice channel you're currently in. *|* *must be the first time having something or someone in a call with you.*\n**!play** | the bot will play music from a url you provide *|* *somebody finally wants to speak to you.*\n**!leave** | the bot will leave the voice channel if currently connected in one. *|* *now your fake friend is gone; probably the closest thing to a real friend you've had.*\n**!ping** | shows you the ping of the bot. *|* *yet you'll still complain about lag*")

#Music Bot
MBStream = open("Scripts\MusicBot.py")
MBRead = MBStream.read()
exec(MBRead)

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(
        f'<:online:793620927023677451> Pong! I have responded. | (it took me {round(client.latency * 1000)}ms) <:online:793620927023677451>')

# 8ball Command
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Age Command
@client.command(aliases=['ui', 'userinfo', 'account'])
async def age(ctx, member: discord.Member):
    created_at = member.created_at.strftime("%b %d, %Y")
    joined_at = member.joined_at.strftime("%b %d, %Y")
    await ctx.send(f"Account created: {created_at} \nJoined: {joined_at}")\

# Telephone & Reactions
@client.event
async def on_message (message):
    AmericanEmoji = '🔫'
    # React to Messages
    if ("america") in message.content:
        await message.add_reaction(AmericanEmoji)
    if ("America") in message.content:
        await message.add_reaction(AmericanEmoji)
    # Telephone to another server
    if message.author != client.user:
        if (message.channel.id == 793629200326197259):# Music And Games ID
            Telephone = client.get_channel(Connection)   # Music & Games > Undefined
            await Telephone.send(f'**{message.author.name}**: {message.content}')
        if (message.channel.id == (Connection)): #Undefined ID
            Telephone = client.get_channel(793629200326197259) # Undefined > Music and Games
            await Telephone.send(f'**{message.author.name}**: {message.content}')
    await client.process_commands(message)

# This is the Bot's token.
with open('Others\Token.txt','r') as file:
    TokenRead = file.read()
TOKEN = TokenRead
client.run(TOKEN)
