#!/usr/bin/env python3

import sys, range

if len(sys.argv) != 3:
    print("Invalid Input!!")
    sys.exit()

key = sys.argv[1]
string = sys.argv[2]
print(len(re.findall(re.escape(key), string)))