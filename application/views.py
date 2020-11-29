import json
import datetime
from aiohttp import web

from constants import WORKERS_FILE_NAME


JSONEncoderNoAsciiEnsure = json.JSONEncoder(ensure_ascii=False, indent=4)


def open_json_file():
    with open(WORKERS_FILE_NAME, 'r') as f:
        workers = f.read()
    return workers


def exact_match_dictionary(filter_parameter, filter_value, work_json):
    dictionary_to_post = {}
    count = 1
    for value in work_json.values():
        if value[filter_parameter] == filter_value:
            dictionary_to_post[count] = value
            count += 1
    return dictionary_to_post


def dictionary_by_age_of_workers(filter_value, work_json):
    dictionary_to_post = {}
    count = 1
    now = datetime.datetime.now()
    for value in work_json.values():
        date = value['date'].split('.')
        day_w = int(date[0]) - now.day
        month_w = now.month - int(date[1])
        year_w = now.year - int(date[2])
        if month_w < 0:
            age = year_w - 1
            if age > int(filter_value):
                dictionary_to_post[count] = value
                count += 1
        else:
            if day_w <= 0:
                age = year_w
                if age > int(filter_value):
                    dictionary_to_post[count] = value
                    count += 1
            else:
                age = year_w - 1
                if age > int(filter_value):
                    dictionary_to_post[count] = value
                    count += 1

    return dictionary_to_post


async def workers_get(request):
    workers_json = json.loads(open_json_file())
    return web.json_response(workers_json, dumps=JSONEncoderNoAsciiEnsure.encode)


async def workers_post(request):
    workers_json = json.loads(open_json_file())
    try:
        dict_to_response = {}
        if 'name' in request.query:
            dict_to_response = exact_match_dictionary('name', request.query['name'], workers_json)
        elif 'surname' in request.query:
            dict_to_response = exact_match_dictionary('surname', request.query['surname'], workers_json)
        elif 'patronymics' in request.query:
            dict_to_response = exact_match_dictionary('patronymics', request.query['patronymics'], workers_json)
        elif 'sex' in request.query:
            dict_to_response = exact_match_dictionary('sex', request.query['sex'], workers_json)
        elif 'age' in request.query:
            dict_to_response = dictionary_by_age_of_workers(request.query['age'], workers_json)
        return web.json_response(dict_to_response, dumps=JSONEncoderNoAsciiEnsure.encode)
    except Exception as e:
        text = str(e.args)
        return web.Response(text=text)


