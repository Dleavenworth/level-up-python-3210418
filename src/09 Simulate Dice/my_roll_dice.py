import random

def roll_dice(dice: list):
    iters = 1000000
    max_sum = 1
    for j in dice:
        max_sum += j

    #print(max_sum)
   
    count = [0]*max_sum
    for roll in range(0, iters):
        summ = 0
        for die in dice:
            summ += random.randint(1, die)
            count[summ] += 1
    print(count)
    for i in range(1, len(count)):
        print(str(i) + " occured with probability: " + str((count[i])/iters))

roll_dice([6, 6])