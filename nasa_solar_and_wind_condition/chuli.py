#!/usr/bin/python
# -*- coding: UTF-8 -*-

i=0
with open('province_location.csv', 'r') as f:
	with open('out.txt','w') as w:
		for line in f.readlines():
			if i==3:
				w.write('\n')
				i=0
			if line != '\n':
				w.write(line.replace('\n',' '))
				i=i+1

