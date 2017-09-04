#!/usr/bin/env python

import sys
import yaml

filename = sys.argv[1] 

with open (filename, "r") as stream:
	try:
		print (yaml.load (stream))
	except yaml.YAMLError as ex:
		print (ex)


'''
commentary

./template_basic_test.py file.yml

'''
