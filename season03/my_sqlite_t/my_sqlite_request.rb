
require 'csv'

class MySqliteRequest
    def initialize
        @type_of_request = :none
        @select_columns  =  []
        @table_name      =  nil
        @where_parama    = []
        @order           = :asc  
        @insert_attributes = {}
    end

    def from(table_name)
        @table_name = table_name
        self
    end

    def select(columns)
        if (columns.is_a?(Array))
            @select_columns += columns.collect { |elem| elem.to_s }
        else
            @select_columns << columns.to_s
        end
        self._setTypeOfRequest(:select)
        self
    end

    def where(column_name, criteria)
        @where_parama <<[column_name, criteria]
        self
    end

    def join(column_on_db_a, filename_db_b, column_on_db_b)
        self
    end

    def order(order, column_name)
        self

    end


    def insert(table_name)
        @table_name = table_name
        self._setTypeOfRequest(:insert)
        self
    end

    def values(data)
        if(@type_of_request == :insert)
            @insert_attributes = data
        else
                raise "Wrong"
        end
        self
    end

    def update(table_name)
        @table_name = table_name
        self._setTypeOfRequest(:update)
        self
    end

    def set(data)
        self
    end

    def delete
        self._setTypeOfRequest(:delete)
        self
    end

    def  print_select_type
        puts "Select Attributes #{@select_columns}"
        puts "Where Attributes #{@where_parama}"
    end

    def  print_insert_type
        puts "insert Attributes #{@insert_attributes}"
    end

    def print 
        puts "Type of request: #{@type_of_request}"
        puts "Table name: #{@table_name}"
        if (@type_of_request == :select)
            print_select_type
        elsif (@type_of_request == :insert)
            print_insert_type
        end 

    end

    def run
        print
        if (@type_of_request == :select)
            _run_select
        elsif (@type_of_request == :insert)
            _run_insert
        end        
    end 

    def _setTypeOfRequest (new_type)
        if (@type_of_request == :none or @type_of_request == new_type)
            @type_of_request = new_type
        else
            raise "Invalid: type of request already set to #{type_of_request} (new type =>#{new_type}"
        end
    end

    


    def _run_select
        result =[]
        CSV.parse(File.read(@table_name), headers:true).each do |row|
            @where_parama.each do |where_attribute|
                if row [where_attribute[0]] == where_attribute[1]
                    result << row.to_hash.slice(* @select_columns)
                end
            end
        end
        result
    end

    def _run_insert
        File.open(@table_name, 'a') do |f|
            f.puts @insert_attributes.values.join(',')
        end
    end

end

def _main()
=begin
    request = MySqliteRequest.new
    request = request.from('nba_player_data.csv')
    request = request.select('college')
    request = request.where('year_start', '1991')
    p request.run
=end
    request = MySqliteRequest.new
    request = request.insert('nba_player_data_copy.csv')
    request = request.values({"name" => "Alex Acker", "year_start" => "2006", "year_end" => "2009", "position" => "G", "height" => "6-5", "weight" => "185", "birth_date" => "January 21, 1983", "college" => "Pepperdine University"})
    request.run
end

_main()