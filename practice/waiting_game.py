import random
from time import perf_counter

def waiting_game():
    target_time = random.randint(2, 4)
    input(f"Your target time is {target_time} seconds.\n ---Press Enter to Begin---")
    start_time = perf_counter()
    input(f"...Press Enter again after {target_time} seconds...")
    stop_time = perf_counter()
    elapsed_time = round(stop_time-start_time, 3)
    remainder = target_time - elapsed_time
    print(f"Elapsed time is {elapsed_time}")
    if remainder > 0: 
      print(f"{abs(remainder)} seconds too fast.")
    elif remainder < 0:
      print(f"{abs(remainder)} seconds too slow.")
    else:
       print("Spot on!")

waiting_game()

