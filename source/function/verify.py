def fVerify(
   
   pScreen,
   pContact
   
):
   '''  '''
   
   return pScreen.find(
      
      confidence = 0.99,
      image = f'asset/contact/{pContact}'
      
   )