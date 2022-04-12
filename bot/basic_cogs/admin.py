import discord
from discord.ext import commands

# Admin/Dev only commands (put admin id in DEVS)
class Admin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx: discord.ApplicationContext):
        if str(ctx.author.id) not in ctx.bot.DEVS:
            msg = await ctx.send(f"{ctx.command.name} is a dev only command")
            await msg.delete(delay=5)
            return False
        return True;

    # Pong command
    @commands.command(name = "ping", aliases=["p"])
    async def ping(self, ctx:commands.Context):
        await ctx.send("Pong! Latency: {:.2f}".format(self.bot.latency * 1000), delete_after=5)
        



def setup(bot:commands.Bot):
    bot.add_cog(Admin(bot))