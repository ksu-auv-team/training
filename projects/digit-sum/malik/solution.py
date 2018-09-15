#!/bin/python

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N):
    return recursion(X,N,1)

def recursion(X,N,num):
    if pow(num,N)==X:
        return 1
    elif pow(num,N)<X:
        return recursion(X,N,num+1) + recursion(X-pow(num,N),N,num+1)
    elif pow(num,N)>X:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(raw_input())

    N = int(raw_input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
# I needed help for this one. I suck at recursion : (
