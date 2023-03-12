import json
# 处理数据

# 去掉不合json规范的开头
f_us = open("D:/测试资料/美国.txt","r",encoding="UTF-8")
us_data = f_us.read()#美国全部内容
#去掉不合json规范的结尾
us_data = us_data.replace("jsonp_1629344292311_69436(","")

#json转python字典
us_data = us_data[:-2]
us_dict = json.loads(us_data)
print(type(us_data))
print(us_data)
#获取trend key
trend_data=us_dict['data'][0]['trend']
print(trend_data)#{'updateDate': ['2.22', '2.23', '2.24', '2

# 获取日期数据 用于x轴 取2020年到315下标结束
x_data = trend_data['updateDate'][:314]
print(x_data)

# 获取确认数据 用于y轴 取2020年到315下标结束
y_data = trend_data['list'][0]['data'][:314]
print(y_data)

# 生成图表