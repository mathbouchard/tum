# defaultphysics module for the tum project
#
# user default implemetation of the tum project methods
#
# created by : mathbouchard, 2013/02/22
# modified by : mathbouchard, 2013/02/22

import universe
import random



# user default implementation to get the the reachable elements from
# an initial list of elements
def ugetreachables(u, elems, efilter):
    
    
    ss = set()
    sts = set(elems)
    cs = set(elems)
        
    while len(cs) > 0 and len(ss) < 200:
        ss = sts.copy()
        for e in cs:
            
            for s in e.getOutDuals(ugetoutduals, None):
                for e2 in s.getInDuals(ugetinduals, None):
                    sts.add(e2)
        cs = sts-ss

    if efilter != None:
        ss = efilter['filter'](efilter,ss)
    return ss

# user default implementation to get all initial elements filtered by Filter
def ugetinitialelements(u, efilter):
    s=set()
    e = universe.Element(u, 'state', 1, [])
    e.attr.append(universe.Attribute("box0", str(0), 0))
    s.add(e)
    if efilter != None:
        s = efilter['filter'](efilter,s)
    return s

# user default implementation to get the output of an element
def ugetoutputs(o, efilter):
    return [ universe.Attribute("val", "1", 1) ]

# user implementation to get all dual incident elements
def ugetallduals(o, efilter):
    s = ugetinduals(o, efilter) | ugetoutduals(o, efilter)
    if efilter != None:
        s = efilter['filter'](efilter,s)
    return s

# user implementation to get ingoing dual incident elements
def ugetinduals(o, efilter):
    if 'sout' not in o.u.workspace:
        odata = fill(o.u.workspace)
    s=set()
    if o.type == 'state':
        i = o.u.workspace['sin'][o.attr[0].dblval]
        e = universe.Element(o.u, 'transition', 1, [])
        e.attr.append(universe.Attribute("move"+str(i), str(i), i))
        s.add(e)
    else:
        i = o.u.workspace['tin'][o.attr[0].dblval]
        e = universe.Element(o.u, 'state', 1, [])
        e.attr.append(universe.Attribute("box"+str(i), str(i), i))
        s.add(e)
    if efilter != None:
        s = efilter['filter'](efilter,s)
    return s

# user implementation to get outgoing dual incident elements
def ugetoutduals(o, efilter):
    if 'sout' not in o.u.workspace:
        odata = fill(o.u.workspace)
    s=set()
    if o.type == 'state':
        i = o.u.workspace['sout'][o.attr[0].dblval]
        e = universe.Element(o.u, 'transition', 1, [])
        e.attr.append(universe.Attribute("move"+str(i), str(i), i))
        s.add(e)
    else:
        i = o.u.workspace['tout'][o.attr[0].dblval]
        e = universe.Element(o.u, 'state', 1, [])
        e.attr.append(universe.Attribute("box"+str(i), str(i), i))
        s.add(e)
    if efilter != None:
        s = efilter['filter'](efilter,s)
    return s

def fill(w):
    w['sout'] = range(100)
    w['sin'] = range(100)
    w['tout'] = range(100)
    w['tin'] = range(100)
    l = range(100)
    random.seed()
    
    for i in range(100):
        t = l.pop(random.randint(0,len(l)-1))
        w['sout'][i] = i;
        w['sin'][t] = i;
        w['tin'][i] = t;
        w['tout'][i] = i;
        c=t;
