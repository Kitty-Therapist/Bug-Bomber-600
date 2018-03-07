import discord
import time
from discord.ext import commands
from utils import permissions


class ModerationCog:
    config = configparser.ConfigParser()
    config.read('config.ini')
    announce = []
    """This cog includes the mod utils like ban, kick, mute, warn, etc"""
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx:commands.Context):
        return await permissions.hasPermission(ctx, "moderation")

    @commands.command()
    async def roles(selfs, ctx:commands.Context):
        """Shows all roles of the server and their IDs"""
        roles = ""
        ids = ""
        for role in ctx.guild.roles:
            roles += f"<@&{role.id}>\n\n"
            ids += str(role.id) + "\n\n"
        embed = discord.Embed(title=ctx.guild.name + " roles", color=0x54d5ff)
        embed.add_field(name="\u200b", value=roles, inline=True)
        embed.add_field(name="\u200b", value=ids, inline=True)
        await ctx.send(ctx.channel, embed=embed)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Shows the Gateway Ping"""
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.send(f":hourglass: Gateway Ping is {round((t2 - t1) * 1000)}ms :hourglass:")

    @commands.group(name='perms', aliases=['permissions'])
    async def perms(self, ctx:commands.Context):
        """Manages the permissions."""
        if ctx.invoked_subcommand is None:
            permshelp = "`perms` - Shows this help text"\
                        "\n\n`perms add <role> <permission>` -  Adds the given permission to the role" \
                        "\n\n`perms available` - Shows all available permissions **unfinished**"\
                        "\n\n`perms list <role>` - Shows the current permissions of the given role"\
                        "\n\n`perms rmv <role> <permission>` - Removes the given permission form the role"
            embed = discord.Embed(title='Permissions help', color=0x7c519f)
            embed.add_field(name='\u200b', value=permshelp, inline=True)
            await ctx.send(embed=embed)

    @perms.command()
    async def add(self, ctx:commands.Context, role: discord.Role, permission):
        """Adds the given permission to the role."""
        await ctx.send(permissions.addPermission(ctx, role, permission))

    @perms.command()
    async def list(self, ctx:commands.Context, role: discord.Role):
        """Shows all available permissions."""
        perms = permissions.listPermissions(ctx, role)
        if perms == '':
            perms = "This role doesn't has any permissions."
        embed = discord.Embed(title=f"Permissions of {role.name}", color=0x7c519f)
        embed.add_field(name='\u200b', value=perms, inline=True)
        await ctx.send(embed=embed)

    @perms.command(name='available', aliases=['avbl', 'avail', 'avl', 'av'])
    async def available(self, ctx:commands.Context):
        """Shows the current permissions of the given role."""
        info =  "`*`    - Grants access to all commands\n"\
                "`cog.*`    - Grants access to all commands of the cog \n"\
                "`cog.command`  - Grants access to command"
        avail = ""
        for perm in permissions.listAvailable(ctx):
            avail += f"{perm}\n"
        embed = discord.Embed(title='Available permissions', color=0x7c519f)
        embed.add_field(name='Information', value=info, inline=True)
        embed.add_field(name='Available permissions', value=avail, inline=False)
        await ctx.send(embed=embed)

    @perms.command()
    async def rmv(self, ctx:commands.Context, role: discord.Role, permission):
        """Removes the given permission from the role."""
        await ctx.send(permissions.rmvPermission(ctx, role, permission))

    @commands.group(name='announcehelp', aliases=['announce'])
    async def announcement(self, ctx:commands.Context):
        """Shows announcement help"""
        if ctx.invoked_subcommand is None:
            permshelp = "`announcehelp` - Shows this help text." \
                        "\n\n`announce` - Creates an announcement."
            embed = discord.Embed(title='Announcements', color=0x7c519f)
            embed.add_field(name='\u200b', value=permshelp, inline=True)
            await ctx.send(embed=embed)
            
   ## @commands.group(name='announce', aliases=['announcing'])
   ## async def announce(self, ctx, target: str):
     ##   """Announces."""
    ##    try channel = client.get_channel(420586792467693589)
     ##       await message.channel.send("{target}")   
     ##   if perms == '':
     ##       perms = "This role doesn't has any permissions."
def setup(bot):
    bot.add_cog(ModerationCog(bot))
