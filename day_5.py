#!/bin/python3

import math
import os
import random
import re
import sys

def mult_func(n):
    for y in range(1, 10+1):
        x = n * y
        print('{} x {} = {}'.format(n, y, x))

if __name__ == '__main__':
    n = int(input())
    mult_func(n)