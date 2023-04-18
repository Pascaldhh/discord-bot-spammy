import json
from random import randint
from urllib.request import Request, urlopen
from discord.ext import commands


class Quoter(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self.quotes = json.loads(urlopen(Request("https://type.fit/api/quotes", headers={'User-Agent': 'Mozilla/5.0'})).read())

    @commands.hybrid_command(name="quote", description="The bot generates a random quote")
    async def randomQuote(self, ctx):
      quote = self.quotes[randint(0, len(self.quotes)-1)]
      await ctx.send(f"\"{quote['text']}\" ~ *{quote['author']}*")

async def setup(bot):
  await bot.add_cog(Quoter(bot))