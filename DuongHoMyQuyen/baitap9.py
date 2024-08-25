# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:24:37 2024

@author: Student
"""
import math
a=float(input("So thuc a:"))
b=float(input("So thuc b:"))
bieu_thuc = (math.sqrt(a)- math.sqrt(b))/(a**(1/4) - b**(1/4)) - (math.sqrt(a) + (a*b)**(1/4)) / (a**(1/4) + b**(1/4))
print("ket qua:", bieu_thuc)
