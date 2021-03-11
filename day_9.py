#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    return math.factorial(n)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(factorial(i))
