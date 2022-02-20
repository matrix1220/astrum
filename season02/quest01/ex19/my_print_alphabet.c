void my_putchar(char c) {
  write(1, &c, 1);
}

void my_print_alphabet()
{
    for(char i='a'; i<='z'; ++i) {
        my_putchar(i);
    }
    my_putchar('\n');
}