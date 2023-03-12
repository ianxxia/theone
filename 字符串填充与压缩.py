

str1 = 'chen xian is a good boy'
#以#将字符串填充到50个字符
print(str1.center(50, '#'))
#将字符串翻左边l填充/字符串放右边r
print(str1.ljust(50,'#'))
print(str1.rjust(50, '#'))

str='#############chen xian is a good boy##############'
# print(str.lstrip('#'))
# print(str.rstrip('#'))
# print(str.strip('#'))
#z:zero zfill用0填充到需要到长度
print(str.zfill(70))


