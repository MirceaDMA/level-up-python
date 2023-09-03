from random import randint
from collections import Counter

# My Solution
def roll_dice(*dice, num_trials=1_000_000):
    roll_sum = []
    for _ in range(num_trials):
        roll_sum += [sum(randint(1, sides) for sides in dice)]
    counter = Counter(roll_sum)
    
    # print(counter)
    print("\nOUTCOME\tPROBABILITY")
    for outcome in range(len(dice), sum(dice) + 1):
        print(f"{outcome}\t{counter[outcome]*100/num_trials :0.2f}%")


if __name__ == "__main__":
    roll_dice(6, 6)
