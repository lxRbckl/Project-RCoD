# import <


# >


class roles():
   
   
   def __init__(self):
      '''  '''
   
      pass

   
   def call(self, screen):
      '''  '''
      
      screen.click(screen.find(
         
         confidence = 0.90,
         image = "assets/facetime/call.png"
         
      ))
   
   
   def answer(self, screen):
      '''  '''
      
      screen.click(screen.find(
         
         confidence = 0.95,
         image = "assets/facetime/answer.png"
         
      ))