function my_array_uniq(param_1) {
    let new_arr = []
    for (const val of param_1) {
        if (!new_arr.includes(val)) new_arr.push(val);
    }
    return new_arr;
};