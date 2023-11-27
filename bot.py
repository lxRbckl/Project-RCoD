# import <
from os import popen
from discord.ext.commands import errors
from discord.ext.commands.context import Context
from lxrbckl.screen import screen
from discord.ext.commands.errors import CommandRegistrationError
from discord import (
   
   Object,
   Intents,
   app_commands
   
)
from discord.ext import (
   
   tasks,
   commands
   
)

# >


class Bot(commands.Bot):
   
   def __init__(
      
      self,
      pRole,
      pToken,
      pContact,

      pRoles = ['call', 'answer'],
      pGuild = 974210528958369863,
      pChannel = 1062210162129129492
      
   ):
      '''  '''
      
      self.role = pRole
      self.roles = pRoles
      self.guild = pGuild
      self.token = pToken
      self.screen = screen()
      self.contact = pContact
      self.channel = pChannel
      
      super().__init__(
         
         command_prefix = '',
         intents = Intents.all()
         
      )
      
      
   async def on_ready(self):
      '''  '''
      
      # add commands <
      # run algorithm <
      self.register()
      await self.tree.sync(guild = Object(id = self.guild))
      
      self.listen.start()
      
      # >
         
   
   def mute(self):
      '''  '''
      
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/mic/unmuted.png'
         
      ))
   
   
   def call(self):
      '''  '''
         
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/facetime/call.png'
         
      ))
               
   
   def answer(self):
      '''  '''
      
      self.screen.click(self.screen.find(
         
         confidence = 0.95,
         image = 'asset/facetime/answer.png'
         
      ))
      
   
   def verify(self):
      '''  '''
      
      return self.screen.find(
         
         confidence = 0.98,
         image = f'asset/contact/{self.contact}.png'
         
      )
   
   
   @tasks.loop(seconds = 30)
   async def listen(self):
      '''  '''
      
      # if (on contact) <
      if (self.verify()):
      
         {
            
            'call' : self.call,
            'answer' : self.answer
            
         }[self.role]()
         
      # >
                                             
   
   def register(self):
      '''  '''
      
      try:
         
         @self.hybrid_command(
            
            name = 'volume',
            description = 'Adjust computer volume.'
            
         )
         @app_commands.guilds(Object(id = self.guild))
         @app_commands.describe(num = 'Number')
         @app_commands.describe(role = 'Role')
         @app_commands.choices(role = [
            
            app_commands.Choice(
               
               name = i,
               value = i
               
            )
            
         for i in self.roles])
         async def volume(
            
            ctx,
            num: int,
            role: app_commands.Choice[str]
            
         ):
            '''  '''
            
            # if (is role) <
            if (self.role == role.value):
            
               popen(f'osascript -e "set volume output volume {num}"')
               await ctx.reply(f'`Role:` `{role.value}`\n`Volume:` `{num}`')            
            
            # >

      
         @self.hybrid_command(
         
            name = 'switch',
            description = 'Transition to a different camera.'
         
         )
         @app_commands.guilds(Object(id = self.guild))
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
            

         
         
         # @self.hybrid_command(
            
         #    name = 'off',
         #    description = 'Turns off RCoD Bot'
         
         # )
         # async def off(ctx):
         #    ''' '''
            
         #    popen('pmset displaysleepnow')
         #    exit()
         
      except CommandRegistrationError: pass