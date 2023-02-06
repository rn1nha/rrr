'''
JSON (JavaScript Object Notation)
    -딕셔너리랑 비슷하다
    -구조 { K : V }
'''
import json

# 첫번째 방법
dict_list =[
    {

        'name':'james',
        'age':20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {

        'name':'alice',
        'age':21,
        'spec': [
            168.5,
            60.5
        ]
    }
]
json_string = json.dumps(dict_list)

with open('dictlist.json', 'w') as file:
    file.write(json_string)
print('dictlist.json 파일이 생성되었습니다.')