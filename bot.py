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

      pChannel = 1062210162129129492,
      
   ):
      '''  '''
      
      self.role = pRole
      self.token = pToken
      self.screen = screen()
      self.channel = pChannel
      self.mute = lambda : popen('osascript -e "set volume output volume 0"')
      self.unmute = lambda : popen('osascript -e "set volume output volume 100"')
      
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
      # synced = await self.tree.sync()
      
      await self.listen()
      
      # >
   
   
   async def call(self):
      '''  '''
         
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/facetime/call.png'
         
      ))
               
   
   async def answer(self):
      '''  '''
      
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/facetime/answer.png'
         
      ))
   
   
   @tasks.loop(seconds = 30)
   async def listen(self):
      '''  '''
         
      self.mute()
      await {
         
         'call' : self.call,
         'answer' : self.answer
         
      }[self.role]()
      self.unmute()
                                             
   
   def register(self):
      '''  '''
      
      @self.hybrid_command(
      
         name = 'switch',
         description = 'Transition to a different camera.'
      
      )
      async def switch(ctx):
         '''  '''
         
         # open <
         # click more <
         # click available <
         self.screen.move(xy = [500, 500])
         self.screen.click(self.screen.find(
            
            confidence = 0.95,
            image = 'asset/camera/more.png'
            
         ))
         self.screen.click(self.screen.find(
            
            confidence = 0.95,
            image = 'asset/camera/available.png'
            
         ))
         self.screen.click(xy = [500, 1000])
         
         # >
      
      
      @self.hybrid_command(
         
         name = 'off',
         description = 'Turns off RCoD Bot'
      
      )
      async def off(ctx):
         ''' '''
         
         popen('pmset displaysleepnow')
         exit()