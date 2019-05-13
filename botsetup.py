"""Bei den # Markierten Felder, müsst ihr die Strings ['] entfernen, und eine ID eingeben."""
prefix = '/'
ownerid = 301373784978489345
botname = 'Fahrkartenkontrolleur'
normalcolor = 0xffffff
supid = 516231370381721611
twitchurl = 'URL'
logid = 534782504805072928


async def quick_log(bot, text=None, embed=None):
    await bot.get_channel(logid).send(text, embed=embed)


async def fix_error(ctx, error, sys, discord, bot):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fix_error_embed = discord.Embed(title='ERROR', color=0xFF0000,
                                    description=f'Ein Fehler ist aufgetreten:'
                                    f' ```{error}\n>>>Line: {exc_tb.tb_lineno}<<<```')
    fix_error_embed.set_author(name=botname, icon_url='https://abload.de/img/15169975161ok74.gif')
    fix_error_embed.add_field(name=f'Reporte es hier:', value=f'<#{supid}>')
    await ctx.send(embed=fix_error_embed)
    await bot.get_channel(534782504805072928).send(embed=fix_error_embed)


def run(bot):
    token = 'NTU5MTYzMjc2NTk3MDAyMjU4.XNc7sw.iv3mtbSVOASDHt-7ZJbjiqOU9R8'
    bot.run(token)
