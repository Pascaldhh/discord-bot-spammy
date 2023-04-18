import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("./.env")
TOKEN = os.getenv("TOKEN")

class BasicBot(commands.Bot):
  def __init__(self, *, command_prefix, intents: discord.Intents):
    super().__init__(command_prefix=command_prefix, intents=intents)

  async def setup_hook(self):
    await self.loading_extensions()
    await self.tree.sync(guild=None)

  async def on_ready(self):
    print(f"Bot {self.user} is online.")

  async def loading_extensions(self):
    await self.load_extension(name="src.Greetings")
    await self.load_extension(name="src.DirectMessager")
    await self.load_extension(name="src.React")

bot = BasicBot(command_prefix="?", intents=discord.Intents.all())
bot.run(TOKEN)