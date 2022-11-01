import asyncio
import random
from typing import Optional
import discord
from discord.ext import commands
from discord import app_commands
import dbutils
from config import guilds

ROLES = [
    {"name": "League of Legends", "role_id": 1037133173919858829},
    {"name": "Valorant", "role_id": 1037094545965461556},
    {"name": "Genshin", "role_id": 1037133179150151731},
]

class RoleButton(discord.ui.Button):

    def __init__(self, role):
        self.role = role
        # if the role has the "emoji" property it will be on the button aswell
        try:
            super().__init__(emoji=role["emoji"], style=discord.ButtonStyle.blurple, label=role["name"], custom_id=role["name"])
        except:
            super().__init__(style=discord.ButtonStyle.green, label=role["name"], custom_id=role["name"])
    async def callback(self, interaction):
        # Switch out the role
        user_roles = interaction.user.roles
        role = discord.utils.get(interaction.guild.roles, id=self.role["role_id"])
        if role in user_roles:
            await interaction.user.remove_roles(role)
        else:
            await interaction.user.add_roles(role)

        try:
            await interaction.response.send_message()
        except:
            return
class RoleButtonView(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=None)
        for role in roles:
            button = RoleButton(role)
            self.add_item(button)


class basic(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name="test", description="test")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("Deez Nuts")

    @commands.command()
    async def roleassignment(self, ctx):
        em = discord.Embed(title="Roles", description="Hello and welcome, here you can select your roles!",
                           colour=discord.Color.dark_teal())
        await ctx.send(embed=em)
        em = discord.Embed(title="What games are you interested in?", colour=discord.Color.dark_teal())
        await ctx.send(embed=em, view=RoleButtonView(ROLES))


async def setup(client):
    await client.add_cog(basic(client), guilds=guilds)
