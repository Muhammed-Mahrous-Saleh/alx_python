def is_prime(number):
    print(number)
    if number == 1:
        return False
    elif number <= 0:
        return False
    for i in range(1, number):
        if number % i == 0:
            return True

    return False
