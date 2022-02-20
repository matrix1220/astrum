#include<stdio.h>

int main(int ac, char** av) {
	if (av==0) return 0;
	int map[256];
	for(int i=0; i<256; ++i) {
		map[i] = 0;
	}
	for(int i=1; i<ac; ++i) {
		if (av[i]==0) continue;
		char* p = av[i] + 1;
		while(*(p+1)!='\0') {
			++map[*p];
			++p;
		}
	}
	
	for(int i=0; i<256; ++i) {
		if(map[i]>0) printf("%c:%d\n", i, map[i]);
		
	}
}