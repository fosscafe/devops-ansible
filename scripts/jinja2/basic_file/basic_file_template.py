#!/usr/bin/env python

import os
from jinja2 import Environment
from jinja2 import FileSystemLoader

dir = os.path.dirname (os.path.abspath (__file__))

meetup = {}

meetup ['group']  = 'fosscafe'
meetup ['topic']  = 'ansible'
meetup ['date']   = '2017-09-02T15:00:00+05:30'
meetup ['time']   = '2017-09-02T15:00:00+05:30'
meetup ['venue']  = 'Nutanix'

jinja_env = Environment (loader=FileSystemLoader(dir),
						 trim_blocks=True)

t = jinja_env.get_template ('file.template')

print (t.render(
	group  = meetup['group'],
	topic  = meetup['topic'],
	date   = meetup['date'],
	time   = meetup['time'],
	venue  = meetup['venue']))


'''
commentary


'''
