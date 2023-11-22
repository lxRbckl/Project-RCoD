# < Project RCoD by Alex & Jorydn > #


# import <
from bot import cBot

# >


# variables <
gRole = 'caller'
gToken = ''

# >


# main <
if (__name__ == '__main__'):
   
   bot = cBot(
      
      role = gRole,
      token = gToken
      
   )
   bot.run()

# >