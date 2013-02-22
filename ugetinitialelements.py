# ugetinitialelements module for the tum project
#
# user implementation to get all initial elements filtered by Filter
#
# created by : mathbouchard, 2013/02/21
# modified by : mathbouchard, 2013/02/21

import universe

def ugetinitialelements(ofilter, odata):
    s=set()
    e = universe.Element('state', 1, [])
    e.type = 'state'
    e.attr.append(universe.Attribute("box0", str(0), 0))
    s.add(e)
    s = filter(ofilter, s)
    return s

