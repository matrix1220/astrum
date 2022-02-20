// #include <stdio.h>

char* my_strstr(char* param_1, char* param_2)
{
    char* p = param_1;
    int f;
    while (1) {
        if (*p=='\0') return 0;
        f = 0;
        while(1) {
            if(p[f]!=param_2[f]) break;
            ++f;
            if(param_2[f]=='\0') return p;
        }
        ++p;
    }
    return 0;
}

// int main() {
//     printf("%s", my_strstr("mississippi", "issip"));
    
// }