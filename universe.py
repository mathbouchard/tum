# Universe module for the tum project
#
# A universe is a set of elements. Each elements are defined
# by a set of attributes, a qty and a type (either 'state' or
# 'transition'). Each element has a set of incident
# dual elements (either of type 'in' or 'out'). The dual of
# a 'state' is a 'transition' and vice-versa.
#
# created by : mathbouchard, 2013/02/21
# modified by : mathbouchard, 2013/02/21

from ugetinitialelements import ugetinitialelements
from ugetdualelements import ugetindualelements, ugetoutdualelements, ugetalldualelements
from ugetoutputs import ugetoutputs
from ugetreachables import ugetreachables

# The universe that encapsulates all possible elements and the
# methods to retrieve them
class Universe(object):
    def getInitialElements(self, ofilter, odata):
        return ugetinitialelements(ofilter, odata)
    def getReachables(self, elems, ofilter, odata):
        return ugetreachables(elems, ofilter, odata)

# A partial view of a universe with a discrete number of elements
class World(object):
    def __init__(self, e):
        self.elements = e
        self.initialelements = e
    def printElements(self):
        for e in self.elements:
            print '[('+str(len(self.elements))+') type = ' + e.type
            for a in e.attr:
                print ' ['+a.name + '('+a.strval +', '+str(a.dblval) + ')] '
            print ']'

# An element description an the methods to get its neighbors dual elements
class Element(object):
    def __init__(self, t, q, a):
        type = t
        qty = q
        self.attr = a
    def getInDualElements(self, ofilter, odata):
        return ugetindualelements(self, ofilter, odata)
    def getOutDualElements(self, ofilter, odata):
        return ugetoutdualelements(self, ofilter, odata)
    def getAllDualElements(self, ofilter, odata):
        return ugetalldualelements(self, ofilter, odata)
    def getOutputs(self, ofilter, odata):
        return ugetoutputs(self, ofilter, odata)
    def getstrval(self):
        hstr = self.type;
        for a in self.attr:
            hstr = hstr+a.name#+a.strval+str(a.dblval)
        return hstr
                
# A set of values that defined an element or a measurable output
class Attribute(object):
    def __init__(self, n, sv, dv):
        self.name = n
        self.strval = sv
        self.dblval = dv
