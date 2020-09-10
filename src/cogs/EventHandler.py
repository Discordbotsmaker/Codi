from discord.ext import commands
import discord

import random
import os

#env
from dotenv import load_dotenv
load_dotenv()

#define client
client = commands.Bot(command_prefix=os.getenv("PREFIX"))

roles = {
    "c_": 751526041809584168,
    "cpp": 751525042537627748,
    "csharp": 752228975127953484,
    "css": 752226862796898417,
    "html": 751525079241982033,
    "js": 751525158816317572,
    "ts": 751525213170171925,
    "vuejs": 752227111414268015,
    "reactjs": 752227077595332694,
    "nodejs": 752227035899887657,
    "go": 751525988973674556,
    "r_": 751526019025862867,
    "python": 751525058442297385,
    "java": 751525011017171041,
    "rust": 751525960968306730
}

class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.message_id)
        if payload.message_id == 752244419864035429:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            role = member.guild.get_role(roles[payload.emoji.name])
            if member is not None:
                await member.add_roles(role)
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 752244419864035429:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            role = member.guild.get_role(roles[payload.emoji.name])
            print(role)
            if member is not None:
                await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = member.guild.name
        role = member.guild.get_role(752247003819409450)
        await member.add_roles(role)

        embed = discord.Embed(
            color=discord.Color(random.randint(0x000000, 0xFFFFFF)),
            title='Welcome Message',
            description=f'Welcome to {server} {member.mention}!'
        )
        await member.send(embed=embed)


def setup(bot):
    bot.add_cog(EventHandler(bot))