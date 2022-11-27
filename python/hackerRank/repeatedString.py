#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Can be changed later
    ch = 'a'
    # length of pattern
    m = len(s)
    # number of times a string is fully repeated
    whole_repetitions = n // m
    remainder_len = n % m
    
    count_remainder = s[:remainder_len].count(ch)
    count_whole_repetitions = (count_remainder + s[remainder_len:].count(ch)) * whole_repetitions
    
    
    print(count_remainder)
    
    return count_whole_repetitions + count_remainder
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
