#!/usr/bin/env python
import rethinkdb as r
import os
import sys

r.connect('localhost', 28015, db='tp2').repl()

locacion = int(sys.argv[1])

rows = r.db('tp2').table('parques').filter({'idLocacion':locacion})["atracciones"].map(lambda x:
  x.pluck("nombre",{"visitas":"precio"})).run()

for parque in rows:
    for atraccion in parque:
        total = 0
        for visita in atraccion['visitas']:
            total += visita['precio']
        print(atraccion['nombre'] + " $" + str(total))
