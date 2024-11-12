def fMute(
   
   pScreen,
   pMuteAfterCall
   
):
   '''  '''
   
   # if (mute call) <
   if (pMuteAfterCall):
   
      pScreen.click(pScreen.find(
         
         confidence = 0.95,
         image = 'asset/mic/unmuted.png'
         
      ))
      
   # >