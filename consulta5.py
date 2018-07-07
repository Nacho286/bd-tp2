#!/usr/bin/env python
import rethinkdb as r
import sys

r.connect('localhost', 28015, db='tp2').repl()

persona = int(sys.argv[1])

rows = r.db('tp2').table('clientes').filter({'dni':persona})["atraccionesVisitadas"].reduce(lambda y: y).map(lambda val:r.expr([]).append(val["nombre"])).reduce(lambda x,y :x.set_union(y)).run()

for atraccion in rows:
    print(atraccion)
