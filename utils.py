import json
from json import JSONDecodeError

def is_valid_content_length(content:list):
    return False if len(str(content)) >= 3500 else True

def get_context(file_name: str):
    try: 
        with open(file_name, 'r') as file:
            try:
                context = json.load(file)
            except JSONDecodeError as e:
                print('JSONDecodeError ', e)
                context = {'messages': []}
    except FileNotFoundError as ex:
        print('FileNotFoundError ', ex)
        context = {'messages': []}
    return context

def write_to_json(content: dict, filename: str):
    with open(filename, 'w') as file:
        json.dump(content, file, ensure_ascii=False, indent=4)
