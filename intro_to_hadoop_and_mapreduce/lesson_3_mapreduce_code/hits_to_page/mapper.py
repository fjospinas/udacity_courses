#!/usr/bin/python

import sys
import re

patern = re.compile('(.*GET) (.*) (H.*)')

for line in sys.stdin:
	data = patern.match(line)
	if data:
		print '{key}'.format(key=data.group(2))
