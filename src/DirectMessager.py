import discord
from discord.ext import commands, tasks

class DirectMessager(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.spamMembers = {}

  @commands.Cog.listener()
  async def on_ready(self):
    self.spammingUsers.start()

  @tasks.loop(seconds=10)
  async def spammingUsers(self):
    for member, message in self.spamMembers.items():
      direct_message = await member.create_dm()
      await direct_message.send(f"<@{member.id}> {message}")

  @commands.hybrid_command(name="dm-me", description="The bot dm's you")
  async def dmMe(self, ctx):
    direct_message = await ctx.author.create_dm()
    await direct_message.send(f"Suprise, **Spammy** is in your dm's :p\n<@{ctx.author.id}>")
    await ctx.send(f"Succesfully send dm to <@{ctx.author.id}>")

  @commands.hybrid_command(name="spam-dm", description="The bot spams a user in dm")
  async def spamDm(self, ctx, member: discord.Member, message: str = "you're cool"):
    if member.id in self.spamMembers.keys():
      await ctx.send(f"Already spamming user <@{member.id}>")
      return

    await ctx.send(f"spamming <@{member.id}> in dm every 10 seconds")
    self.spamMembers[member] = message

  @commands.hybrid_command(name="stop-spam-dm", description="Stop spam dm'in someone you like")
  async def disableSpamDm(self, ctx, member: discord.Member):
    if member not in self.spamMembers.keys():
      await ctx.send(f"I'm not spam dm'in <@{member.id}>..")
      return
    del self.spamMembers[member]
    await ctx.send(f"Stopped spam'in <@{member.id}>")

async def setup(bot):
  await bot.add_cog(DirectMessager(bot))