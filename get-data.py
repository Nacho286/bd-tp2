#!/usr/bin/env python
import rethinkdb as r
import json

r.connect('localhost', 28015, db='tp2').repl()

print '\n-----------------CLIENTES'
for row in r.table('clientes').run():
    print json.dumps(row, indent=2)
# print '\n-----------------EVENTOS'
# for row in r.table('eventos').run():
#     print json.dumps(row, indent=2)
# print '\n-----------------PARQUES'
# for row in r.table('parques').run():
#     print json.dumps(row, indent=2)
# print '\n-----------------FACTURAS'
# for row in r.table('facturas').run():
#     print json.dumps(row, indent=2)
