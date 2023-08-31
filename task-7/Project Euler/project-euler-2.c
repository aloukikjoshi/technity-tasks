#include <stdio.h>

long long even_fibonacci_sum(long long limit) {
    long long a = 1, b = 2;
    long long even_sum = 0;
    while (b <= limit) {
        if (b % 2 == 0) {
            even_sum += b;
        }
        long long temp = b;
        b = a + b;
        a = temp;
    }
    return even_sum;
}

int main() {
    int T;
    scanf("%d", &T);
    
    for (int i = 0; i < T; i++) {
        long long N;
        scanf("%lld", &N);
        long long result = even_fibonacci_sum(N);
        printf("%lld\n", result);
    }
    return 0;
}