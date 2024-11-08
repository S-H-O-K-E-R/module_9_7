def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result - 1):
            if result % i == 0:
                print('Составное')
                return result
            else:
                print('Простое')
                return result
    return wrapper

@is_prime
def sum_three(first, second, third):
    return first + second + third

result = sum_three(2, 3, 6)
print(result)
