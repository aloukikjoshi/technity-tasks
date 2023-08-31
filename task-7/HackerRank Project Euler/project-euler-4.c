#include <stdio.h>

int is_palindrome(int n)
{
    int original = n;
    int reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return original == reversed;
}

int largest_palindrome_below_n(int N)
{
    for (int num = N - 1; num >= 101101; num--)
    {
        if (is_palindrome(num))
        {
            for (int divisor = 999; divisor >= 100; divisor--)
            {
                if (num % divisor == 0 && num / divisor >= 100 && num / divisor <= 999)
                {
                    return num;
                }
            }
        }
    }
    return -1;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        int N;
        scanf("%d", &N);
        int result = largest_palindrome_below_n(N);
        printf("%d\n", result);
    }
    return 0;
}