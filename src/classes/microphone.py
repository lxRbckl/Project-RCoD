# import <


# >


class microphone:
   
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   def _checkFacetime(self, screen):
      '''  '''
   
      screen.move(xy = [500, 500])
   
   
   def _checkForUnmute(self, screen):
      '''  '''
      
      self._checkFacetime(screen)
      
      return screen.find(
         
         confidence = 0.90,
         image = "assets/microphone/unmuted.png"
         
      )
   
   
   def mute(self, screen):
      '''  '''
      
      isUnmuted = self._checkForUnmute(screen)
      
      if (isUnmuted): screen.click(xy = isUnmuted)
      