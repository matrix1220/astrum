char* my_strcpy(char* param_1, char* param_2)
{
    char* p = param_2;
    while(*p!='\0') {
        param_1[p - param_2] = *p;
        ++p;
    }
    return param_1;
}