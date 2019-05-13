# import discord
from discord.ext import commands
import botsetup
import logging

bot = commands.Bot(command_prefix=botsetup.prefix)
logging.basicConfig(level=logging.INFO)
bot.owner_id = botsetup.ownerid
"""Das "#" nur entfernen, wenn du ein Help Command schreibst."""
# bot.remove_command('help')


@bot.event
async def on_ready():
    """Wenn der Bot Startet, führt er ein Print aus."""
    print('___________________________')
    print('FahrkartenKontrolleur BOT')
    print('___________________________')
    logging.info(f'\nUsername: {bot.user.name}#{bot.user.discriminator}\nID: {bot.user.id}')

cogs = [
    'commands'
]

"""Lädt Cogs"""
for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

"""Startet Bot"""
botsetup.run(bot)
