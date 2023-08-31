import math

def largest_prime_factor(n):
    max_prime = -1

    while n % 2 == 0:
        max_prime = 2
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i


    if n > 2:
        max_prime = n

    return max_prime

t = int(input())

for _ in range(t):
    n = int(input())
    result = largest_prime_factor(n)
    print(result)