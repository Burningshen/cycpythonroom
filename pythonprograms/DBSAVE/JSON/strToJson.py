import json

str='''
[{"name":"chenyichao","gender":"male","birthday":"1994314"},{"name":"guxiao","gender":"female","birthday":"19940116"}]'''

print(type(str))
data=json.loads(str)
print(data)
print(type(data))

print(data[0]['name'])
#这里用json.dumps方法是操作python对, 或者可以用json.dump(data,file,ensure_as# cii = False)


with open('json.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data,ensure_ascii = False))
