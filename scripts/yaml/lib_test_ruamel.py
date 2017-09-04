#!/usr/bin/env python

import ruamel.yaml as yaml

filename = 'lib-tofix.yml'

with open (filename, "r") as stream:
	try:
		print (yaml.load (stream))
	except yaml.YAMLError as ex:
		print (ex)


