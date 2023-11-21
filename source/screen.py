# import <
from pyautogui import (
   
   size,
   click,
   moveTo,
   locateCenterOnScreen
   
)

# >


class screen:
   
   def __init__(
      
      self,
      isRetinaDisplay = True
      
   ):
      '''  '''
      
      self.isRetinaDisplay = isRetinaDisplay
   
   
   def move(self):
      '''  '''
      
      fDisplay = lambda i : i / 2 if (self.isRetinaDisplay) else i
      x, y = map(fDisplay, size())
      
      moveTo(x, y)
   
   
   def click(
      
      self,
      x,
      y,
      times = 1
      
   ):
      '''  '''
      
      for i in range(times): click(x, y)

   
   def locate(
      
      self,
      image,
      grayscale,
      confidence
      
   ):
      '''  '''
      
      return locateCenterOnScreen(
         
         image = image,
         grayscale = grayscale,
         confidence = confidence
         
      )
   


# remove
x = screen()
print(x.move())