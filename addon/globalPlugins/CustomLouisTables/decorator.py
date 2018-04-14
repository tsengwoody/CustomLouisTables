from functools import wraps
import os

def customTableList(func):
	'''
	Decorator tableList
	'''
	@wraps(func)
	def wrapper(tableList, inbuf, *args, **kwargs):

		custom_tableList = []
		for table in tableList:
			dirname = os.path.dirname(table)
			basename = os.path.basename(table)
			custom_table = os.path.join(dirname, 'custom_' +basename)
			if os.path.exists(custom_table):
				custom_tableList.append(custom_table)
			else:
				custom_tableList.append(table)
		result = func(custom_tableList, inbuf, *args, **kwargs)
		return result
	return wrapper
