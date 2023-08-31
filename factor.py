def get_prime_factors(chosen_number):
    num_list = []
    for num in range(2, chosen_number+1):
        while chosen_number % num == 0:
            chosen_number /= num
            num_list.append(num)

    return num_list
