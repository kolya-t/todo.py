from json import dumps
from collections import OrderedDict
from flask import request
from Insert_in_table import insertion
import time
from Select_from_DB import selection, column_names

def request_handling_POST():
	
	Data_from_POST = request.get_json()

	Data_from_POST = Data_from_POST.values()

	date_created = int(time.time() * 1000)

	insertion(date_created, Data_from_POST, 0)

	return dumps(OrderedDict(zip(column_names(), selection()))), 201


def request_handling_GET():
	pass
