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
