#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Invalid Input!")