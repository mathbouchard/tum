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

# The universe that encapsulates all possible elements and the
# methods to retrieve them
class Universe(object):
    def getInitialElements(self, f, efilter):
        return f(self, efilter)
    def getReachables(self, f, elems, efilter):
        return f(self, elems, efilter)
    workspace = dict()

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
    def __init__(self, inu, t, q, a):
        self.type = t
        self.qty = q
        self.attr = a
        self.u = inu;
    def getInDuals(self, f, efilter):
        return f(self, efilter)
    def getOutDuals(self, f, efilter):
        return f(self, efilter)
    def getAllDuals(self, f, efilter):
        return f(self, efilter)
    def getOutputs(self, f, efilter):
        return f(self, efilter)
    def __hash__(self):
        hstr = self.type;
        for a in self.attr:
            hstr = hstr+a.name+a.strval+str(a.dblval)
        return hash(hstr)
    def __eq__(self, other):
        return self.type == other.type and self.attr == other.attr
    
                
# A set of values that defined an element or a measurable output
class Attribute(object):
    def __init__(self, n, sv, dv):
        self.name = n
        self.strval = sv
        self.dblval = dv
    def __eq__(self, other):
        return self.name == other.name and self.strval == other.strval and self.dblval == other.dblval
