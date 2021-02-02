#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
def valor(n):
    if n % 2 != 0:
        valoracion = "Weird"
    elif n > 1 and n < 6:
        valoracion = "Not Weird"
    elif n > 20:
        valoracion = "Not Weird"
    else:
        valoracion ="Weird"
    return valoracion 
print (valor(int(n)))