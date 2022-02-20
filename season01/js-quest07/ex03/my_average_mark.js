function my_average_mark(param_1) {
    sum = 0;
    param_1.forEach(x => sum+=x['integer']);
    return Math.round(sum/param_1.length*10)/10; 
};