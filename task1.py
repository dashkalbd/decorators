import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання: {end - start:.6f} секунд")
        return result
    return wrapper


def is_prime(number):
    if number < 2:
        return False
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True


@measure_time
def get_primes():
    primes = []
    for number in range(0, 1001):
        if is_prime(number):
            primes.append(number)
    return primes


result = get_primes()
print("Прості числа:", result)