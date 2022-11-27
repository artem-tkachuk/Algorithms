#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

from collections import defaultdict

def sockMerchant(n, ar):
    colors = defaultdict(int)
    
    for color in ar:
        colors[color] += 1
        
    pairs = 0
    
    for (color, quantity) in colors.items():
        pairs += (quantity // 2)
        
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
