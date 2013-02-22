from universe import Universe, World, Element, Attribute

def f(x): return 0==0

u = Universe()
elems = u.getInitialElements(f, None)
reachelems = u.getReachables(elems, f, None)
w1 = World(elems)
w1.printElements()
w2 = World(reachelems)
#w2.printElements()
