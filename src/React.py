from random import randint
from discord.ext import commands

class React(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.emojis = ["😀", "😃", "😄", "😁", "😆", "🥹", "😅", "😂", "🤣", "🥲", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘"]

  @commands.hybrid_command(name="react", description="Bot reacts with random emoji (only works with the ? prefix -> ?react)")
  async def reactEmoji(self, ctx):
    await ctx.message.add_reaction(self.emojis[randint(0, len(self.emojis)-1)])

async def setup(bot):
  await bot.add_cog(React(bot))