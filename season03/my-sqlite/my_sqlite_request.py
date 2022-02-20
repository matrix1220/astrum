import csv

class Table:
	def __init__(self, table_name = None):
		self.columns = []
		self.rows = []
		self.table_name = table_name
		if table_name:
			self.read(table_name)

	def read(self, table_name = None):
		if not table_name:
			table_name = self.table_name

		with open(table_name, 'r') as csvfile:
			data = list(csv.reader(csvfile))
		
		self.columns = data[0]
		self.rows = data[1:]
	
	def write(self, table_name = None):
		if not table_name:
			table_name = self.table_name

		with open(table_name, 'w') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerows([self.columns, *self.rows])
	
	def show(self):
		return [
			{column_name:value for column_name, value in zip(self.columns, row)}
			for row in self.rows
		]


def select(input_):
	#if "from" not in input_: return
	table = Table(input_['from'][0])
	
	if "join" in input_:
		column_name = input_['join'][0]
		column_index = table.columns.index(column_name)

		new_table_name = input_['join'][1]
		new_table = Table(new_table_name)

		generated_table = Table()
		generated_table.columns = [*table.columns, *new_table.columns]
		
		new_column_name = input_['join'][2]
		new_column_index = table.columns.index(new_column_name)

		for row in table.rows:
			for new_row in new_table.rows:
				if row[column_index]==new_row[new_column_index]:
					generated_table.rows.append([*row, *new_row])
		
		table = generated_table
	
	if "where" in input_:
		column_name = input_['where'][0]
		criteria = input_['where'][1]

		column_index = table.columns.index(column_name)
			
		new_rows = []
		for row in table.rows:
			if row[column_index]==criteria:
				new_rows.append(row)

		table.rows = new_rows
	
	if "order" in input_:
		order = input_['order'][0]
		column_name = input_['order'][1]
		column_index = table.columns.index(column_name)

		table.rows = list(sorted(table.rows, key=lambda row: row[column_index], reverse=order=='desc'))

	if "select" in input_ and len(input_['select'])>0:
		if type(input_['select'][0])==str:
			columns = [input_['select'][0]]
		elif type(input_['select'][0])==list:
			columns = input_['select'][0]
		else:
			raise Exception("please do not input what ever you want")
		
		column_indicies = []
		for column_name in columns:
			column_index = table.columns.index(column_name)
			column_indicies.append(column_index)

		new_rows = []
		for row in table.rows:
			new_row = []
			for column_index in column_indicies:
				new_row.append(row[column_index])
			new_rows.append(new_row)
		table.rows = new_rows
	
	return table.show()

def insert(input_):
	table = Table(input_['insert'][0])

	if "values" not in input_: raise Exception("not good")
	values = input_['values'][0]

	if type(values)==list:
		table.rows.append(values)
	elif type(values)==dict:
		new_row = []
		for column_name in table.columns:
			new_row.append(values[column_name] or '')
		table.rows.append(new_row)

	table.write()

def update(input_):
	table = Table(input_['update'][0])
	if "set" not in input_: raise Exception("not good")
	set = input_['set'][0]

	column_indicies = []
	values = []
	for column_name, value in input_['set'][0].items():
		column_index = table.columns.index(column_name)
		column_indicies.append(column_index)
		values.append(value)

	if "where" in input_:
		column_name = input_['where'][0]
		criteria = input_['where'][1]

		column_index = table.columns.index(column_name)
			
		for row in table.rows:
			if row[column_index]==criteria:
				for column_index_, value in zip(column_indicies, values):
					row[column_index_] = value
	else:
		for row in table.rows:
			for column_index, value in zip(column_indicies, values):
				row[column_index] = value
			
	table.write()

def delete(input_):
	table = Table(input_['delete'][0])

	if "where" in input_:
		column_name = input_['where'][0]
		criteria = input_['where'][1]

		column_index = table.columns.index(column_name)
			
		for i, row in enumerate(table.rows):
			if row[column_index]==criteria:
				table.rows.pop(i)
	else:
		table.rows = []
	
	table.write()


modes = {
	"from": select,
	"insert": insert,
	"update": update,
	"delete": delete
}

class MySqliteRequest:
	keywords = [
		"from", "select", "join",
		"insert", "values",
		"update", "set",
		"delete",
		"where", "order"
	]
	def __init__(self, table_name=None):
		self._input = {}
		if table_name:
			getattr(self, "from")(table_name + ".csv")

	def __getattr__(self, key):
		if key not in self.keywords: return
		def temporary_function(*args):
			self._input[key] = args
			return self
		return temporary_function

	def run(self):
		for mode in modes:
			if mode in self._input:
				return modes[mode](self._input)

# # Test 1
# my_sqlite_request = MySqliteRequest()
# getattr(my_sqlite_request, "from")("nba_player_data.csv")
# my_sqlite_request.select('name')
# my_sqlite_request.where('year_start', "1947")
# print(my_sqlite_request.run())

# print(MySqliteRequest('nba_player_data').select('name').where('year_start', '1947').run())

# Test 2
# my_sqlite_request = MySqliteRequest()
# my_sqlite_request.insert("nba_player_data_copy.csv")
# my_sqlite_request.values([
# 	'Alaa Abdelnaby', '1991', '1995', 'F-C', '6-10', '240',
# 	"June 24, 1968",'Duke University'
# ])
# print(my_sqlite_request.run())

# # Test 3
# my_sqlite_request = MySqliteRequest()
# my_sqlite_request.update("nba_player_data_copy.csv")
# my_sqlite_request.set({"year_start":"123123"})
# print(my_sqlite_request.run())

# # Test 3
# my_sqlite_request = MySqliteRequest()
# my_sqlite_request.delete("nba_player_data_copy.csv")
# print(my_sqlite_request.run())