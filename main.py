# Project RCoN by Alex Arbuckle #


# import <
from discord import Intents
from datetime import datetime
from lxRbckl import requestsGet
from discord.ext import commands, tasks
from pyautogui import click, locateCenterOnScreen

# >


# global <
discordToken = ''

gInput = 'on'
gChannel = 1062210162129129492
RCoD = commands.Bot(command_prefix = '', intents = Intents.all())
gSettingLink = 'https://raw.githubusercontent.com/lxRbckl/Project-RCoD/main/setting.json'
gTime = [

    '01 AM',
    '02 AM',
    '03 AM',
    '04 AM',
    '05 AM',
    '06 AM',
    '07 AM'

]

# >


@RCoD.command(aliases = requestsGet(pLink = gSettingLink)['aliases'])
async def commandFunction(ctx):
    '''  '''

    global gInput
    gInput = ctx.invoked_with.lower()


@tasks.loop(minutes = 1)
async def loopFunction():
    '''  '''

    # try if (facetime online) <
    # except then (facetime online) <
    try:

        if ((datetime.now().strftime('%I %p') in gTime) and (gInput != 'off')):

            # find facetime <
            # click facetime <
            pos = locateCenterOnScreen('asset/facetime.jpeg', confidence = 0.9, grayscale = True)
            click(x = (pos[0] / 2), y = (pos[1] / 2))

            await RCoD.get_channel(gChannel).send(':man_mage: FaceTime Recovered')

            # >

    except TypeError: pass

    # >


@RCoD.event
async def on_ready(): loopFunction.start()


# main <
if (__name__ == '__main__'): RCoD.run(discordToken)

# >
