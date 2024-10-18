def is_prime(func):
    def wrapper(*args):
        result1 = func(*args)
        if isinstance(result1, int):
            print('Простое')
        elif isinstance(result1, float):
            print('Составное')
        return result1
    return wrapper


@is_prime
def sum_three(*args):
    result_sum = 0
    for arg in args:
        result_sum += arg
    return result_sum

result = sum_three(2, 3, 6)
print(result)