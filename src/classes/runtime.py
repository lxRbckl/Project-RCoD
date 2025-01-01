# import <
from os import popen

# >


class runtime():
   
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   def _checkForStop(self, screen):
      '''  '''
      
      return screen.find(
         
         confidence = 0.9,
         image = "assets/runtime/stop.png"
         
      )
      
      
   def stop(self, screen):
      '''  '''
      
      if (self._checkForStop(screen)):
         
         popen('pmset displaysleepnow')
         return True
            
      else: return False