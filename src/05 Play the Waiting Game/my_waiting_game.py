import random
import time

def waiting_game() -> None:
    to_wait = random.randrange(1, 30)
    print("The target time is: " + str(to_wait) + " seconds")
    input()
    start = time.perf_counter()
    input()
    end = time.perf_counter()
    print("You were " + str(to_wait - (end-start)) + " seconds off")

waiting_game()