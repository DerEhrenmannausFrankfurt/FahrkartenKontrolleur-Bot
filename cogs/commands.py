import asyncio
import discord
from discord.ext import commands
import botsetup
import random


ilink = 'https://i.gifer.com/8CHv.gif'
alltext = 'für mehr Commands gebe /bottalk ein'
puhgif = 'https://noktara.de/wp-content/uploads/phew.gif'
bombegif = 'https://media.giphy.com/media/HhTXt43pk1I1W/giphy.gif'
lighton = 'https://www.licht.de/fileadmin/bildarchiv/_processed_/8/d/csm_09_lw14_026_OS_Wohnzimmer_002f69bfad.jpg'
lightoff = 'https://media-cdn.holidaycheck.com/w_1280,h_720,c_fit,q_80/ugc/images/1da6bff8-3cdf-3a4b-8171-e5a4e3b411f6'


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # /test
    async def test(self, ctx):
        """Ein Beispiel Command im Embed"""
        test = discord.Embed(title='Test', description='Verstanden', color=0x00ff19)
        await ctx.send(embed=test)
        await botsetup.quick_log(self.bot, embed=test)
        await botsetup.quick_log(self.bot, f'{ctx.author.name} hat ein Test durchgeführt.')
        test.set_footer(text=alltext, icon_url=ilink)

    @commands.command()
    # /pommes
    async def pommes(self, ctx):
        pommes = discord.Embed(title='!!!🍟POMMES🍟!!!', description='POMMES!!!', color=0xffff11)
        pommes.set_thumbnail(url='https://media1.giphy.com/media/4T1KlY8tSnrq6q7FY1/giphy.gif')
        pommes.set_author(name='Pommes🍟', url='https://www.instagram.com/schwarzfahrer528')
        pommes.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=pommes)

    @commands.command()
    # /bombe
    async def bombe(self, ctx):
        bombe = discord.Embed(title='', description='ACHTUNG!!! BOMBE:bomb:', color=0xff0000)
        bombe.set_author(name='BOMBE', icon_url='')
        bombe.set_thumbnail(url='https://gifimage.net/wp-content/uploads/2017/09/bombe-gif-5.gif')
        bombe.set_footer(text=alltext, icon_url=ilink)
        nobomb = discord.Embed(title='OH NEIN:boom::boom:',
                               description=':boom:Die Bombe ist explodiert:boom:', color=0xbc0000)
        nobomb.set_thumbnail(url=bombegif)
        await ctx.send(embed=bombe)
        await botsetup.quick_log(self.bot, embed=bombe)
        await botsetup.quick_log(self.bot, f'{ctx.author.name} Wollte eine Bombe auslösen')
        oneortwo = random.randint(1, 2)
        await asyncio.sleep(2)
        if oneortwo == 1:
            bombe2 = discord.Embed(title='Oh ist doch nichts passiert!',
                                   description='da hat wohl jemand versucht eine Bombe auszulösen',
                                   color=0x00ff19)
            bombe2.set_thumbnail(url=puhgif)
            bombe2.set_footer(text=alltext, icon_url=ilink)
            await ctx.send(embed=bombe2)
        if oneortwo == 2:
            await ctx.send(embed=nobomb)

    @commands.command()
    # /bottalk
    async def bottalk(self, ctx):
        bottalk = discord.Embed(title='Der Bot reagiert auf folgende Commands:\n'
                                      '/pommes\n'
                                      '/siri\n'
                                      '/bombe\n'
                                      '/hey\n'
                                      '/hi\n'
                                      '/alexa\n'
                                      '/alexamachdaslichtaus\n'
                                      '_______________________________________\n'
                                      '/bottalk zeigt dir Commands an\n'
                                      '/setgame (/setlisten, /setlisten2, /setstream) ändert den Status\n'
                                      '/test testet den Bot\n'
                                      '', description='')
        bottalk.set_author(name='FahrkartenKontrolleur Bot', url='https://www.instagram.com/schwarzfahrer528\n')
        bottalk.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=bottalk)

    @commands.command()
    # /hey
    async def hey(self, ctx):
        hey = discord.Embed(title='Hi!', description='wie gehts dir so?', color=botsetup.normalcolor)
        hey.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=hey)

    @commands.command()
    # /hi
    async def hi(self, ctx):
        hi = discord.Embed(title='', description='was ist denn heute wieder los🤔', color=botsetup.normalcolor)
        hi.set_author(name='du schon wieder🙄')
        hi.set_thumbnail(url='https://thumbs.gfycat.com/DifficultDiligentCobra-small.gif')
        hi.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=hi)

    @commands.command()
    # /feedback
    async def feedback(self, ctx, *, text):
        print('________________________________')
        print('Feedback (Eines Anonymen Users):')
        print(text)
        print('________________________________')
        await asyncio.sleep(2)
        feedback = discord.Embed(title='Dein Feedback hilft den Server',
                                 description='Teile uns dein Feedback mit /feedback', color=botsetup.normalcolor)
        feedback.add_field(name='Dein Feedback bleibt bei uns Anonym',
                           value='Dein Anonymer Feedback wird lediglich in der '
                                 'Konsole gespeichert ohne deinen Nutzernamen'
                                 'Dein Feedback:{text}')
        feedback.set_thumbnail(
            url='https://www.bqool.com/wp-content/themes/courtyard/images/amazon-feedback-software_05.gif')
        feedback.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=feedback)

    @commands.command()
    # /siri
    async def siri(self, ctx):
        heysiri = discord.Embed(title='MEIN NAME IST FAHRKARTENKONTROLLEUR😡',
                                description='Wer ist überhaupt diese Siri die kann doch nichts🤬', color=0xff0000)
        heysiri.set_thumbnail(url='https://thumbs.gfycat.com/CourteousUnfoldedKoalabear-size_restricted.gif')
        heysiri.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=heysiri)

    @commands.command()
    # /setlisten
    async def setlisten(self, ctx):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.listening, name='/bottalk'))
        changegame = discord.Embed(title='Der Bot Status wurde zu', description='"Hört auf /bottalk" verändert',
                                   color=0x2dff31)
        changegame.set_thumbnail(
            url='https://media1.tenor.com/images/f482b8ee6d41a003808cabfd5f309c54/tenor.gif?itemid=7824812')
        changegame.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=changegame)

    @commands.command()
    # /setlisten2
    async def setlisten2(self, ctx):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.listening, name='dich!'))
        changegame = discord.Embed(title='Der Bot Status wurde zu', description='"Hört auf dich" verändert',
                                   color=0x2dff31)
        changegame.set_thumbnail(url='https://i.pinimg.com/originals/28/42/85/284285df2da60877fb17f4243f5013c1.gif')
        changegame.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=changegame)

    @commands.command()
    # /setgame
    async def setgame(self, ctx):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.playing, name='mit dir'))
        changegame = discord.Embed(title='Der Bot Status wurde zu', description='"Spielt mit dir" verändert',
                                   color=0x00e803)
        changegame.set_thumbnail(url='https://media.giphy.com/media/y0NFayaBeiWEU/giphy.gif')
        changegame.set_footer(text=alltext, icon_url=ilink)
        await ctx.send(embed=changegame)

    @commands.command()
    # /setstream
    async def setstream(self, ctx):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.streaming, name='mit dir'))
        changegame = discord.Embed(title='Der Bot Status wurde zu', description='"Streamt mit dir" verändert',
                                   color=0xee00ff)
        changegame.set_footer(text=alltext, icon_url=ilink)
        changegame.set_thumbnail(url='https://media.giphy.com/media/sS2LbFGIKoTqU/200.gif')
        await ctx.send(embed=changegame)

    @commands.command()
    async def shutdown(self, ctx):
        shutdown = discord.Embed(title='Shutdown', description='Der Bot wird heruntergefahren')
        await ctx.send(embed=shutdown)
        await quit(0)

    @commands.command()
    async def alexamachdaslichtan(self, ctx):
        alexalighton = discord.Embed(title='schon wieder du', description='Das Licht wird eingeschaltet')
        alexalighton.set_thumbnail('https://www.licht.de/fileadmin/bildarchiv/_processed_/8/d/csm_09_lw14_026_OS_Wohnzimmer_002f69bfad.jpg')
        alexalightoff = discord.Embed(title='du schon wieder!', description='DAS LICHT BLEIBT AUS')
        alexalightoff.set_thumbnail(lightoff)
        await ctx.send(embed=alexalighton)



def setup(bot):
    bot.add_cog(Commands(bot))
