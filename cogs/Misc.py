import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      '''the command triggered on any error'''
      await ctx.send(error)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user}')
    
    




def setup(client):
    client.add_cog(Misc(client))
