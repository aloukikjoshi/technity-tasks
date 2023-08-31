#include <stdio.h>
#include <math.h>

int main() {
    long long n, m, a;
    scanf("%lld %lld %lld", &n, &m, &a);
    long long flagstones_needed = (long long)ceil((double)n/a) * (long long)ceil((double)m/a);
    printf("%lld\n", flagstones_needed);
    return 0;
}
