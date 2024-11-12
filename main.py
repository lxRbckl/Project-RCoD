# < Project RCoD by Alex & Jorydn > #


# import <
from sys import argv
from source.bot import Bot

# >


# variables <
version = '2.1.16'

# >


# main <
if (__name__ == '__main__'):
   
   print(f'\nProject RCoD - Version: {version}\n')
         
   bot = Bot(
      
      pRole = argv[1],
      pQuery = argv[2],
      pContact = argv[3],
      pGuildId = argv[4],
      pSkipQuery = argv[5],
      pTokenOpenai = argv[6],
      pMuteAfterCall = argv[8]
      
   ).run(argv[7])
      
# >
