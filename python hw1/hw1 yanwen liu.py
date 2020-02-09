# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 1
list1 = list(range(1,21))
list2 = list(range(20,0,-1))
list3 = list(range(19,0,-1))
list4 = [4,6,3] * 10
list5 = [4,6,3] * 11
del list5[31:33]
print(list1)
print(list2)
print(list1+list3)
print(list4)
print(list5)
# 2
list6 = list(range(30,61,1))
list7 = [i * 0.1 for i in list6]
from math import exp, cos
list8 = [exp(i)*cos(i) for i in list7]
print(list8)
# 3
list9 = list(range(1,26,1))
print([2**i/i for i in list9])
# 4
print([list1[i-1]-list1[19-i] for i in list1])
print([i%2 == 0 for i in list1])
# 5 
file = open("lorem.txt", "r")
file.read(1)
file.close()