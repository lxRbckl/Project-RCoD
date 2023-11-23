# import <
from os import popen
from asyncio import sleep
from discord import Intents
from discord.ext import tasks
from lxrbckl.screen import screen
from discord.ext.commands import Bot

# >


class cBot(Bot):
   
   def __init__(
      
      self,
      pRole,
      pToken,

      pInterval = 5,
      pChannel = 1062210162129129492,
      pDuration = {
         
         'call' : 20,
         'answer' : 3
         
      }
      
   ):
      '''  '''
      
      self.role = pRole
      self.token = pToken
      self.screen = screen()
      self.channel = pChannel
      self.duration = pDuration
      self.interval = pInterval
      
      Bot.__init__(
         
         self,
         command_prefix = '',
         intents = Intents.all()
         
      )
      
      
   async def on_ready(self):
      '''  '''
      
      # add commands <
      # run algorithm <
      self.register()
      synced = await self.tree.sync()
      
      await self.listen()
      
      # >
   
   
   async def call(self):
      '''  '''
      
      print('call') # remove
      
      # find call <
      # click call <
      # wait to end <
      x, y = self.screen.find(
         
         grayscale = True,
         confidence = 0.95,
         image = 'asset/facetime/call.png'
         
      )
      self.screen.click(x = x, y = y)
      
      # >
               
   
   async def answer(self):
      '''  '''
      
      print('answer') # remove
      
      # find answer <
      # click answer <
      x, y = self.screen.find(
         
         grayscale = True,
         confidence = 0.95,
         image = 'asset/facetime/answer.png'
         
      )
      self.screen.click(x = x, y = y)
      
      # >
   
   
   @tasks.loop(seconds = 30)
   async def listen(self):
      '''  '''
         
      try:

         await {
            
            'call' : self.call,
            'answer' : self.answer
            
         }[self.role]()
         await sleep(self.duration[self.role])
                     
      except ValueError: pass
                        
   
   def register(self):
      '''  '''
      
      @self.hybrid_command(
      
         name = 'switch',
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
      
      
      @self.hybrid_command(
         
         name = 'off',
         description = 'Turns off RCoD Bot'
      
      )
      async def off(ctx):
         ''' '''
         
         popen('pmset displaysleepnow')
         exit()