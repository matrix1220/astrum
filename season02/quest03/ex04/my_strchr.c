char* my_strchr(char* param_1, char param_2)
{
    char* p = param_1;
    while(*p!=param_2) {
        if (*p=='\0') return 0;
        ++p;
    }
    return p;
}