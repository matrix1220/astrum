#include <stdlib.h>

char* my_strdup(char* param_1)
{
    char*p = param_1;
    while(*p!='\0') ++p;
    char* t = (char*) malloc(p - param_1 + 1);
    p = param_1;
    while(*p!='\0') {
        t[p-param_1] = *p;
        ++p;
    }
    return t;
}