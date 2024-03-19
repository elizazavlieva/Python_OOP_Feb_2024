def get_primes(my_list):
    for number in my_list:
        if number <= 1:
            continue

        # for div in range(2, math.isqrt(num) + 1):
        for div in range(2, int(number**0.5) + 1):
            if number % div == 0:
                break
        else:
            yield number


""" TEST """
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
