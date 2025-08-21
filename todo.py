"""todoリスト管理スクリプト step1 課題2"""
import json
import os
if not os.path.exists('./CAWAL/basicassignment01/todo_save.json'):
    with open('./CAWAL/basicassignment01/todo_save.json', 'w', encoding='utf-8') as f:
        json.dump({}, f)

while 1:
    user_input=input(">").split()
    with open('./CAWAL/basicassignment01/todo_save.json', 'r', encoding="utf-8") as f:
        todo_dict = json.load(f)
    if user_input[0]=='list':
        if len(todo_dict)==0:
            print("(タスクなし)")
        for v in todo_dict.keys():
            print("[",v,"]",todo_dict[v])
    elif user_input[0]=='done':
        try:
            if int(user_input[1])<=len(todo_dict)\
                and int(user_input[1])>0:
                if len(todo_dict)>1:
                    for i in range(int(user_input[1]),len(todo_dict)):
                        todo_dict[str(i)]=todo_dict[str(i+1)]
                del todo_dict[str(len(todo_dict))]
                with open('./CAWAL/basicassignment01/todo_save.json', 'w', encoding="utf-8") as f:
                    json.dump(todo_dict, f)
        except ValueError:
            print("error:",user_input[0],">>",user_input[1],"<<\nexpected an index number")
    elif user_input[0]=='add':
        todo_dict[str(len(todo_dict)+1)]=user_input[1]
        with open('./CAWAL/basicassignment01/todo_save.json', 'w', encoding="utf-8") as f:
            json.dump(todo_dict, f)
    elif user_input[0]=='q':
        break
    else:
        print("error!")
