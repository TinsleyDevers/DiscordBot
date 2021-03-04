reddit = praw.Reddit(client_id ='g_ljbxm_pS2kKw',
                    client_secret = 'wR8XiGGcHPsLdRjtfNQv0RvE2yWA_A',
                    user_agent ='MusicAndGamesBot')

# Reddit/Meme Command
@client.command(aliases=['Meme', 'Memes', 'memes', 'Reddit', 'reddit'])
async def meme(ctx, subred = "memes"):
    submission = reddit.subreddit(subred).random()
    await ctx.send(submission.url)
    return

# Puppy Command
@client.command(aliases=['puppies', 'Puppies', 'Puppy', 'babydog', 'Babydog', 'BabyDog', 'dog', 'Dog', 'Dogs', 'dogs'])
async def puppy(ctx, subred = "puppy"):
    submission = reddit.subreddit(subred).random()
    await ctx.send(submission.url)
    return

# Aww Command
@client.command(aliases=['aw', 'Aw', 'Aww', 'awe', 'Awe', 'Awww', 'awww'])
async def aww(ctx, subred = "aww"):
    submission = reddit.subreddit(subred).random()
    await ctx.send(submission.url)
    return

#Slap Command  // WIP
@client.command(aliases=['Slap'])
async def slap(ctx, *, member: discord.Member):
    responses = [
        f"{member.name} has sadly passed away due to being DUMB",
        f"{member.name} was hurt by you being mean",
        f"{member.name} didn't stand a chance",
        f"{member.name} is sad now :(",
        f"{member.name} isn't feeling it mr krabs.",
        f"{member.name} has lost all sense of direction and is now spiraling down into an endless pit of sorrow and sadness doesn't know what to do now and they are plotting their revenge while also giving up on everything and everyone."]
    gifs = ["https://tenor.com/xhlc.gif",
            "https://tenor.com/bbHX6.gif",
            "https://tenor.com/bjOZT.gif",
            "https://tenor.com/E1MC.gif",
            "https://tenor.com/wIbu.gif",
            "https://tenor.com/8ps1.gif",
            "https://tenor.com/blgKM.gif",
            "https://tenor.com/7EU6.gif",
            "https://tenor.com/bkOur.gif",
            "https://tenor.com/bmMOI.gif",
            "https://tenor.com/sMgo.gif",
            "https://tenor.com/T3n1.gif",
            "https://tenor.com/J9fE.gif",
            "https://tenor.com/3Syd.gif",
            "https://tenor.com/HyAC.gif",
            "https://tenor.com/bgql7.gif",
            "https://tenor.com/bnf3g.gif",
            "https://tenor.com/T3nh.gif",
            "https://tenor.com/brJ00.gif",
            "https://tenor.com/F3Xx.gif",
            "https://tenor.com/bg1Jg.gif",
            "https://tenor.com/bq6S5.gif",
            "https://tenor.com/bgHIX.gif",
            "https://tenor.com/blIUs.gif",
            "https://tenor.com/btBg7.gif",
            "https://tenor.com/T3nR.gif",
            "https://tenor.com/T3nR.gif",
            "https://tenor.com/bmI3Y.gif"]
    await ctx.send(f"**{ctx.message.author.mention} slapped:** {member.mention}\n{random.choice(responses)}\n{random.choice(gifs)}")
    await asyncio.sleep(3)
    await ctx.message.delete()
    return

#Kill/Shoot Command  // WIP
@client.command(aliases=['Kill', 'Shoot', 'shoot'])
async def kill(ctx, *, member: discord.Member):
    responses = [
        f"Hey! Let's do some tiktok dances on {member.name}'s grave in memorial of them!'",
        f"Mamaaaa I just killed ({member.name}) didn't mean to make you cry.",
        f"{member.name}: Lost but not forgotten. actually yeah kinda forgotten EVERYTHING ISN'T ABOUT YOU {member.name}",
        f"{member.name} this is so sad, can we get an L in the chat for my dead friend.",
        f"{member.name} I won't let this happen to you...\n{member.mention} comes out of the grave and with their power they lift {ctx.message.author.mention} up into the ground and slams multiple times over and over again into the pavement."]
    gifs = ["https://tenor.com/PV5d.gif",
            "https://tenor.com/w4jp.gif",
            "https://tenor.com/LD2r.gif",
            "https://tenor.com/bmG91.gif",
            "https://tenor.com/bmO5u.gif",
            "https://tenor.com/btIx0.gif",
            "https://tenor.com/bk2h2.gif",
            "https://tenor.com/EfV2.gif",
            "https://tenor.com/bsrj7.gif",
            "https://tenor.com/bh4Y3.gif",
            "https://tenor.com/yFrl.gif"]
    await ctx.send(f"**{ctx.message.author.mention} killed:** {member.mention}\n{random.choice(responses)}\n{random.choice(gifs)}")
    await asyncio.sleep(3)
    await ctx.message.delete()
    return

#Hug Command  // WIP
@client.command(aliases=['Hug', 'Hold', 'hold'])
async def hug(ctx, *, member: discord.Member):
    responses = [
        f"{member.name} was hugged so tightly they passed out",
        f"{member.name} was held lovingly"]
    gifs = ["https://tenor.com/UDdM.gif",
            "https://tenor.com/bhraa.gif",
            "https://tenor.com/9VUn.gif",
            "https://tenor.com/FQNP.gif",
            "https://tenor.com/biMNv.gif",
            "https://tenor.com/7lZ6.gif",
            "https://tenor.com/ETCF.gif",
            "https://tenor.com/vQcO.gif",
            "https://tenor.com/7Wko.gif",
            "https://tenor.com/bmpnc.gif",
            "https://tenor.com/MLKl.gif",
            "https://tenor.com/PM3W.gif",
            "https://tenor.com/bb9kg.gif",
            "https://tenor.com/Nu12.gif",
            "https://tenor.com/1jRF.gif",
            "https://tenor.com/bnbIs.gif",
            "https://tenor.com/baHmj.gif",
            "https://tenor.com/bnEtd.gif",
            "https://tenor.com/bgGhm.gif",
            "https://tenor.com/oY1o.gif",
            "https://tenor.com/FQNR.gif",
            "https://tenor.com/FQNU.gif",
            "https://tenor.com/blXR1.gif",
            "https://tenor.com/4ocV.gif",
            "https://tenor.com/btfSd.gif",
            "https://tenor.com/v1L6.gif",
            "https://tenor.com/bhlaU.gif",
            "https://tenor.com/bcVv8.gif",
            "https://tenor.com/bnvmy.gif",
            "https://tenor.com/7mxR.gif",
            "https://tenor.com/booMX.gif",
            "https://tenor.com/Nw86.gif",
            "https://tenor.com/btf1h.gif",
            "https://tenor.com/ZOap.gif",
            "https://tenor.com/bgyzF.gif",
            "https://tenor.com/xPCb.gif",
            "https://tenor.com/Z5t6.gif",
            "https://tenor.com/G98q.gif",
            "https://tenor.com/PDah.gif",
            "https://tenor.com/be3CQ.gif"]
    await ctx.send(f"**{ctx.message.author.mention} hugged:** {member.mention}\n{random.choice(responses)}\n{random.choice(gifs)}")
    await asyncio.sleep(3)
    await ctx.message.delete()
    return

#Lick Command  // WIP
@client.command(aliases=['Lick'])
async def lick(ctx, *, member: discord.Member):
    responses = [
        f"{member.name} was licked, EWWW!",
        f"{member.name} was licked... lovingly??",
        f"{member.name} was shown what that tounge do"]
    gifs = ["https://tenor.com/P827.gif",
            "https://tenor.com/7Sn5.gif",
            "https://tenor.com/basQN.gif",
            "https://tenor.com/Y6Mt.gif",
            "https://tenor.com/uyfz.gif",
            "https://tenor.com/4Bvg.gif",
            "https://tenor.com/Y6Mn.gif",
            "https://tenor.com/bglo1.gif",
            "https://tenor.com/bj8Iw.gif",
            "https://tenor.com/bmLlf.gif",
            "https://tenor.com/bnWf5.gif",
            "https://tenor.com/bhfu6.gif",
            "https://tenor.com/6UVl.gif",
            "https://tenor.com/biSOf.gif"]
    await ctx.send(f"**{ctx.message.author.mention} licked:** {member.mention}\n{random.choice(responses)}\n{random.choice(gifs)}")
    await asyncio.sleep(3)
    await ctx.message.delete()
    return

#Kiss Command  // WIP
@client.command(aliases=['Kiss', 'smooch', 'Smooch'])
async def kiss(ctx, *, member: discord.Member):
    responses = [
        f"{member.name} was kissed on the knee",
        f"{member.name} was kissed on the elbow",
        f"{member.name} was kissed on the shoulder",
        f"{member.name} was kissed on the lips",
        f"{member.name} was kissed on the eyelid",
        f"{member.name} was kissed on the eyeball",
        f"{member.name} was kissed on the ear",
        f"{member.name} was kissed on the nose",
        f"{member.name} was kissed on the forehead",
        f"{member.name} was kissed on the cheek",
        f"{member.name} was kissed on the hand",
        f"{member.name} was kissed on the foot",
        f"{member.name} was kissed on the toe",
        f"{member.name} was kissed on the finger",
        f"{member.name} was kissed on the arm",
        f"{member.name} was kissed on the neck",
        f"{member.name} was kissed on the back"]
    gifs = ["https://tenor.com/bdq8l.gif",
            "https://tenor.com/wMKO.gif",
            "https://tenor.com/bfhTQ.gif",
            "https://tenor.com/bpN3G.gif",
            "https://tenor.com/bne8u.gif",
            "https://tenor.com/2nX4.gif",
            "https://tenor.com/Y683.gif",
            "https://tenor.com/PIoc.gif",
            "https://tenor.com/2oAL.gif",
            "https://tenor.com/ba8M6.gif",
            "https://tenor.com/bbjcL.gif",
            "https://tenor.com/bi3Ct.gif",
            "https://tenor.com/11HE.gif",
            "https://tenor.com/bk57O.gif",
            "https://tenor.com/wHJu.gif",
            "https://tenor.com/5tgc.gif",
            "https://tenor.com/zZxa.gif",
            "https://tenor.com/uX8n.gif",
            "https://tenor.com/RCju.gif",
            "https://tenor.com/uCg2.gif",
            "https://tenor.com/uquG.gif",
            "https://tenor.com/zZwX.gif",
            "https://tenor.com/Z93A.gif",
            "https://tenor.com/OJXy.gif",
            "https://tenor.com/PrAb.gif",
            "https://tenor.com/6fqy.gif",
            "https://tenor.com/05fP.gif",
            "https://tenor.com/vxPx.gif",
            "https://tenor.com/bk57E.gif"]
    await ctx.send(f"**{ctx.message.author.mention} kissed:** {member.mention}\n{random.choice(responses)}\n{random.choice(gifs)}")
    await asyncio.sleep(3)
    await ctx.message.delete()
    return

# Telephone & Reactions
@client.event
async def on_message (message):
    # React to Messages
    if ("America") in message.content:
        await message.add_reaction(AmericanEmoji)
    if ("america") in message.content:
        await message.add_reaction(AmericanEmoji)
    if ("Australia") in message.content:
        await message.add_reaction(AustraliaEmoji)
    if ("australia") in message.content:
        await message.add_reaction(AustraliaEmoji)
    # Telephone to another server
    if message.author != client.user:
        if (message.channel.id == 793629200326197259):# Music And Games ID
            Telephone = client.get_channel(Connection)   # Music & Games > Undefined
            await Telephone.send(f'**{message.author.name}**: {message.content}')
        if (message.channel.id == (Connection)): #Undefined ID
            Telephone = client.get_channel(793629200326197259) # Undefined > Music and Games
            await Telephone.send(f'**{message.author.name}**: {message.content}')
    await client.process_commands(message)

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
