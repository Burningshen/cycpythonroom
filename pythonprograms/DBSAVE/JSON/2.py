import json

with open('json.json','r') as file:
    str=file.read()
    data=json.loads(str)
    print(data[1]['name'])
