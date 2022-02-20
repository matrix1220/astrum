#include <stdlib.h>
#include <stdio.h>

struct Vector
{
    int x;
    int y;
};

struct Direction
{
    char* name;
    struct Vector vector;
};

struct Direction directions[4] = {
    {"up", {0, -1} },
    {"right", {1, 0} },
    {"down", {0, 1} },
    {"left", {-1, 0} },
};

void vector_add(struct Vector * d, struct Vector s) {
    d->x += s.x;
    d->y += s.y;
}


int direction_direction_id(int direction_id) {
    direction_id = direction_id % 4;
    direction_id += 4;
    direction_id = direction_id % 4;
    return direction_id;
}


char* my_spaceship(char* param_1)
{
    struct Vector position = {0, 0};
    int direction_id = 0;
    char*p = param_1;
    while(*p!='\0') {
        switch(*p) {
            case 'L':
                direction_id -= 1;
                direction_id = direction_direction_id(direction_id);
                break;
            case 'R':
                direction_id += 1;
                direction_id = direction_direction_id(direction_id);
                break;
            case 'A':
                vector_add(&position, directions[direction_id].vector);
                break;
        }
        ++p;
    }
    char* result = (char*) malloc(100);
    sprintf(result, "{x: %d, y: %d, direction: '%s'}", position.x, position.y, directions[direction_id].name);

    return result;
}

// int main() {
//     printf("%s", my_spaceship("RAALALL"));
// }