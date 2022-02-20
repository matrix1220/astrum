#include <stdbool.h>
#ifndef STRUCT_INTEGER_ARRAY
#define STRUCT_INTEGER_ARRAY
typedef struct s_integer_array
{
    int size;
    int* array;
} integer_array;
#endif


bool my_is_sort(integer_array* param_1)
{
    int diff = 0;
    int tmp;
    for(int i=1; i < param_1->size; ++i) {
        tmp = param_1->array[i] - param_1->array[i-1];
        if(tmp==0) continue;
        if (diff==0) diff = tmp;
        if(tmp*diff<0) return false;
    }
    return true;
}