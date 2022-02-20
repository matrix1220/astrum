#include <ctype.h>

char* my_downcase(char* param_1)
{
    char* p = param_1;
    while(*p!='\0') {
        if (isupper(*p)) *p -= 'A' - 'a';
        ++p;
    }
    return param_1;
}