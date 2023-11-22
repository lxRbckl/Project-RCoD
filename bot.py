# import <
from os import popen
from asyncio import sleep
from datetime import datetime
from discord.ext import tasks
from discord.ext.commands import Bot
from discord import (
   
   Intents,
   app_commands
   
)

# >


class cBot:
   
   def __init__(
      
      self,
      role,
      token,
      channel = 1062210162129129492
      
   ):
      '''  '''
      
      self.role = role
      self.token = token
      self.channel = channel
      
      self.bot = Bot(
         
         command_prefix = '',
         intents = Intents.all()
         
      )
      
   
   def run(self):
      '''  '''
      
      self.bot.run(self.token)
      
   
   def call(self):
      ''' '''
      
      pass
   
   
   def answer(self):
      '''  '''
      
      pass
   
   
   def listen(self):
      '''  '''
      
      pass