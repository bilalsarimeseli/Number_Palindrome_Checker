# Original is_prime function
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    # Check for divisibility up to half of n
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True

# Uncomment this section for a fair comparison
number_to_check = 123
result = is_prime(number_to_check)
print(f"{number_to_check} is prime: {result}")

#Find prime numbers in the range 100 to 151
start_range = 100
end_range = 151
prime_numbers = [num for num in range(start_range, end_range + 1) if is_prime(num)]
print(f"Prime numbers in the range {start_range} to {end_range}:")
print(prime_numbers)
print(f"Number of prime numbers: {len(prime_numbers)}")

# Optimized is_prime function
def is_prime_optimized(m):
    if m <= 1:
        return False
    elif m == 2:
        return True
    elif m % 2 == 0:
        return False
    
    # Check for divisibility up to the square root of n
    sqrt_m = int(m**0.5) + 1
    for j in range(3, sqrt_m, 2):
        if m % j == 0:
            return False
    return True

# Compare efficiency using timeit
import timeit
number_to_check = 9973  # A random prime number for testing

original_time = timeit.timeit(lambda: is_prime(number_to_check), number=10000)
optimized_time = timeit.timeit(lambda: is_prime_optimized(number_to_check), number=10000)

print(f"Original is_prime time: {original_time:.6f} seconds")
print(f"Optimized is_prime time: {optimized_time:.6f} seconds")
