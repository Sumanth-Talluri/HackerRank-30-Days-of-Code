#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    maxx = 0
    res = 0

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for i in range(4):
        for j in range(4):
            res = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 
            if maxx < res or (i==0 and j==0):
                maxx = res
    print(maxx)

