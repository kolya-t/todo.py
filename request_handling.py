# test pycharm commit
from json import dumps
from collections import OrderedDict
from flask import request, make_response
from insert_in_table import insert_new_quask
import time
from select_from_db import *
from update_field_in_table import update_is_done_quask


def handle_request_post():
	data_from_post = request.get_json()
	data_from_post = data_from_post['description']
	date_created = int(time.time() * 1000)
	insert_new_quask(date_created, data_from_post, 0)

	return dumps(OrderedDict(zip(get_column_names(), select_last_quask()))), 201, \
		{
			'Content-Type': 'application/json',
			'location': 'http://localhost:5000/tasks/' + str(select_last_id())
		}


def handle_request_get():
	tasks_list = select_all_quasks()
	quask_line = []

	for quask in range(len(tasks_list)):
		quask_line.append(OrderedDict(zip(get_column_names(), tasks_list[quask])))

	return dumps(quask_line, indent=1), 200, {'Content-Type': 'application/json'}


def handle_request_get_id(quask_num):
	if str(select_quask_by_id(quask_num)) == 'None':
		return '', 404
	else:
		line_from_table = OrderedDict(zip(get_column_names(), select_quask_by_id(quask_num)))

		return dumps(line_from_table, indent=1), 200, {'Content-Type': 'application/json'}


def handle_request_patch_id(quask_num):
	print(int(bool(request.get_json()['is_done'])))
	print(select_quask_by_id(quask_num)[3])
	if str(select_quask_by_id(quask_num)) == 'None':
		return '', 404
	elif request.content_type != 'application/json':
		return '', 400
	elif 'is_done' not in request.get_json():
		return '', 400
	elif int(bool(request.get_json()['is_done'])) == select_quask_by_id(quask_num)[3]:
		return '', 204
	elif int(bool(request.get_json()['is_done'])) != select_quask_by_id(quask_num)[3]:
		table_update = update_is_done_quask(int(bool(request.get_json()['is_done'])), quask_num)

		return table_update, 200
	select_quask_by_id(quask_num)
	data_from_post = request.get_json()['is_done']
	return


def create_post_response():
	response = make_response(handle_request_post())
	return response


def create_get_response():
	response = make_response(handle_request_get())
	return response


def create_get_id_response(quask_num):
	response = make_response(handle_request_get_id(quask_num))
	return response

def create_patch_id_response(quask_num):
	response=make_response(handle_request_patch_id(quask_num))
	return response