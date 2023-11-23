# < Project RCoD by Alex & Jorydn > #


# import <
from bot import cBot

# >


# variables <
gRole = 'call'
gToken = ''

# >


# main <
if (__name__ == '__main__'):

   bot = cBot(
      
      pRole = gRole,
      pToken = gToken
      
   )

   bot.run(gToken)
   
# >