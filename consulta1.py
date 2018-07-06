#!/usr/bin/env python
import rethinkdb as r
import sys

r.connect('localhost', 28015, db='tp2').repl()

persona = int(sys.argv[1])

rows = r.db('tp2').table('clientes').filter({'dni':persona})["atraccionesVisitadas"].map(lambda val:
  val["nombre"].distinct()).run()

for atracciones in rows:
    for atraccion in atracciones:
        print(atraccion)
