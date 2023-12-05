import json
from json import JSONDecodeError
import g4f

def get_response(messages):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=messages,
)
    return response



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


# def chat():
#     msg = input()
#     context = get_context('context.json')
#     context['messages'].append({'role': 'user', 'content': msg})
#     response = get_response(context['messages'])
#     context['messages'].append({'role': 'assistant', 'content': response})
#     write_to_json(context, 'context.json')

# if __name__ == '__main__':
#     chat()
