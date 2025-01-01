# Project RCoD by Alex Arbuckle #


# import <
from sys import argv
from time import sleep
from lxrbckl.screen import screen

from src.classes.roles import roles
from src.classes.microphone import mic
from src.classes.runtime import runtime

# >


# variables <
role = argv[1]
version = "3.0.0"

# >


if (__name__ == "__main__"):
   
   print(f"Project RCoD - Version: {version}")
   
   try:
      
      mic = mic()
      roles = roles()
      screen = screen()
      runtime = runtime()
      while (runtime.stop(screen) == False):
         
         facetimeAction = {
            
            "call" : roles.call,
            "answer" : roles.answer
            
         }[role]
         
         facetimeAction(screen)
         mic.mute(screen)
         sleep(60)
         
   except KeyboardInterrupt: exit(0)