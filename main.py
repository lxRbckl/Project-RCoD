# Project RCoD by Alex Arbuckle #


# import <
from sys import argv
from time import sleep
from lxrbckl.screen import screen

from src.classes.roles import roles
from src.classes.runtime import runtime
from src.classes.microphone import microphone

# >


# variables <
role = argv[1]
version = "3.0.0"

# >


if (__name__ == "__main__"):
   
   roles = roles()
   mic = microphone()
   runtime = runtime()
   currentScreen = screen()
   while (runtime.stop(currentScreen) == False):
      
      facetimeAction = {
         
         "call" : roles.call,
         "answer" : roles.answer
         
      }[role]
      
      facetimeAction(currentScreen)
      mic.mute(currentScreen)
      sleep(60)