# import <
from os import popen

# >


class runtime():
   
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   def checkForStop(self, screen):
      '''  '''
      
      return screen.find(
         
         confidence = 0.9,
         image = "assets/facetime/stop.png"
         
      )
      
      
   def stop(self):
      '''  '''
      
      popen('pmset displaysleepnow')
      exit(0)