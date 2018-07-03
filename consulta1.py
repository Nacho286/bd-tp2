#!/usr/bin/env python
import rethinkdb as r
import os
import sys

r.connect('localhost', 28015, db='tp2').repl()

persona = int(sys.argv[1])

print(r.db('tp2').table('clientes').filter({'dni':persona})["atraccionesVisitadas"].map(lambda val:
  val["nombre"].distinct()).run())