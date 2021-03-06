# Reaction Roles
@client.command(aliases=['react', 'role', 'Role', 'React', 'Roles', 'roles', 'Reaction'], pass_context=True)
async def reaction(ctx):
    member = ctx.message.author
    dm = await member.create_dm()
    valoranter = discord.utils.get(member.guild.roles, name = "valoranter")
    minecrafter = discord.utils.get(ctx.guild.roles, name = "minecrafter")
    ruster = discord.utils.get(ctx.guild.roles, name = "ruster")
    rainbower = discord.utils.get(ctx.guild.roles, name = "rainbower")
    gmoder = discord.utils.get(ctx.guild.roles, name = "gmoder")
    leauger = discord.utils.get(ctx.guild.roles, name = "leauger")
    message = await ctx.send(f"<:valorant:817618905731301386> for valoranter\n<:minecraft:817619421139959838> for minecrafter\n<:rust:817619487343771678> for ruster\n<:rainbowsixs:817618905886883850> for rainbower\n<:gmod:817618907602092032> for gmoder\n<:LeaugeOfLegends:817618905806798859> for leauger\n<:Cross:793787279461449769> to close this message")

    await message.add_reaction("<:valorant:817618905731301386>")
    await message.add_reaction("<:minecraft:817619421139959838>")
    await message.add_reaction("<:rust:817619487343771678>")
    await message.add_reaction("<:rainbowsixs:817618905886883850>")
    await message.add_reaction("<:gmod:817618907602092032>")
    await message.add_reaction("<:LeaugeOfLegends:817618905806798859>")
    await message.add_reaction("<:Cross:793787279461449769>")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["<:valorant:817618905731301386>", "<:minecraft:817619421139959838>", "<:rust:817619487343771678>", "<:rainbowsixs:817618905886883850>", "<:gmod:817618907602092032>", "<:LeaugeOfLegends:817618905806798859>", "<:Cross:793787279461449769>"]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=15, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            if str(reaction.emoji) == "<:valorant:817618905731301386>":
                if valoranter in user.roles:
                    await member.remove_roles(valoranter)
                    await dm.send(f"<:valorant:817618905731301386> has been removed from your roles")
                else:
                    await member.add_roles(valoranter)
                    await dm.send(f"<:valorant:817618905731301386> was added to your roles")
            elif str(reaction.emoji) == "<:minecraft:817619421139959838>":
                if minecrafter in user.roles:
                    await member.remove_roles(minecrafter)
                    await dm.send(f"<:minecraft:817619421139959838> has been removed from your roles")
                else:
                    await member.add_roles(minecrafter)
                    await dm.send(f"<:minecraft:817619421139959838> was added to your roles")
            elif str(reaction.emoji) == "<:rust:817619487343771678>":
                if ruster in user.roles:
                    await member.remove_roles(ruster)
                    await dm.send(f"<:rust:817619487343771678> has been removed from your roles")
                else:
                    await member.add_roles(ruster)
                    await dm.send(f"<:rust:817619487343771678> was added to your roles")
            elif str(reaction.emoji) == "<:rainbowsixs:817618905886883850>":
                if rainbower in user.roles:
                    await member.remove_roles(rainbower)
                    await dm.send(f"<:rainbowsixs:817618905886883850> has been removed from your roles")
                else:
                    await member.add_roles(rainbower)
                    await dm.send(f"<:rainbowsixs:817618905886883850> was added to your roles")
            elif str(reaction.emoji) == "<:gmod:817618907602092032>":
                if gmoder in user.roles:
                    await member.remove_roles(gmoder)
                    await dm.send(f"<:gmod:817618907602092032> has been removed from your roles")
                else:
                    await member.add_roles(gmoder)
                    await dm.send(f"<:gmod:817618907602092032> was added to your roles")
            elif str(reaction.emoji) == "<:LeaugeOfLegends:817618905806798859>":
                if leauger in user.roles:
                    await member.remove_roles(leauger)
                    await dm.send(f"<:LeaugeOfLegends:817618905806798859> has been removed from your roles")
                else:
                    await member.add_roles(leauger)
                    await dm.send(f"<:LeaugeOfLegends:817618905806798859> was added to your roles")
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

# Age Command
@client.command(aliases=['Age'])
async def age(ctx, member: discord.Member):
    created_at = member.created_at.strftime("%b %d, %Y")
    joined_at = member.joined_at.strftime("%b %d, %Y")
    await ctx.send(f"**{member.name}'s** Account Created: {created_at} \n**{member.name}** Joined: {joined_at}")

# Userinfo command
@client.command(aliases=['user', 'account', 'userinfo'])
async def whois(ctx, member : discord.Member):
    created_at = member.created_at.strftime("%b %d, %Y")
    joined_at = member.joined_at.strftime("%b %d, %Y")
    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Color.lighter_grey())
    embed.add_field(name = "ID", value = member.id, inline = False)
    embed.add_field(name = "Account Age", value = created_at, inline = True)
    embed.add_field(name = "Server Join", value = joined_at, inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

# Ping Command
@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.send(
        f'<:online:793620927023677451> Pong! I have responded. | (it took me {round(client.latency * 1000)}ms) <:online:793620927023677451>')
