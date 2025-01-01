# Project RCoD by Alex Arbuckle #


# import <
from sys import argv
from time import sleep
from lxrbckl.screen import screen

from src.classes.roles import roles
from src.classes.runtime import runtime

# >


# variables <
delay = 5 # argv[0]
role = "call" # argv[1]
version = "3.0.0"

# >


if (__name__ == "__main__"):
   
   roles = roles()
   runtime = runtime()
   currentScreen = screen()
   while (True):
      
      # if (keep running) <
      # else (then stop running) <
      if (not runtime.checkForStop(currentScreen)):
         
         action = {
            
            "call" : roles.call,
            "answer" : roles.answer
            
         }[role]
         
         action(currentScreen)
         sleep(delay)
         
      else: runtime.stop()
      
      # >