
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    for i in range(1, 11):
        print(f'{i} -> {is_prime(i)}')