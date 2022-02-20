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