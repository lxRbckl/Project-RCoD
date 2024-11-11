# < Project RCoD by Alex & Jorydn > #


# import <
from source.bot import Bot

# >


# variables <
gRole = ''
gContact = ''

gTokenOpenai = ''
gTokenDiscord = ''

version = '1.0.1'
# >


# main <
if (__name__ == '__main__'):

   print(f'Version: {version}')
   
   try:
      
      bot = Bot(
         
         pRole = gRole,
         pContact = gContact,
         pTokenOpenai = gTokenOpenai
         
      ).run(gTokenDiscord)
      
   except RuntimeError: pass
      
# >
