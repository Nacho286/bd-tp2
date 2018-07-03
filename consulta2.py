#!/usr/bin/env python
import rethinkdb as r
import os
import sys

r.connect('localhost', 28015, db='tp2').repl()

locacion = int(sys.argv[1])

print(r.db('tp2').table('parques').filter({'idLocacion':locacion}).pluck({'atracciones':['nombre','cantidadVisitas']}).order_by(lambda row: row['atracciones']['cantidadVisitas']).run())