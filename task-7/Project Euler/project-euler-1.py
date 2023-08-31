def sum_of_multiples(n):
    n -= 1
    num_multiples_of_3 = n // 3
    num_multiples_of_5 = n // 5
    num_multiples_of_15 = n // 15
    
    sum_of_3 = (num_multiples_of_3 * (num_multiples_of_3 + 1)) // 2 * 3
    sum_of_5 = (num_multiples_of_5 * (num_multiples_of_5 + 1)) // 2 * 5
    sum_of_15 = (num_multiples_of_15 * (num_multiples_of_15 + 1)) // 2 * 15
    
    return sum_of_3 + sum_of_5 - sum_of_15

T = int(input())

for _ in range(T):
    N = int(input())
    result = sum_of_multiples(N)
    print(result)