import time

def schedule_function(func: callable, when, args: list) -> None:
    print("calling function: " + str(func) + " at " + str(when))
    while time.time() < when:
        pass
    func(*args)

schedule_function(print, time.time()+10, ["haha"])
