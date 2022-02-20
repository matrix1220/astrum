int my_string_index(char* param_1, char param_2)
{
    char* p = param_1;
    while(*p!=param_2) {
        if(*p=='\0') return -1;
        ++p;
    }
    return p - param_1;
}