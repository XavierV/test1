#!/usr/bin/env python
# test for Jenkins
import datetime

def get_ts():
        return str(datetime.datetime.now())[:23]

print '{} Bonjour'.format(get_ts())
print 'version0.1'
print 'Added this & that'
print 'trigger1'
print 'trigger2'
print 'Bye!'
