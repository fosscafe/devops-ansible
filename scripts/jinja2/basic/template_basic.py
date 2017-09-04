#!/usr/bin/env python

from jinja2 import Environment

meetup = {}

meetup ['group']  = 'fosscafe'
meetup ['topic']  = 'ansible'
meetup ['date']   = '2017-09-02T15:00:00+05:30'
meetup ['time']   = '2017-09-02T15:00:00+05:30'
meetup ['venue']  = 'Nutanix'

template="""event:
  - {{ group }}
  - {{ topic }}
  - {{ date }}
  - {{ time }}
  - {{ venue }}
"""

t = Environment().from_string (template)

print (t.render(
	group  = meetup['group'],
	topic  = meetup['topic'],
	date   = meetup['date'],
	time   = meetup['time'],
	venue  = meetup['venue']))


'''
commentary


for k,v in meetup.items ():
	print (k, " : ", v, '\n')


event_yml = str.format(
		group  = meetup['group'],
		topic  = meetup['topic'],
		date   = meetup['date'],
		time   = meetup['time'],
		venue  = meetup['venue'])
print (event_yml)

we will use multi-line string format

use date command with ISO format
date --iso-8601=seconds

'''
