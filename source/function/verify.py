def fVerify(
   
   pScreen,
   pContact
   
):
   '''  '''
   
   return pScreen.find(
      
      confidence = 0.98,
      image = f'asset/contact/{pContact}.png'
      
   )