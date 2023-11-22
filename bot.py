# import <
from os import popen
from asyncio import sleep
from discord import Intents
from datetime import datetime
from lxrbckl.screen import screen
from discord.ext.commands import Bot

# >


class cBot(Bot):
   
   def __init__(
      
      self,
      pRole,
      pToken,
      pChannel = 1062210162129129492
      
   ):
      '''  '''
      
      self.role = pRole
      self.token = pToken      
      self.screen = screen()
      self.channel = pChannel
      
      Bot.__init__(
         
         self,
         command_prefix = '',
         intents = Intents.all()
         
      )

      
   async def on_ready(self):
      '''  '''
      
      await self.listen()
   
   
   def call(self):
      '''  '''
      
      # find call <
      # click call <
      x, y = self.screen.find(
         
         grayscale = True,
         confidence = 0.95,
         image = 'asset/facetime/call.png'
         
      )
      self.screen.click(x = x, y = y)
      
      # >
         
   
   def answer(self):
      '''  '''
      
      # find answer <
      # click answer <
      x, y = self.screen.find(
         
         grayscale = True,
         confidence = 0.95,
         image = 'asset/facetime/answer.png'
         
      )
      self.screen.click(x = x, y = y)
      
      # >
   
   
   async def listen(self):
      '''  '''      
      
      while (True):
         
         print('here')
         await sleep(30)
         
   
   def register(self):
      '''  '''
      
      @Bot.hybrid_command(
         
         self, 
         name = 'Switch',
         description = 'Transition to a different camera.'
      
      )
      async def switch(ctx):
         '''  '''
         
         # open <
         # find more <
         # click more <
         self.screen.move(x = 500, y = 500)
         x, y = self.screen.find(
            
            grayscale = True,
            confidence = 0.95,
            image = 'asset/camera/more.png'
            
         )
         self.screen.click(x = x, y = y)
         
         # >
         
         # find available <
         # click available <
         x, y = self.screen.find(
            
            grayscale = True,
            confidence = 0.95,
            image = 'asset/camera/available.png'
            
         )
         self.screen.click(x = x, y = y)
         
         # >
      
      
      @Bot.hybrid_command(
         
         self,
         name = 'Off',
         description = 'Turns of RCoD Bot'
         
      )
      async def off(ctx):
         ''' '''
         
         popen('pmset displaysleepnow')
         exit()