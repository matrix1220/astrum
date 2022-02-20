require 'readline'

class MySqlite 
    def parse (buf)
        p buf
    end

    def run!
        while buf = Readline.readline("> ", true)
            instanse_of_request = parse(buf)
        end
    end 
end

msqcli = MySqlite.new
msqcli.run!