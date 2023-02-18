from time import sleep
for n in range(1,11):
    sleep(0.2)
    print (n)
if n == 10:
    print("Now Reverse")
for n in reversed(range(1,11)):
    sleep(0.2)
    print (n)
if n == 1:
    print("Finish")