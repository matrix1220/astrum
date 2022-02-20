#include <stdio.h>

int my_putchar(char c) {
  return write(1, &c, 1);
}

void my_putstr(char* param_1)
{
    char* p = param_1;
    while (*p!='\0') {
        my_putchar(*p);
        ++p;
    }
}


void my_string_formatting(char* param_1, char* param_2, int param_3)
{
    char str[200];
    sprintf(str, "Hello, my name is %s %s, I'm %d.\n", param_1, param_2, param_3);
    my_putstr(str);
}
