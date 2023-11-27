# < Project RCoD by Alex & Jorydn > #


# import <
from bot import Bot

# >


# variables <
gRole = 'call'
gContact = 'NoahsBroWitch'
gToken = 'test'

# >


# main <
if (__name__ == '__main__'):

   bot = Bot(
      
      pRole = gRole,
      pContact = gContact
      
   ).run(gToken)

   # bot.run(gToken)
   
   # python3 -c "from bot import Bot; Bot(pRole = 'call', pContact = '12').run('token');"
   # python3 -c 
   
# >