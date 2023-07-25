#!/usr/bin/env python3

dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 6}
print(dic)
first_key = next(iter(dic))
dic.pop(first_key)
print(dic)


