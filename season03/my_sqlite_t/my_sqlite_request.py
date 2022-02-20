class MySqliteRequest:
	def __init__(self):
		self._columns = []
		self._data = []

	def from_(db_name):
		data = open(db_name).read().split('\n')
		self._columns = data.pop(0).split(',')
		self._data = [x.split(',') for x in data]

	#def select(column_name) OR def select([column_name_a, column_name_b])

	def where(column_name, criteria):
		column_index = self._columns.find(column_name)
		
		if column_index==None:
			raise Exception("No such column")
			
		new_data = []

		for item in self._data:
			if item[column_index]==criteria:
				new_data.append(item)

		self._data = new_data
		#return self

	def join(column_on_db_a, filename_db_b, column_on_db_b):
		tmp = MySqliteRequest()
		tmp.from_(filename_db_b)
		appended = []
		for item in self._data:
			if item[column_index]==criteria:
				new_data.append(item)

	def order(order, column_name):
		pass
	def insert(table_name):
		pass
	def values(data):
		pass
	def update(table_name):
		pass
	def set(data):
		pass
	def delete():
		pass