# import <
from os import popen

# >


async def fOff(
   
   ctx,
   oGPT,
   pQuery,
   pCloser,
   pSkipQuery
   
):
   '''  '''
   
   try:
      
      # if (skip default query) <
      if (pSkipQuery):
         
         response = await oGPT.message(message = pQuery)
         await ctx.reply(response, ephemeral = True)
         
      # >
      
      popen('pmset displaysleepnow')
      await pCloser()

      # exit(0)
   
   except RuntimeError: pass