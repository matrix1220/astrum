def my_data_process(param_1)
    columns = param_1.shift.split(',')
    result = {}
    columns.each {|t| result[t] = {}}
    param_1.each do |value|
        value.split(',').each_with_index do |inner_value, key|
            result[columns[key]][inner_value] = 0 if result[columns[key]].key?(inner_value)
            result[columns[key]][inner_value] += 1
        end
    end
    result
end

my_data_process("")