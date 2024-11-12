# < Project RCoD by Alex & Jorydn > #


# import <
from sys import argv
from source.bot import Bot

# >


# variables <
version = '1.1.0'

# >


# main <
if (__name__ == '__main__'):
   
   print(f'Version: {version}')
   print(f'token: {argv[7]} {type(argv[7])}')
   
   try:
      
      bot = Bot(
         
         pRole = argv[1],
         pQuery = argv[2],
         pContact = argv[3],
         pGuildId = argv[4],
         pSkipQuery = argv[5],
         pTokenOpenai = argv[6],
         pMuteAfterCall = argv[8]
         
      ).run(argv[7])
      
   except RuntimeError: pass

# >
