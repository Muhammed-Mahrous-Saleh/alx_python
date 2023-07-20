def is_prime(number):
    if number == 1:
        return True
    elif number == 0:
        return False
    elif number < 0:
        number = number * -1
    for i in range(1, number):
        if number % i == 0:
            return True

    return False
