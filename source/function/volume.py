# import <
from os import popen

# >


async def fVolume(
   
   ctx,
   pRole,
   pLevel,
   pRoleValue

):
   '''  '''
   
   if (pRole == pRoleValue):
   
      popen(f'osascript -e "set volume output volume {pLevel}"')
      await ctx.reply(f'`Role:` `{pRoleValue}`\n`Volume:` `{pLevel}`')