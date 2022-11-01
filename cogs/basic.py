import asyncio
import random
from typing import Optional
import discord
from discord.ext import commands
from discord import app_commands
import dbutils
from config import guilds


class basic(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name="test", description="test")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("Deez Nuts")

async def setup(client):
    await client.add_cog(basic(client), guilds=guilds)
