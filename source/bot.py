# import <
from source.function.off import fOff
from source.function.mute import fMute
from source.function.call import fCall
from source.function.switch import fSwitch
from source.function.answer import fAnswer
from source.function.verify import fVerify
from source.function.volume import fVolume

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
      pQuery,
      pGuildId,
      pContact,
      pTokenOpenai,
      
      isMuted = True,
      pRoles = ['call', 'answer']
            
   ):
      '''  '''
      
      self.role = pRole
      self.roles = pRoles
      self.query = pQuery
      self.isMuted = isMuted
      self.contact = pContact
      
      self.screen = screen()
      self.guildId = pGuildId
      self.gpt = gpt(pTokenOpenai)
      
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
         
         self.tree.clear_commands(guild = Object(self.guildId))
         await self.tree.sync(guild = Object(id = self.guildId))
         
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
      # if (is muted) <
      if (fVerify(pScreen = self.screen, pContact = self.contact)):
      
         {
            
            'call' : fCall,
            'answer' : fAnswer
            
         }[self.role](pScreen = self.screen)
         
      if (self.isMuted): fMute(pScreen = self.screen)
         
      # >
   
   
   def registerOff(self):
      '''  '''
      
      @self.hybrid_command(
         
         name = 'off',
         description = 'Turns off RCoD Bot'
      
      )
      @app_commands.guilds(Object(id = self.guildId))
      @app_commands.describe(query = 'custom query')
      async def off(ctx, query: str = self.query):
         ''' '''

         fOff(
            
            ctx = ctx,
            pQuery = query,
            oGPT = self.gpt
            
         )


   def registerSwitch(self):
      '''  '''
      
      @self.hybrid_command(
      
         name = 'switch',
         description = 'Transition to a different camera.'
      
      )
      @app_commands.guilds(Object(id = self.guildId))
      async def switch(ctx): fSwitch(self.screen)
   
   
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
      @app_commands.describe(level = 'Level')
      @app_commands.guilds(Object(id = self.guildId))
      async def volume(
         
         ctx,
         level: int,
         role: app_commands.Choice[str]
         
      ):
         '''  '''
         
         await fVolume(
            
            ctx = ctx,
            pLevel = level,
            pRole = self.role,
            pRoleValue = role.value
            
         )