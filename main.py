# < Project RCoD by Alex & Jorydn > #


# import <
import sys
from source.bot import Bot

# >


# variables <
version = '1.1.0'

# >


# main <
if (__name__ == '__main__'):
   
   print(f'Version: {version}')
   
   try:
      
      bot = Bot(
         
         pRole = sys.argv(1),
         pQuery = sys.argv(2),
         pGuildId = sys.argv(3),
         pContact = sys.argv(4),
         pSkipQuery = sys.argv(5),
         pTokenOpenai = sys.argv(6),
         pMuteAfterCall = sys.argv(7)
         
      ).run(sys.argv(8))
      
   except RuntimeError: pass
      
# >
