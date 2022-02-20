
char* reverse_string(char* param_1)
{
    char* p = param_1;
    while(*p!='\0') ++p;
    --p;
    int t = 0;
    char tmp;
    while(param_1 + t < p - t) {
        tmp = param_1[t];
        param_1[t] = p[-t];
        p[-t] = tmp;
        ++t;   
    }
    return param_1;
}