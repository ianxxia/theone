#
import json

#准备符合格式josn格式要求的python数据
#将列表 转换为json
data = [{"name":"老王","age":"16"},
        {"name":"张三","age":"20"}]
#通过以下方法把python数据转化为json数据
json_data = json.dumps(data)#[{"name": "\u8001\u738b", "age": "16"}, {"name": "\u5f20\u4e09", "age": "20"}]
json_datacn = json.dumps(data,ensure_ascii=False)#[{"name": "\u8001\u738b", "age": "16"}, {"name": "\u5f20\u4e09", "age": "20"}]
#ensure_ascii 不使用ascii转换 输出中文
print(type(json_data))#<class 'str'>
print(json_data)
print(json_datacn)#[{"name": "老王", "age": "16"}, {"name": "张三", "age": "20"}]

#将字典转换为json
d = {"name":"周杰伦","addr":"台湾"}
json_dict = json.dumps(d,ensure_ascii=False)
print(json_data)
print(json_dict)#{"name": "周杰伦", "addr": "台湾"}

#通过方法把json转化为python数据
s = '[{"name":"老王","age":"16"},{"name":"张三","age":"20"}]'
l = json.loads(s)
print(type(l))#<class 'list'>
print(l)#[{'name': '老王', 'age': '16'}, {'name': '张三', 'age': '20'}]

s = '{"name":"周杰伦","addr":"台湾"}'
d = json.loads(s)
print(type(d))#<class 'dict'>
print(d)#{'name': '周杰伦', 'addr': '台湾'}
