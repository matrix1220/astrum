#include <stdlib.h>
int* my_range(int param_1, int param_2)
{
    if(param_1>=param_2) return 0;
    int length = param_2 - param_1;
    int *p = (int *) malloc(length*sizeof(int));
    for(int i=0; i<length; ++i) {
        p[i] = param_1 + i;
    }
    return p;
}