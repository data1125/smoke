#############################第二章
#######資料:型態.值.變數與名稱
#賦值
# x = 5
# y = x + 12
# print(y)

# a = 5
# b = 12 - a
# print(b)

# c = 7
# print(c)

# d = c
# print(d)
# ####type()
# print(type(5))
# print(type(5) == int)
# print(isinstance(7, int))
# a = 6
# b = a
# print(type(a))
# print(type(b))
# print(type(56))
# print(type(44.4))
# print(type("abc"))
###################指派給多個名稱
# two = deux = zwei = 2
# print(two)
# print(deux)
# print(zwei)####這三個都能印出2   ###重新指派名稱
#################複製
# x = 5
# print(x)

# y = x
# print(y)

# x = 29
# print(x)
# print(y)

# a = [2, 4, 6]
# b = a
# print(a)
# print(b)

# a[0] = 99
# print(a)
# print(b)
# ###########################2.1
# prince  = 99
# print(prince)
# ###########################2.2
# print(type(5))
# ###########################2.3
# print(type(2.0))
# ###########################2.4
# print(type(5+2.0))
######################################第三章
#############數字
###########布林
####bool()函式可以用引數接收任何值,並回傳其對應的布林值
# print(bool(True))
# print(bool(1))
# print(bool(45))
# print(bool(-45))
# ####將零值數字視為False
# print(bool(False))
# print(bool(0))
# print(bool(0.0))
#########整數前面放上 + - 符號 
# print(f"+{123}")  #印出+123
# print(f"-{456}")  #印出-123
# #########整數裡面不能有任何逗號
# print(1,000,000)  #印出 1 0 0
####可以用_字元當成數字分隔符號
# million = 1_000_000
# print(million)  #成功印出1000000
# ####可以在第一個數字後面的任何地方加入底線,它們都會被忽略
# print(1_2_3)
##############整數運算
print(5 + 9)
print(100 - 9)
print(4 - 10)
#############可以隨意使用任何數量的數字和運算子
print(5 + 9 + 4)
print(4 + 3 - 2 - 1 + 6)
###########不需要每一個數字與運算子之前加上空格
print(5+9  + 4)
###########乘法也很簡單
print(6*7)
print(7*6)
print(7 * 6 * 2 * 3)
##########使用 / 會產生浮點數結果,即使你將整數除以整數
print(9 / 5)
