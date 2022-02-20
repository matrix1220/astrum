function my_levenshtein(param_1, param_2) {
    if(param_1.length!=param_2.length) return -1;
    sum = 0;
    for(const key in param_1) {
        if (param_1[key]!=param_2[key]) sum++;
        //sum += param_2.charCodeAt(key) - param_1.charCodeAt(key)
    }
    return sum;
}