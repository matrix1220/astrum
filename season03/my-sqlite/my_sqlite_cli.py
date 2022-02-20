from lark import Lark
from lark.visitors import Transformer

import argparse
import os.path

sql_grammar = '''
start           : command ";"?
command         : "SELECT" column_names "FROM" table_name join? where? order? -> select
                | "INSERT INTO" table_name "VALUES" "(" values ")"            -> insert
                | "UPDATE" table_name "SET" equations where?                  -> update
                | "DELETE FROM" table_name where?                             -> delete

join            : "JOIN" table_name "ON" column_name "=" column_name
where           : "WHERE" equation
order           : "ORDER" "BY" column_name          -> order_asc
                | "ORDER" "BY" column_name "ASC"    -> order_asc
                | "ORDER" "BY" column_name "DESC"   -> order_desc

equations       : equation ("," equation)*
equation        : column_name "=" value

column_names    : column_name ("," column_name)*
                | "*"
column_name     : value
table_name      : value

values          : value ("," value)*
value           : VAL1
                | "'" VAL2 "'"

VAL1            : /(\w|\d)+/
VAL2            : /[^\']+/
 

%import common.WS
%ignore WS
'''

sql_parser = Lark(sql_grammar, parser='lalr', debug=True)


#sql = "SELECT * FROM students ORDER BY id;"
# SELECT * FROM nba_player_data_copy;
# SELECT name FROM nba_player_data_copy WHERE year_start=1991;
# INSERT INTO nba_player_data_copy VALUES ('Alaa Abdelnaby',1992,1995,'F-C','6-10',240,'June 24, 1968','Duke University')
# UPDATE nba_player_data_copy SET year_end = 1890 WHERE name = 'Alaa Abdelnaby'
# UPDATE nba_player_data_copy SET name = asd WHERE year_end = 1890
# DELETE FROM nba_player_data_copy WHERE name = 'Mark Acres';
# DELETE FROM nba_player_data_copy WHERE year_end = 1890
#sql = "INSERT INTO students VALUES (John, john@johndoe.com, A, https://blog.johndoe.com);"
#sql = "UPDATE students SET email = 'jane@janedoe.com', blog = 'https://blog.janedoe.com' WHERE name = 'Jane';"
#sql = "DELETE FROM students WHERE name = 'John';"

#print()

class TransformSQL(Transformer):
    VAL1 = str
    VAL2 = str

    def start(self, args):
        return args[0]
    
    def select(self, args):
        return {
            "select": [args[0]] if len(args[0])>0 else [], #if len(args[0])>0 else None,
            "from": [args[1] + ".csv"],
            **{k:v for value in args[2:] for k, v in value.items()}
        }

    def insert(self, args):
        return {
            "insert": [db + '/' + args[0] + ".csv"],
            "values": [args[1]],
            #**{k:v for value in args[2:] for k, v in value.items()}
        }
    
    def update(self, args):
        return {
            "update": [db + '/' + args[0] + ".csv"],
            "set": [args[1]],
            **{k:v for value in args[2:] for k, v in value.items()}
        }
    
    def delete(self, args):
        return {
            "delete": [db + '/' + args[0] + ".csv"],
            **{k:v for value in args[1:] for k, v in value.items()}
        }
    
    def where(self, args):
        return {"where":args[0]}
    
    def join(self, args):
        return [args[1], args[0], args[2]]
    
    def order_asc(self, args):
        return {"order":["asc", args[0]]}
    def order_desc(self, args):
        return {"order":["desc", args[0]]}
    
    def equation(self, args):
        return args
    
    def equations(self, args):
        return {value[0]:value[1] for value in args}

    def table_name(self, args):
        return args[0]

    def column_names(self, args):
        return args

    def column_name(self, args):
        return args[0]

    def values(self, args):
        return args

    def value(self, args):
        return args[0]

#print(TransformSQL(visit_tokens=True).transform( sql_parser.parse(sql) ))

arg_parser = argparse.ArgumentParser(
    description='Command Line Interface (CLI) to MySqlite class.'
)
arg_parser.add_argument(
    'db', help='datebase directory name',
    nargs='?', const=1, default='.'
)
print("MySQLite version 0.1")

db = arg_parser.parse_args().db
if not os.path.exists(db):
    raise Exception(f"{db} does not exist")
if not os.path.isdir(db):
    db = os.path.dirname(db)

def sql_print(data):
    if not data: return
    for row in data:
        print(*[value for column_name, value in row.items()], sep='|')
            

from my_sqlite_request import modes
while True:
    command = input()
    if command == "quit": break
    transformed = TransformSQL(visit_tokens=True).transform( sql_parser.parse(command) )
    print(transformed)
    for mode in modes:
        if mode in transformed:
            sql_print(modes[mode](transformed))

