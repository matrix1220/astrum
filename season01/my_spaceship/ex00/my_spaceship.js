class Vector {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    add(another) {
        this.x += another.x;
        this.y += another.y;
    }
}

const directions = {
    up: new Vector(0, -1),
    right: new Vector(1, 0),
    down: new Vector(0, 1),
    left: new Vector(-1, 0),
};
const direction_names = Object.keys(directions);
const directions_length = direction_names.length;

class Direction {
    constructor(direction_index) {
        this.direction_index = direction_index;
        this._direction()
    }
    _direction() {
        if(this.direction_index<0) {
            this.direction_index += directions_length;
        }
        this.direction_index = this.direction_index % directions_length;
        this.direction_name = direction_names[this.direction_index];
        this.direction = directions[this.direction_name];
    }
    rotate_right() {
        this.direction_index += 1;
        this._direction()
    }
    rotate_left() {
        this.direction_index -= 1;
        this._direction()
    }
}
function my_spaceship(param_1) {
    let position = new Vector(0, 0);
    let direction = new Direction(0);
    for (const val of param_1) {
        switch (val) {
            case 'L':
                direction.rotate_left();
                break;
            case 'R':
                direction.rotate_right();
                break;
            case 'A':
                position.add(direction.direction);
                break;
            default:
                break;
        }
    }
    return `{x: ${position.x}, y: ${position.y}, direction: '${direction.direction_name}'}`
    //return {x:position.x, y:position.y, direction:direction.direction_name}
}