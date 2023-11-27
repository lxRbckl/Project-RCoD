# < Project RCoD by Alex & Jorydn > #


# import <
from source.bot import Bot

# >


# variables <
gRole = 'call'
gContact = 'NoahsBroWitch'
gTokenOpenai = ''
gTokenDiscord = ''

# >


# main <
if (__name__ == '__main__'):

   bot = Bot(
      
      pRole = gRole,
      pContact = gContact,
      pTokenOpenai = gTokenOpenai
      
   )
   
   bot.run(gTokenDiscord)
   
   # python3 -c "from bot import Bot; Bot(pRole = 'call', pContact = '12').run('token');"
   
# >