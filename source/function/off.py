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
   
   # if (skip default query) <
   if (pSkipQuery):
      
      response = await oGPT.message(message = pQuery)
      await ctx.reply(response, ephemeral = True)
      
   # >
   
   pCloser()
   popen('pmset displaysleepnow')
   exit(0)