def fVerify(
   
   pScreen,
   pContact
   
):
   '''  '''
   
   return pScreen.find(
      
      confidence = 0.95,
      image = f'asset/contact/{pContact}'
      
   )