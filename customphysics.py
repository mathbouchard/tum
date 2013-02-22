# customphysics module for the tum project
#
# user custom implemetation of the tum project methods
#
# created by : mathbouchard, 2013/02/22
# modified by : mathbouchard, 2013/02/22

import universe
import defaultphysics

def custominitials(u, efilter):
    ss=set()
    total=set()
    s = u.getInitialElements(defaultphysics.ugetinitialelements, None)
    ss= ss | s
    while 0==0:
        reachelems = u.getReachables(defaultphysics.ugetreachables, s, None)
        
        total = total | reachelems
        
        s = set()
        stop = 1
        for i in range(100):
            e = universe.Element(u, 'state', 1, [])
            e.attr.append(universe.Attribute("box"+str(i), str(i), i))
            if e not in total:
                s.add(e)
                ss.add(e)
                stop = 0
                break
        if stop == 1:
            break
    return ss

def customoutputs(o, efilter):
    s=set()
    s.add(o)
    reachelems = o.u.getReachables(defaultphysics.ugetreachables, s, None)
    return [ universe.Attribute("val", str(len(reachelems)), len(reachelems)) ]
