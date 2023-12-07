import json
from json import JSONDecodeError
import g4f
import asyncio

def create_chat_completion(model, messages):
    return g4f.ChatCompletion.create(model=model, messages=messages)

async def get_response(messages):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, create_chat_completion, g4f.models.gpt_4, messages)
    return response




# def chat():
#     msg = input()
#     context = get_context('context.json')
#     context['messages'].append({'role': 'user', 'content': msg})
#     response = get_response(context['messages'])
#     context['messages'].append({'role': 'assistant', 'content': response})
#     write_to_json(context, 'context.json')

# if __name__ == '__main__':
#     chat()


# def chat():
#     msg = input()
#     response = get_response([{'role': 'user', 'content': msg}])
#     print(type(response))

# chat()
    
