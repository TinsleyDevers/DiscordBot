# Clear Commannd
@client.command(aliases=['purge', 'Clear', 'Purge'])
async def clear(ctx, amount=0):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit= amount+1)
        await asyncio.sleep(2)
        await ctx.send(f"<a:AnimatedCheckmark:793787234095464499> Sucessfully cleared: {amount}! <a:AnimatedCheckmark:793787234095464499>", delete_after=3)
    else:
        await ctx.send("You are lacking permission to clear the chat.", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
# Ban Command
@client.command(aliases=['Ban'])
async def ban(ctx, member : discord.Member, * ,reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
        await ctx.send(f"Sucessfully Bannned: {member.mention}", delete_after=10)
        await member.ban(reason=reason)
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.send("You are lacking permission to ban this user.", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()

# Kick Command
@client.command(aliases=['Kick'])
async def kick(ctx, member : discord.Member, * ,reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).kick_members):
        await ctx.send(f"Sucessfully Kicked: {member.mention}", delete_after=10)
        await member.kick(reason=reason)
        await asyncio.sleep(10)
        await ctx.message.delete()
    else:
        await ctx.send("You are lacking permission to kick this user.", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
# Unban Command
@client.command(aliases=['Unban'])
async def unban(ctx, *, member):
    if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}", delete_after=10)
                await asyncio.sleep(10)
                await ctx.message.delete()
                return
    else:
        await ctx.send("You are lacking permission to unban this user.", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
