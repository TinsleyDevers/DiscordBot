import discord
import praw
import youtube_dl
import os
import random
import shutil
import asyncio
import discordslashcommands as dsc
from discord.ext import commands, tasks
from discord.utils import get
from discord.voice_client import VoiceClient
from itertools import cycle
from os import system

# opening files w/ strings
with open('Others\Token.txt','r') as file:
    TokenRead = file.read()

# strings to referrence from.
BOT_PREFIX = '!' # Prefix the bot use | EX: !help, .help
AmericanEmoji = '🔫'
AustraliaEmoji = "🦘"
Connection = 793629106923110450 # Address for Telephone | Channel ID goes here
client = commands.Bot(command_prefix=BOT_PREFIX, help_command=None)

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
@client.command(aliases=['Help', 'pages', 'Pages'])
async def help(ctx):
    contents = ["**---Index---\n-Page 1: Index\n-Page 2: Utilities\n-Page 3: Fun\n-Page 4: Music\n-Page 5: Moderation**",
                "**---Utilities---**\n**!help** | shows this command.\n**!age @mention** | shows the join & account age of mentioned user.\n**!user @mention** | shows mentioned, user-info.\n**!ping** | pings the bot and responds with latency.",
                "**---Fun---**\n**!reddit (reddit name)** | shows a random post from that reddit. - DO NOT USE FOR NSFW!\n**!meme** | shows a random meme.\n**!dog** | shows a random picture of a dog.\n**!aww** | shows a random cute image.\n**!slap @mention** | slaps the mentioned user.\n**!kill @meniton** | kills the mentioned user.\n**!hug @mention** | hugs the mentioned user\n**!lick @meniton** | licks the mentioned user.\n**!kiss @mention** | kisses the mentioned user.\n**!8ball (question)** | answers your question.",
                "**---Music---**\n**!join** | joins your currently connected voice channel.\n**!leave** | leaves your currently connected voice channel.\n**!play (song name)** | plays & queues the song you requested.\n**!pause** | pauses the current song.\n**!unpause** | unpauses the paused song.\n**!stop** | stops the song and removes it from queue.\n**!next** | plays the next song in queue.\n**!volume** | changes the volume of the bot",
                "**---Moderation---**\n**!clear (amount)** | clears the chat.\n**!ban @mention** | bans the mentioned user.\n**!kick @mention** | kicks the mentioned user.\n**!unban (userid)** | unbans the user."]
    pages = 5
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    await message.add_reaction("<:Cross:793787279461449769>")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️", "<:Cross:793787279461449769>"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "<:Cross:793787279461449769>":
                await ctx.message.delete()
                await message.delete()

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await ctx.message.delete()
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds

# Fun
FunStream = open("Scripts\Fun.py")
FunRead = FunStream.read()
exec(FunRead)

# Music
MusicStream = open("Scripts\Music.py")
MusicRead = MusicStream.read()
exec(MusicRead)

# Moderation
ModStream = open("Scripts\Moderation.py")
ModRead = ModStream.read()
exec(ModRead)

# Utilities
ToolStream = open("Scripts\Tools.py")
ToolRead = ToolStream.read()
exec(ToolRead)

# This is the Bot's token.
TOKEN = TokenRead
client.run(TOKEN)

# NOTES FOR ME
# EX: @commands.has_permissions(kick_members=True) | SETS PERMISSIONS FOR USERS TO ACCESS COMMAND.
