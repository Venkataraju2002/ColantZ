# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:42:57 2021

@author: admin
"""

n=int(input())
L=n
while n>=1:
    if (L%2==0):
        L=L//2
        print(L)
    if (L==1):
        break
    if L%2!=0:
        L=((3*L)+1)
        print(L)
n=L