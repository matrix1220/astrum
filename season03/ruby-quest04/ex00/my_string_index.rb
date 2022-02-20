def my_string_index(param_1, param_2)
    if not param_1.include? param_2
        return -1
    end
    return param_1.index(param_2)
end