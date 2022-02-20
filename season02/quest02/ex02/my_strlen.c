
int my_strlen(const char *s) {
    const char* p = s;
    while (*p!='\0') ++p;
    return p - s;
}