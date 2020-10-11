from json import dumps
from collections import OrderedDict
from flask import request, make_response
from insert_in_table import insert_new_quask
import time
from select_from_DB import *


def handle_request_post():
	data_from_post = request.get_json()
	data_from_post = data_from_post['description']
	date_created = int(time.time() * 1000)
	insert_new_quask(date_created, data_from_post, 0)

	return dumps(OrderedDict(zip(get_column_names(), select_last_quask()))), 201


def handle_request_get():
	tasks_list = select_all_quasks()
	quask_line = []

	for quask in range(len(tasks_list)):
		quask_line.append(OrderedDict(zip(get_column_names(), tasks_list[quask])))

	return dumps(quask_line, indent=1), 201  # maybe something else? not 201?


def handle_request_get_id(quask_num):
	if str(select_quask_by_id(quask_num)) == 'None':
		return '', 404
	else:
		line_from_table = OrderedDict(zip(get_column_names(), select_quask_by_id(quask_num)))

		return dumps(line_from_table, indent=1), 201  # maybe something else? not 201?


def create_post_response():
	response = make_response(handle_request_post())
	response.headers['location'] = 'http://localhost:5000/tasks/' + str(select_last_id())
	response.headers['Content-Type'] = 'application/json'

	return response


def create_get_response():
	response = make_response(handle_request_get())
	response.headers['Content-Type'] = 'application/json'

	return response


def create_get_id_response(quask_num):
	response = make_response(handle_request_get_id(quask_num))
	response.headers['Content-Type'] = 'application/json'

	return response
