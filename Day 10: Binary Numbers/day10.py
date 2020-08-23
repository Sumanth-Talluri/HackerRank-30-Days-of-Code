#!/bin/python3

import math
import os
import random
import re
import sys

res = ''
def dec_to_binary(num): 
    if num <= 0 : 
        return ''
    return str(num%2) + str(dec_to_binary(num//2))

if __name__ == '__main__':
    n = int(input())
    binary_val = dec_to_binary(n)

    maxx = 0
    for i in range(0,len(binary_val)):
        count = 0
        for j in range(i,len(binary_val)):
            if binary_val[i] == '1' and binary_val[j] == '1':
                count += 1
            else :
                break
        if maxx < count:
            maxx = count
    print(maxx)
