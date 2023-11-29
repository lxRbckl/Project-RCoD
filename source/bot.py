# import <
from source.function.call import call
from source.function.answer import answer
from source.function.verify import verify

from os import popen
from lxrbckl.gpt import gpt
from lxrbckl.screen import screen
from discord.ext import (tasks, commands)
from discord import (Object, Intents, app_commands)
from discord.ext.commands.errors import CommandRegistrationError

# >


class Bot(commands.Bot):
   
   def __init__(
      
      self,
      pRole,
      pContact,
      pTokenOpenai,

      pRoles = ['call', 'answer'],
      pGuildId = 974210528958369863,
      pMotivation = 'Tell me something motivating!'
      
   ):
      '''  '''
      
      self.role = pRole
      self.roles = pRoles
      self.screen = screen()
      self.guildId = pGuildId
      self.contact = pContact
      self.gpt = gpt(pTokenOpenai)
      self.motivation = pMotivation
      
      super().__init__(
         
         command_prefix = '',
         intents = Intents.all()
         
      )
      
      
   async def on_ready(self):
      '''  '''
      
      # try (if new commands) <
      # except (then existing) <
      # finally (run algorithm) <
      try:
         
         self.registerOff()
         self.registerSwitch()
         self.registerVolume()
         
         await self.tree.sync(guild = Object(id = self.guildId))
            
      except CommandRegistrationError: pass
      finally : self.algorithm.start()
      
      # >
         
   
   @tasks.loop(seconds = 55)
   async def algorithm(self):
      '''  '''
      
      # if (on contact) <
      if (verify(screen = self.screen, contact = self.contact)):
      
         {
            
            'call' : call,
            'answer' : answer
            
         }[self.role](screen = self.screen)
         
      # >
   
   
   def registerOff(self):
      '''  '''
      
      @self.hybrid_command(
         
         name = 'off',
         description = 'Turns off RCoD Bot'
      
      )
      @app_commands.guilds(Object(id = self.guildId))
      @app_commands.describe(query = self.motivation)
      async def off(ctx, query: str = self.motivation):
         ''' '''
         
         # message user <
         # shut off <
         response = await self.gpt.message(message = query)
         await ctx.reply(response, ephemeral = True)
         
         popen('pmset displaysleepnow')
         exit()
         
         # >


   def registerSwitch(self):
      '''  '''
      
      @self.hybrid_command(
      
         name = 'switch',
         description = 'Transition to a different camera.'
      
      )
      @app_commands.guilds(Object(id = self.guildId))
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
   
   
   def registerVolume(self):
      '''  '''
   
      @self.hybrid_command(
         
         name = 'volume',
         description = 'Adjust computer volume.'
         
      )
      @app_commands.describe(role = 'Role')
      @app_commands.choices(role = [
         
         app_commands.Choice(
            
            name = i,
            value = i
            
         )
         
      for i in self.roles])
      @app_commands.describe(level = 'Number')
      @app_commands.guilds(Object(id = self.guildId))
      async def volume(
         
         ctx,
         level: int,
         role: app_commands.Choice[str]
         
      ):
         '''  '''
         
         # if (is role) <
         if (self.role == role.value):
         
            popen(f'osascript -e "set volume output volume {level}"')
            await ctx.reply(f'`Role:` `{role.value}`\n`Volume:` `{level}`')            
         
         # >