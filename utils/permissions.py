
# creates a connection to the DB
from discord.ext import commands

# Receives a permissions and the roles of a user
# Checks if any of the roles has the needed Permission


def hasPermission(ctx, cog):
    conn = ctx.bot.DBC
    for crole in ctx.author.roles:
        conn.query(f"SELECT id, permission FROM permissions where role_id='{crole.id}' AND (permission = '*' OR permission = '{cog}.*' OR permission = '{cog}.{ctx.command}');")
        if len(conn.fetch_rows()) is not 0:
            return True

    return False

def listPermissions(ctx, role):
    conn = ctx.bot.DBC
    perms = ""
    conn.query(f"SELECT permission FROM permissions where role_id='{role.id}' ORDER BY permission;")
    for perm in conn.fetch_rows():
        perms += f"{perm['permission']}\n"
    return perms


def owner_only():
    async def predicate(ctx):
        return ctx.bot.is_owner(ctx.author)
    return commands.check(predicate)
