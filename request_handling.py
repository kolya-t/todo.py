from json import dumps
from collections import OrderedDict
from flask import request, make_response
from insert_in_table import insert_new_quask
import time
from constant import *
from select_from_db import *
from update_field_in_table import update_is_done_quask


def handle_request_post():
	data_from_post = request.get_json()
	date_created = int(time.time() * 1000)
	if request.content_type != CONTENT_TYPE_JSON:
		return 'The type of the content in your request is clearly and utterly wrong, it have to be Json', 400
	elif type(data_from_post) is not dict:
		return 'The data in your request is absolutely wrong, it have to be a Json string', 400
	elif 'description' not in data_from_post:
		return 'There is no proper field to use in your request, description is absolute necessity', 400
	elif str(data_from_post['description']) == '':
		return 'The data in your request is absolutely wrong, it must not  be empty', 400
	else:
		insert_new_quask(date_created, data_from_post, 0)

		return dumps(OrderedDict(zip(get_column_names(), select_last_quask()))), 201, \
			{
			'Content-Type': CONTENT_TYPE_JSON,
			'location': LOCATION_HEADER + str(select_last_id())
			}


def handle_request_get():
	tasks_list = select_all_quasks()
	quask_line = []

	for quask in range(len(tasks_list)):
		quask_line.append(OrderedDict(zip(get_column_names(), tasks_list[quask])))

	return dumps(quask_line, indent=1), 200, {'Content-Type': CONTENT_TYPE_JSON}


def handle_request_get_id(quask_num):
	if str(select_quask_by_id(quask_num)) == 'None':
		return '', 404
	else:
		line_from_table = OrderedDict(zip(get_column_names(), select_quask_by_id(quask_num)))

		return dumps(line_from_table, indent=1), 200, {'Content-Type': CONTENT_TYPE_JSON}


def handle_request_patch_id(quask_num):
	data_from_patch = request.get_json()
	if str(select_quask_by_id(quask_num)) == 'None':
		return 'There appears to be no task with such ID', 404
	elif request.content_type != CONTENT_TYPE_JSON:
		return 'The type of the content in your request is clearly and utterly wrong, it have to be Json', 400
	elif type(data_from_patch) is not dict:
		return 'The data in your request is absolutely wrong, it have to be a Json string', 400
	elif 'is_done' not in data_from_patch:
		return 'There is no proper field to use in your request, is_done is absolute necessity', 400
	elif str(data_from_patch['is_done']) == '':
		return 'The data in your request is absolutely wrong, it must not be empty', 400
	elif int(bool(data_from_patch['is_done'])) == select_quask_by_id(quask_num)[3]:
		return '', 204
	elif int(bool(data_from_patch['is_done'])) != select_quask_by_id(quask_num)[3]:
		table_update = update_is_done_quask(int(bool(data_from_patch['is_done'])), quask_num)

		return table_update, 200


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
	response = make_response(handle_request_patch_id(quask_num))
	return response
