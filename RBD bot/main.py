import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import config
Intents = discord.Intents()
Intents.members = True

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=(config.PREFIX), intents=intents) 
bot.remove_command('help')

 ## all Events
@bot.event
async def on_ready():
 print('--------')
 print('You are running RBD v1')
 print('Created by Razer bot Development')
 print('--------')

 ## Error meesage
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
    channel=bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW ERROR MESSAGE",color=0x9208ea)
    embed.add_field(name="Error message", value=f"{(error)}", inline=True),
    
    await channel.send(embed=embed)
    ## Deleted messages
@bot.event
async def on_message_delete(message):
    channel=bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW DELETED MESSAGE",color=0x9208ea)
    embed.add_field(name="USER", value=f"{message.author.name}", inline=True),
    embed.add_field(name="DELETE MESSAGE", value=f"{message.content}", inline=True),
    embed.add_field(name="CHANNEL", value=f"{message.channel}", inline=True),
    await channel.send(embed=embed)

    ## All commands 



    ## Help command
@bot.command()
async def help(ctx):
        embed=discord.Embed(title="Help Menu!",color=0xFF5733)
        embed.add_field(name="help", value="To say the help menu", inline=True),
        embed.add_field(name="say", value="To say something as the bot", inline=True),
        embed.add_field(name="suggest", value="To make a suggestion", inline=True),
        embed.add_field(name="embed", value="To send a embed message as the bot", inline=True),
        embed.add_field(name="verify", value="To verify yourself ", inline=True),
        embed.add_field(name="dm", value="To dm someone as the bot", inline=True),
        embed.add_field(name="kick", value="To kick someone from the server", inline=True),
        embed.add_field(name="ban", value="To ban someone from the server", inline=True),
        embed.add_field(name="unban", value="To unban someone from the server", inline=True),
        embed.add_field(name="warn", value="To warn someone in your server", inline=True),
        embed.add_field(name="giverole", value="To add a role to someone", inline=True),
        embed.add_field(name="removerole", value="To remove a role to someone", inline=True),
        embed.add_field(name="clear", value="To clear messages from a server", inline=True),
        embed.add_field(name="mute", value="To mute someone", inline=True),
        embed.add_field(name="unmute", value="To unmute someone", inline=True),
        embed.add_field(name="new", value="To open a ticket", inline=True),
        embed.add_field(name="close", value="To close a ticket", inline=True),
        embed.add_field(name="claim", value="To claim a ticket", inline=True),
        embed.add_field(name="rename", value="To rename a ticket", inline=True),
        await ctx.send(embed=embed)
        await ctx.message.delete()

    ## UTILITIES COMMANDS
    ## Say command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()
    ## Embed command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx,title,message):
    embed=discord.Embed(title=title,description=message)
    await ctx.send(embed=embed)
@bot.command()
async def dm(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)
    await ctx.message.delete()

 ## verify comamnds 
@bot.command(pass_context=True)
async def verify(ctx,user: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="tested")
    await user.add_roles(role)
    dm = await bot.fetch_user(user.id)
    em=discord.Embed(title="Verified", description=f"You are now verified in Server: {ctx.guild.name}")
    await dm.send(embed=em)
    ## MOD COMMANDS 
    ## Kick command
@bot.command()
@commands.has_permissions(kick_members=True)

async def kick(ctx, member: discord.Member, *, reason=None):
    dm = await bot.fetch_user(member.id)
    em=discord.Embed(title="kicked", description=f"Server: {ctx.guild.name}\nServer ID: {ctx.guild.id}\nReason: {reason}")
    await dm.send(embed=em)
    await member.kick(reason=reason)

    await ctx.send(f'User {member} was kicked.')
    await ctx.message.delete()
    channel = bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW KICKED",color=0x9208ea)
    embed.add_field(name="USER", value=f"{member}", inline=True),
    embed.add_field(name="REASON", value=f"{reason}", inline=True),
    await channel.send(embed=embed)

    ## ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    dm = await bot.fetch_user(member.id)
    em=discord.Embed(title="Banned", description=f"Server: {ctx.guild.name}\nServer ID: {ctx.guild.id}\nReason: {reason}")
    await dm.send(embed=em)
    await member.ban(reason=reason)
    await ctx.send(f'User {member} was banned.')
    await ctx.message.delete()
    channel = bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW BANNED",color=0x9208ea)
    embed.add_field(name="USER", value=f"{member.name}", inline=True),
    embed.add_field(name="USER ID ", value=f"{member.id}", inline=True),
    embed.add_field(name="REASON", value=f"{reason}", inline=True),
    await channel.send(embed=embed)
        ## unban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User):
    await ctx.guild.unban(user)
    await ctx.send(f"{user.name} has been unbanned!")
    await ctx.message.delete()
    channel = bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW UNBANNED",color=0x9208ea)
    embed.add_field(name="USER", value=f"{user.name}", inline=True),
    await channel.send(embed=embed)
        ## Warn command
@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member,*, reason=None):
    await ctx.send(f"{member.name} has been warned!")
    dm = await bot.fetch_user(member.id)
    em=discord.Embed(title="Warning", description=f"Server: {ctx.guild.name}\nServer ID: {ctx.guild.id}\nReason: {reason}")
    await dm.send(embed=em)
    channel = bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW WARNED",color=0x9208ea)
    embed.add_field(name="USER", value=f"{member}", inline=True),
    embed.add_field(name="REASON", value=f"{reason}", inline=True),
    await channel.send(embed=embed)
    ## Clear command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 0):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Done! Cleared {amount}")


 ## Add role comamnds 
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Hey {ctx.author.name}, {user.name} has been given a role called: {role.name}")
 ## remove role comamnds 
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send(f"Hey {ctx.author.name}, {user.name} has been revoked of a role called: {role.name}")
 ## Mute command
@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx,user: discord.Member,reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await user.add_roles(role)
    await ctx.send(f"{user.name} has been muted!")
    dm = await bot.fetch_user(user.id)
    em=discord.Embed(title="Muted", description=f"Server: {ctx.guild.name}\nServer ID: {ctx.guild.id}\nReason: {reason}")
    await dm.send(embed=em)
    channel = bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW MUTED",color=0x9208ea)
    embed.add_field(name="USER", value=f"{user}", inline=True),
    embed.add_field(name="REASON", value=f"{reason}", inline=True),
    await channel.send(embed=embed)
 ## unMute command
@bot.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx,user: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted" )
    await user.remove_roles(role)
    await ctx.send(f"{user.name} has been unmuted!")
    dm = await bot.fetch_user(user.id)
    em=discord.Embed(title="unmuted", description=f"Server: {ctx.guild.name}\nServer ID: {ctx.guild.id}")
    await dm.send(embed=em)
    channel = bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW UNMUTED",color=0x9208ea)
    embed.add_field(name="USER", value=f"{user}", inline=True),
    await channel.send(embed=embed)


    ## TICKET COMMANDS
    ## Claim command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def claim(ctx):
    embed=discord.Embed(title="CLAIMED",description=f"This ticket is now claimed by {ctx.author.name}")
    await ctx.message.delete()
    await ctx.send(embed=embed)
    ## new command
@bot.command()
async def new(ctx):
    support_role = discord.utils.get(ctx.guild.roles, name="Staff")
    overwrites = {
    ctx.author: discord.PermissionOverwrite(view_channel=True),
    ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False,send_messages=True),
    support_role: discord.PermissionOverwrite(view_channel=True)
}    
    ticketchannel = await ctx.guild.create_text_channel(f'Ticket {ctx.author.name}', overwrites=overwrites)
    dm = await bot.fetch_user(ctx.author.id)
    em=discord.Embed(title="Ticket opened", description=f"Your ticket in `Server: {ctx.guild.name}` is now opened!\nchannel name <#{ticketchannel.id}>")
    await dm.send(embed=em)
    await ctx.message.delete()
    channel = bot.get_channel(ticketchannel.id)
    embed=discord.Embed(title=f"Welcome {ctx.author.name} to your ticket!", description=f"Please be patient, we will be with you shortly.",color=0x9208ea)
    await channel.send(embed=embed)
    ## Close command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def close(ctx,user: discord.Member):
    await ctx.channel.delete()
    dm = await bot.fetch_user(user.id)
    em=discord.Embed(title="Ticket closed", description=f"Your ticket in `Server: {ctx.guild.name}` was closed!")
    await dm.send(embed=em)
    ## Change name command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def rename(ctx, channel: discord.TextChannel, *, new_name):
    await channel.edit(name=new_name)
    await ctx.send(f'{channel} Was changed')
    await ctx.message.delete()


@bot.command()
async def suggest(ctx, *, suggestion=None):
    dm = await bot.fetch_user(ctx.author.id)
    em=discord.Embed(title="Suggestion", description=f"Your suggestion was sent to Server: {ctx.guild.name}\nSuggestion: {suggestion}")
    await dm.send(embed=em)
    await ctx.message.delete()
    channel = bot.get_channel(1086799218016002142)
    embed=discord.Embed(title=f"NEW SUGGESTION",color=0x9208ea)
    embed.add_field(name="Submitter", value=f"{ctx.author.name}", inline=True),
    embed.add_field(name="Suggestion", value=f"{suggestion}", inline=False),
    embed2 = await channel.send(embed=embed)
    reaction = '⬆️'
    reaction2 = '⬇️'
    await embed2.add_reaction(reaction)
    await embed2.add_reaction(reaction2)


bot.run(config.TOKEN)
