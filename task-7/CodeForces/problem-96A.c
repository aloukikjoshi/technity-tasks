#include <stdio.h>
#include <string.h>

int main()
{
    char s[101];
    scanf("%s", s);
    int consecutive_count = 1;
    char prev_player = s[0];
    for (int i = 1; i < strlen(s); i++)
    {
        if (s[i] == prev_player)
        {
            consecutive_count++;
            if (consecutive_count >= 7)
            {
                printf("YES\n");
                return 0;
            }
        }
        else
        {
            consecutive_count = 1;
            prev_player = s[i];
        }
    }
    printf("NO\n");
    return 0;
}