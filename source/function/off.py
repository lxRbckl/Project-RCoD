# import <
from os import popen

# >


async def fOff(
   
   ctx,
   oGPT,
   pQuery,
   pSkipQuery
   
):
   '''  '''
         
   # if (skip default query) <
   if (pSkipQuery):
      
      response = await oGPT.message(message = pQuery)
      await ctx.reply(response, ephemeral = True)
      
   # >
   
   popen('pmset displaysleepnow')
   exit(0)