from os import system
from time import sleep

#  ━┓
#   ┕━┓
#     ┕━┓
#       ┕━┓
#         ┕━
system('cls')
steps_nr = int(input("How many steps? "))
for steps in range (0,steps_nr):
    sleep(0.3)
    if steps ==0:
        print(" ━┓")
    elif steps == steps_nr - 1:
        print(" "*steps*2 + "┕━")  
    else:print(" "* steps*2+ "┕━┓")