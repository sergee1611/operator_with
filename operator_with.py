# -*- coding: utf-8 -*-

file_name = 'bairon.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line, end='')
