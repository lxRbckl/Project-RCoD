# import <
from os import popen
from discord import Intents
from datetime import datetime
from discord.ext import(
   
   tasks,
   commands
   
)

# >


class jabot:
   
   
   
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
      self.bot = commands.Bot(
         
         command_prefix = '',
         intents = Intents.all()
         
      )
      
   
   async def run(self):
      '''  '''
      
      print(self.token)
      
   
   