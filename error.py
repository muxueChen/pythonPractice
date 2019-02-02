#python 中包含若干中异常对象。常用的常用的异常包括 IOError、IndexError、NameError、SyntaxError、TypeError、UnicodeError和valueError。你可以在网上获取更多的异常的信息，参见标准库中的“Built-in Exceptions”那一节

#try-except
# 计算一系列数值的均值
def getMean(numericVales):
    return sum(numericVales)/len(numericVales)

my_list2 = [ 1, 2]
try:
    print("{}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("{}".format(float('nan')))
    print("{}".format(detail))

# 完整形式
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("------{}".format(float('nan')))
    print("-----{}".format(detail))

else:
    print (">>>>{}".format(result))
finally:
    print("The finally block is executed every time")
    