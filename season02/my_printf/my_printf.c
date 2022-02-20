#include <stdarg.h>
#include <stdlib.h>
#include <unistd.h>

void my_put_char(char t) {
	write(1, &t, 1);
}

void my_put_str(char* param_1)
{
    char* p = param_1;
    while (*p!='\0') {
        my_put_char(*p);
        ++p;
    }
}

// https://stackoverflow.com/questions/34661426/writing-an-integer-to-stdout-in-text-form-using-only-write-to-do-writing
void my_put_decimal(int n) {
	if (n < 0) {
        my_put_char(0x2D);
        n = -n;
    }

    if (n > 9) {
        my_put_decimal(n/10);
    }

    my_put_char((n%10) + '0');
}
void my_put_udecimal(unsigned int n) {
    if (n > 9) {
        my_put_decimal(n/10);
    }

    my_put_char((n%10) + '0');
}
void my_put_octal(unsigned int n) {
    if (n > 7) {
        my_put_octal(n/7);
    }

    my_put_char((n%7) + '0');
}
void my_put_hexadecimal(unsigned int n) {
    if (n > 16) {
        my_put_hexadecimal(n/16);
    }
    int tmp = n % 16;
    if(tmp>9) my_put_char(tmp % 9 + 'A');
	else my_put_char(tmp + '0');
}

int my_printf(char * restrict format, ...) {
	va_list vl;
	va_start(vl, format);
	char * p = format;
	int tmp;
	while(1) {
		if(*p=='\0') break;
		if(*p=='%') {
			++p;
			tmp = va_arg(vl, int);
			switch(*p) {
				case 'd':
					my_put_decimal(tmp);
					break;
				case 'o':
					my_put_octal( (unsigned int) tmp);
					break;
				case 'u':
					my_put_udecimal( (unsigned int) tmp);
					break;
				case 'x':
					my_put_hexadecimal( (unsigned int) tmp);
					break;
				case 'c':
					my_put_char((char) tmp);
					break;
				case 's':
					my_put_str((char*) tmp);
					break;
				case 'p':
					my_put_hexadecimal( (unsigned int) tmp);
					break;
			}
		} else {
			write(1, p, 1);
		}

		++p;
	}
	
	va_end(vl);

}

// int main() {
// 	//my_printf("%c %s %d %o %u %x %p", 'a', "asdasd", 123, 123, 123, 123, 123);
// 	//my_printf("%o %u %x %p", 123, 123, 123, 123);
// }