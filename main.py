# < Project RCoD by Alex & Jorydn > #


# import <
from source.bot import Bot

# >


# variables <
gRole = ''
gContact = ''

gTokenOpenai = ''
gTokenDiscord = ''

# >


# main <
if (__name__ == '__main__'):

   bot = Bot(
      
      pRole = gRole,
      pContact = gContact,
      pTokenOpenai = gTokenOpenai
      
   ).run(gTokenDiscord)
      
# >
