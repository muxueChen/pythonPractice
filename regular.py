# 正则表达式

import re

# re.match 函数尝试从字符串的起始位置匹配一个模式，如果不是起始位置汽配城东的话，match()返回就会返回 none。
# 函数语法
# re.march(pattern, string, flags=0)
# pattern 匹配的正则表达式, string 要匹配的字符串, flags 标志位，用于控制支付穿的匹配方式，如：是否区分大小写，多行匹配等等。
# 匹配成功的话返回一个对象，否则返回 none
# try:
#     print(re.match("www", 'www.runoob.com').span())
#     print(re.match("com", 'www.runoob.com').span())
# except AttributeError: 
#     print('>>>>>错误')
# else:
#     print('>>>>>正确')
# finally:
#     pass

# line = "Cats are smarter than dogs"
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))

# else:
#    print ("No match!!")

# re.search 方法
# re.search 扫描整个字符串并返回第一个成功的匹配
# 函数语法： re.search(pattern, string, flags=0)
# pattern 匹配的正则表达式, string 要匹配的字符串, flags 标志位，用于控制支付穿的匹配方式，如：是否区分大小写，多行匹配等等。
# 匹配成功 re.search 方法返回一个匹配从、的对象，否则返回 None 对象

# line = "Cats are smarter than dogs"

# print(re.search("www", 'www.runoob.com').span())
# print(re.search("com", 'www.runoob.com').span())
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
# if searchObj:
#    print ("matchObj.group() : ", searchObj.group())
#    print ("matchObj.group(1) : ", searchObj.group(1))
#    print ("matchObj.group(2) : ", searchObj.group(2))
# else:
#    print ("No match!!")

# 检索和替换

# python 的re模块提供了 re.sub 用于替换自妇产中的匹配项。
# 语法: re.sub(pattern, string : 要被查找替换的原始字符串, string, flags=0)