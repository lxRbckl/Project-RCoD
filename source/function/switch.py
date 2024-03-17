def fSwitch(pScreen):
   '''  '''
   
   # open <
   # click more <
   # click available <
   pScreen.move(xy = [500, 500])
   pScreen.click(pScreen.find(
      
      confidence = 0.95,
      image = 'asset/camera/more.png'
      
   ))
   pScreen.click(pScreen.find(
      
      confidence = 0.95,
      image = 'asset/camera/available.png'
      
   ))
   pScreen.click(xy = [500, 1000])
   
   # >