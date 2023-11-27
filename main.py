# < Project RCoD by Alex & Jorydn > #


# import <
from bot import Bot

# >


# variables <
gRole = 'call'
gContact = 'NoahsBroWitch'
gToken = ''

# >


# main <
if (__name__ == '__main__'):

   bot = Bot(
      
      pRole = gRole,
      pToken = gToken,
      pContact = gContact
      
   )

   bot.run(gToken)
   
# >