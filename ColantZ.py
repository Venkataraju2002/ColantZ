# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:51:44 2021

@author: admin
"""

a,b,c=map(int,input().split())
if a>b and a>c:
    print("1stnumber:",a)
elif b>c and b>a:
    print("2nd no:",b)

else:
    print("3rd number:",c)
