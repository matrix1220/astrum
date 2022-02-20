def my_is_sort(param_1)
    if param_1 == param_1.sort {|a, b| a <=> b }
        return true
    elsif param_1 == param_1.sort {|a, b| b <=> a}
        return true
    end
    return false
end