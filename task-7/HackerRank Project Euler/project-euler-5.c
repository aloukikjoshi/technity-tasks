#include <stdio.h>

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int lcm(int a, int b)
{
    return (a * b) / gcd(a, b);
}

int smallest_evenly_divisible(int N)
{
    int result = 1;
    for (int i = 1; i <= N; i++)
    {
        result = lcm(result, i);
    }
    return result;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++)
    {
        int N;
        scanf("%d", &N);
        int answer = smallest_evenly_divisible(N);
        printf("%d\n", answer);
    }
    return 0;
}