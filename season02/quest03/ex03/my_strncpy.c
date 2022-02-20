char* my_strncpy(char* param_1, char* param_2, int param_3)
{
    char* p = param_2;
    while(*p!='\0' && param_3>0) {
        param_1[p - param_2] = *p;
        ++p;
        --param_3;
    }
    while(param_3>0) {
        param_1[p - param_2] = '\0';
        ++p;
        --param_3;
    }
    return param_1;
}