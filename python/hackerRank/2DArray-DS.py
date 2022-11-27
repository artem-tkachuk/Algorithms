#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

def hourglassSum(arr):
    max_hourglass_sum = float("-inf")
    
    for i in range(1, 5): # [1, 4]
        for j in range(1, 5): # [1, 4]
            curr_hourglass_sum = arr[i][j] + arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + \
                + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            max_hourglass_sum = max(max_hourglass_sum, curr_hourglass_sum)

    return max_hourglass_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
