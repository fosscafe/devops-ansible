#!/usr/bin/env python

import yaml

filename = 'lib-tofix.yml'

with open (filename, "r") as stream:
	try:
		print (yaml.load (stream))
	except yaml.YAMLError as ex:
		print (ex)


