#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    x = (N % 2) == 0
    if not(x):
        print('Weird')
    elif x and N in range(2, 5):
        print('Not Weird')
    elif x and N in range(6, 20+1):
        print("Weird")
    else:
        print('Not Weird')
