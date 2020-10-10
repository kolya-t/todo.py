from json import dumps
from collections import OrderedDict
from flask import request, make_response
from Insert_in_table import insert_new_quask
import time
from Select_from_DB import select_last_quask, select_all_quasks, select_last_id, get_column_names


def handle_request_post():
	data_from_post = request.get_json()
	data_from_post = data_from_post['description']
	date_created = int(time.time() * 1000)
	insert_new_quask(date_created, data_from_post, 0)

	return dumps(OrderedDict(zip(get_column_names(), select_last_quask()))), 201


def handle_request_get():
	pass


def create_post_response():
	response = make_response(handle_request_post())
	response.headers['location'] = 'http://localhost:5000/tasks/' + str(select_last_id())

	return response


def create_get_response():
	tasks_list = select_all_quasks()
	quask_line = []

	for quask in range(len(tasks_list)):
		quask_line.append(OrderedDict(zip(get_column_names(), tasks_list[quask])))

	return dumps(quask_line, indent=1)
