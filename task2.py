import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time:.6f} секунд")
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
def get_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes


start = int(input("Початок діапазону: "))
end = int(input("Кінець діапазону: "))

result = get_primes(start, end)
print("Прості числа:", result)