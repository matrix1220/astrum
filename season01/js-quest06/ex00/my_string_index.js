function my_string_index(param_1, param_2) {
    for (const index in param_1) {
        if (param_1[index]==param_2) return index;
    }
    return -1;
};