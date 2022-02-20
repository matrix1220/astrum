#include <stdlib.h>

#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY
typedef struct s_string_array
{
    int size;
    char** array;
} string_array;
#endif

int length(char* s) {
    char*p=s;
    while(*p!='\0') ++p;
    return p-s;
}
char* copy(char* s, char* d) {
    while(*s!='\0') {
        *d = *s;
        ++s;
        ++d;
    }
    return d;
}

char* my_join(string_array* param_1, char* param_2)
{
    int delimiter_length = length(param_2);
    int final_length = (param_1->size-1) * delimiter_length;
    for(int i=0; i<param_1->size; ++i) {
        final_length += length(param_1->array[i]);
    }
    char* final_str = (char*) malloc(final_length);
    char*p = final_str;
    for(int i=0; i<param_1->size; ++i) {
        p = copy(param_1->array[i], p);
        if(i<param_1->size-1) {
            p = copy(param_2, p);
        }
    }
    return final_str;
}