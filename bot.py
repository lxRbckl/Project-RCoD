# import <
from os import popen
from asyncio import sleep
from discord import Intents
from discord.ext import tasks
from lxrbckl.screen import screen
from discord.ext.commands import Bot
from discord.ext.commands.errors import CommandRegistrationError

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
      self.volume = lambda i : popen('osascript -e "set volume output volume {i}"')
      
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
      await self.tree.sync()
      
      await self.listen.start()
      
      # >
      
   
   def mute(self):
      '''  '''
      
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/mic/unmuted.png'
         
      ))
   
   
   async def call(self):
      '''  '''
         
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/facetime/call.png'
         
      ))
      self.mute()
               
   
   async def answer(self):
      '''  '''
      
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/facetime/answer.png'
         
      ))
   
   
   @tasks.loop(seconds = 30)
   async def listen(self):
      '''  '''
      
      await {
         
         'call' : self.call,
         'answer' : self.answer
         
      }[self.role]()
                                             
   
   def register(self):
      '''  '''
      
      try:
      
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
         
      except CommandRegistrationError: pass