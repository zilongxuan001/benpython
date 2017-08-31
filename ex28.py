#--coding: utf-8 --
#Date:20170831
#Title:ex28 布尔表达式练习

#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
#在python的IDLE（即python 3.5.0 Shell）里练习

# True and True
# False and True
# 1 == 1 and 2 == 1
# "test" == "test"
# 1 == 1 or 2 != 1
# True and 1 == 1
# False and 0 != 0
# True or 1 == 1
# "test" == "testing"
# 1 != 0 and 2 == 1
# "test" != "testing"
# "test" == 1
# not (True and False)
# not (1 == 1 and 0 != 1)
# not (10 == 1 or 1000 == 1000)
# not (1 != 10 or 3 == 4)
# not ("testing" == "testing" and "Zed" == "Cool Guy")
# 1 == 1 and not ("testing" == 1 or 1 == 0)
# "chunky" == "bacon" and not (3 == 4 or 3 == 3)
# 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

# 所有的布尔逻辑表达式都可以用下面的简单流程得到结果：

# 找到相等判断的部分 (== or !=)，将其改写为其最终值 (True 或 False)。
# 找到括号里的 and/or，先算出它们的值。
# 找到每一个 not，算出他们反过来的值。
# 找到剩下的 and/or，解出它们的值。
# 等你都做完后，剩下的结果应该就是 True 或者 False 了。

#加分题
# Python 里还有很多和 != 、 == 类似的操作符. 试着尽可能多地列出 Python 中的等价运算符。例如 < 或者 <= 就是。
# 写出每一个等价运算符的名称。例如 != 叫 “not equal（不等于）”。
# 在 python 中测试新的布尔操作。在敲回车前你需要喊出它的结果。不要思考，凭自己的第一感就可以了。把表达式和结果用笔写下来再敲回车，最后看自己做对多少，做错多少。
# 把习题 3 那张纸丢掉，以后你不再需要查询它了

#等价运算符
# !=  not equal 不等于
# ==  equal      等于
# >=  greater-than-equal 大于等于
# <=  less-than-equal    小于等于
# >   greater-than        大于
# <   less-than           小于

