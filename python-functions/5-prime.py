def is_prime(number):
    if number == 1:
        return True
    for i in range(1, number):
        if number % i == 0:
            return True

    return False