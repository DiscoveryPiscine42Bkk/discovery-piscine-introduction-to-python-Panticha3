#!/usr/bin/env python3

password = "Python is awesome"
val = input()
if val.strip() == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")