void my_putchar(char c) {
  write(1, &c, 1);
}

void my_print_reverse_alphabet()
{
    for(char i='z'; i>='a'; --i) {
        my_putchar(i);
    }
    my_putchar('\n');
}