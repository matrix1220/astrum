int my_strcmp(char* param_1, char* param_2)
{
    int t = 0;
    while(param_1[t]==param_2[t]) {
        if (param_1[t]=='\0') return 0;
        ++t;
    }
    if(param_1[t]<param_2[t]) return -1;
    if(param_1[t]>param_2[t]) return 1;
    return 0;
}