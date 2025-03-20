import discord
from discord import app_commands
from discord.ext import commands
TOKEN = 'UR TOKEN'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


EMBED_COLOR = 0x263c41


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Anjoman❤Retardan"))
    print(f'Bot is ready. Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="conquest", description="HAHAHAHAHAHA")
async def command3(interaction: discord.Interaction):
    embed = discord.Embed(
        title="I AM CONQUEST",
        description="mark im gonna rape u",
        color=EMBED_COLOR 
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="parham", description="Who is Mohammad Parham Eskandary")
async def command4(interaction: discord.Interaction):
    embed = discord.Embed(
        title="MOHAMMAD PARHAM ESKANDARY (WT MASER)",
        description="Parham says : Discipline is choosing between what you want now and what you want most.\n"
                    "my insta : [Click this](https://www.instagram.com/darth._.a?igsh=MWJoMjVmbXV1cXBwdw==)",
        color=EMBED_COLOR
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/740543719580893204/43fdd833d353d27af842c07394201dcc.webp?size=80")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="saeed", description="Who is Saeed Dodel")
async def command5(interaction: discord.Interaction):
    embed = discord.Embed(
        title="SAEED DODEL (WWE MASER)",
        description="Saeed says : Ostad ahman siyah\n"
                    "my insta : [Click this](https://www.instagram.com/saeedd2003?igsh=NzB3NHZvZGd1d25u)",
        color=EMBED_COLOR
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/861216500899250186/1718d96ac864b43aed32406ff4626477.webp?size=80")
    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
