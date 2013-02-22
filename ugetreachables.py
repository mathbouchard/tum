# ugetreachables module for the tum project
#
# user implementation to get the the reachable elements from
# an initial list of elements
#
# created by : mathbouchard, 2013/02/21
# modified by : mathbouchard, 2013/02/21

import universe

def ugetreachables(elems, ofilter, odata):
    ss = set()
    sts = set(elems)
    cs = set(elems)
    comp = set()
    
    for e in elems:
        comp.add(e.getstrval())
    
    while len(cs) > 0 and len(ss) < 200:
        ss = sts.copy()
        for e in cs:
            for s in e.getOutDualElements(lambda x: 0==0, None):
                for e2 in s.getInDualElements(lambda x: 0==0, None):
                    if e2.getstrval() not in comp:
                        sts.add(e2)
                        comp.add(e2.getstrval())
                        print e2.getstrval()
        cs = sts-ss
        print len(ss)
    return ss