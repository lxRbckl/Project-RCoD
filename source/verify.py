def verify(
   
   screen,
   contact
   
):
   '''  '''
   
   return screen.find(
      
      confidence = 0.98,
      image = f'asset/contact/{contact}.png'
      
   )