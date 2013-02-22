# ugetdualelements module for the tum project
#
# user implementation to get dual incident elements
#
# created by : mathbouchard, 2013/02/21
# modified by : mathbouchard, 2013/02/21

import universe
import random

class tempmap(object):
    sout = dict()
    sin = dict()
    tout = dict()
    tin = dict()

def ugetalldualelements(o, ofilter, odata):
    return ugetindualelements(o, ofilter, odata) & ugetoutdualelements(o, ofilter, odata)

def ugetindualelements(o, ofilter, odata):
    odata = fill()
    s=set()
    if o.type == 'state':
        i = odata.sin[o.attr[0].dblval]
        e = universe.Element('transition', 1, [])
        e.type = 'transition'
        e.attr.append(universe.Attribute("move"+str(i), str(i), i))
        s.add(e)
    else:
        i = odata.tin[o.attr[0].dblval]
        e = universe.Element('state', 1, [])
        e.type = 'state'
        e.attr.append(universe.Attribute("box"+str(i), str(i), i))
        s.add(e)
    return s

def ugetoutdualelements(o, ofilter, odata):
    odata = fill()
    s=set()
    if o.type == 'state':
        i = odata.sout[o.attr[0].dblval]
        e = universe.Element('transition', 1, [])
        e.type = 'transition'
        e.attr.append(universe.Attribute("move"+str(i), str(i), i))
        s.add(e)
    else:
        i = odata.tout[o.attr[0].dblval]
        e = universe.Element('state', 1, [])
        e.type = 'state'
        e.attr.append(universe.Attribute("box"+str(i), str(i), i))
        s.add(e)
    return s

def fill():
    o = tempmap()
    l = []
    l = range(100)
    random.seed()
    c = 0
    for i in range(100):
        t = l.pop(random.randint(0,len(l)-1))
        o.sout[c] = i;
        o.sin[t] = i;
        o.tin[i] = t;
        o.tout[i] = i;
        c=t;
    return o