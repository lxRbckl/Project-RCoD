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
         image = "assets/roles/call.png"
         
      ))
   
   
   def answer(self, screen):
      '''  '''
      
      screen.click(screen.find(
         
         confidence = 0.95,
         image = "assets/roles/answer.png"
         
      ))