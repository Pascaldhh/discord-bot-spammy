from discord.ext import commands

class Greetings(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.hybrid_command(name="hello-bot", description="The bot says hello to you")
  async def sayhello(self, ctx):
    await ctx.send(f"Hey <@{ctx.author.id}>")

async def setup(bot):
  await bot.add_cog(Greetings(bot))