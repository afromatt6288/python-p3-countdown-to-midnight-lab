# your code goes here!
import time

def countdown(sec):
    while sec > 0:
        print(f'{sec} SECOND(S)!')
        sec -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(sec):
    while sec > 0:
        print(f'{sec} SECOND(S)!')
        time.sleep(1)
        sec -= 1
    print("HAPPY NEW YEAR!")