char* my_strrchr(char* param_1, char param_2)
{
    char* p = param_1;
    while(*p!='\0') ++p;
    while(*p!=param_2) {
        if (*p==*param_1) return 0;
        --p;
    }
    return p;
}