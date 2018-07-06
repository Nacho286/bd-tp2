#!/usr/bin/env python
import rethinkdb as r
import os
import sys

r.connect('localhost', 28015, db='tp2').repl()

locacion = int(sys.argv[1])

rows = r.db('tp2').table('parques').filter({'idLocacion':locacion}).pluck({'atracciones':['nombre','cantidadVisitas']}).order_by(lambda row: row['atracciones']['cantidadVisitas']).run()

for parque in rows:
    pos = 1
    for atraccion in parque['atracciones']:
        print(str(pos) + ": " + atraccion['nombre'] + " " + str(atraccion['cantidadVisitas']))
        pos += 1
