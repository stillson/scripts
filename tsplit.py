#!/usr/bin/env python

import sys


field = int(sys.argv[1])


for i in sys.stdin:
    try:
        print(i.split()[field - 1], end=" ")
        print()
    except:
        pass


