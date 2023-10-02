# Project RCoD by Alex Arbuckle #


# import <
from os import popen
from asyncio import sleep
from discord import Intents
from datetime import datetime
from lxRbckl import requestsGet
from discord.ext import commands, tasks
from pyautogui import (size, click, locateCenterOnScreen, moveTo)

# >


# token <
# global <
discordToken = ''
 
gIndex = 0
gInput = 'on'
gChannel = 1062210162129129492
RCoD = commands.Bot(command_prefix = '', intents = Intents.all())
gSettingLink = 'https://raw.githubusercontent.com/lxRbckl/Project-RCoD/main/setting.json'
gCameras = [
    
    'usb.png',
    'computer.png'
    
]
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


# @RCoD.command(aliases = requestsGet(pLink = gSettingLink)['aliases'])
# async def commandFunction(ctx):
#     '''  '''

#     global gInput
#     gInput = ctx.invoked_with.lower()


@RCoD.command(aliases = requestsGet(pLink = gSettingLink)['switch'])
async def switchFunction(ctx):
    '''  '''
    
    global gIndex
    gIndex += 1
    print('0')
    x1, y1 = size()
    moveTo(x = (x1 / 2), y = (y1 / 2))
    print('1')
    pos = locateCenterOnScreen('asset/more.png', confidence = 0.9, grayscale = True)
    click(x = (pos[0] / 2), y = (pos[1] / 2))
    print('2')
    pos = locateCenterOnScreen(
        
        image = f'asset/{gCameras[(gIndex % len(gCameras))]}', 
        confidence = 0.8, 
        grayscale = True
    
    )
    click(x = (pos[0] / 2), y = (pos[1] / 2))
    print('3')
    sleep(1) # remove
    moveTo(x = (x1 / 2), y = ((y1 / 2) - 250))
    click(x = (x1 / 2), y = ((y1 / 2) - 250))
    print('4')


@tasks.loop(minutes = 1)
async def loopFunction():
    '''  '''

    # try if (facetime online) <
    # except then (facetime online) <
    try:

        # if (off) <
        # elif (on) <
        if (gInput == 'off'):

            popen('pmset displaysleepnow')
            exit()

        elif ((datetime.now().strftime('%I %p') in gTime) and (gInput != 'off')):

            # find facetime <
            # click facetime <
            pos = locateCenterOnScreen('asset/facetime.jpeg', confidence = 0.9, grayscale = True)
            click(x = (pos[0] / 2), y = (pos[1] / 2))

            await RCoD.get_channel(gChannel).send(':man_mage: FaceTime Recovered')

            # >

        # >

    except TypeError: pass

    # >





@RCoD.event
async def on_ready(): 
    
    print()
    loopFunction.start()


# main <
if (__name__ == '__main__'): RCoD.run(discordToken)

# >
