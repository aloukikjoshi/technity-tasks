import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_evenly_divisible(N):
    result = 1
    for i in range(1, N + 1):
        result = lcm(result, i)
    return result

T = int(input())

for _ in range(T):
    N = int(input())
    answer = smallest_evenly_divisible(N)
    print(answer)