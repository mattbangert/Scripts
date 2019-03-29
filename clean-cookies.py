#!/usr/bin/env python
import json
import sys

if len(sys.argv) == 1:
    print "You must provide a valid path to the cookies json file."
    sys.exit(1)



fileName = sys.argv[1]

data = json.loads(open(fileName).read())

for datum in data:
    print datum['name'] + ':' + datum['value']