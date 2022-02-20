require 'date'

def my_data_transform(param_1)
    p = param_1.split("\n")
    columns = p.shift.split(',')
    mail_index = 0
    age_index = 0
    order_at_index = 0
    columns.each_with_index do |value, index|
        if value=="Email"
            mail_index = index
        elsif value=="Age"
            age_index = index
        elsif value=="Order At"
            order_at_index = index
        end
    end
    rest = p.each_with_index do |value, key|
        t = value.split(',')
        t[mail_index] = /.*@(.*)/.match(t[mail_index])[1]

        case t[age_index].to_i
        when 1..20
            age_str = "1->20"
        when 21..40
            age_str = "21->40"
        when 41..65
            age_str = "41->65"
        when 66..99
            age_str = "66->99"
        end
        t[age_index] = age_str

        time = DateTime.parse(t[order_at_index], '%Y-%m-%d %H:%M:%S').strftime("%k").to_i
        case time
        when 6..11
            time_str = "morning"
        when 12..17
            time_str = "afternoon"
        when 18..23
            time_str = "afternoon"
        end
        t[order_at_index] = time_str

        p[key] = t.join(',')
    end
    rest.unshift(columns.join ",")
    return  rest
end
