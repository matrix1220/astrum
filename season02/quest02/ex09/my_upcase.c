#include <ctype.h>

char* my_upcase(char* param_1)
{
    char* p = param_1;
    while(*p!='\0') {
        if (islower(*p)) *p += 'A' - 'a';
        ++p;
    }
    return param_1;
}