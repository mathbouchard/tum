from universe import Universe, World, Element, Attribute
import defaultphysics
import customphysics

def f(x,y):
    if x['value'] == 1:
        return y
    else:
        return set()

u = Universe()
efilter = {'filter' : f, 'value' : 1}
elems = u.getInitialElements(defaultphysics.ugetinitialelements, efilter)
reachelems = u.getReachables(defaultphysics.ugetreachables, elems, efilter)
w2 = World(reachelems)
w2.printElements()
altelems = u.getInitialElements(customphysics.custominitials, None)
for e in altelems:
    print e.attr[0].name + ' (' +str(e.getOutputs(customphysics.customoutputs, None)[0].dblval) + ')'
    reachelems = u.getReachables(defaultphysics.ugetreachables, set([e]), None)
    strg ='\t'
    for ee in reachelems:
        strg+=str(ee.attr[0].dblval) + ' --> '
    print strg