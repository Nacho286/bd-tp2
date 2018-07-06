#!/usr/bin/env python
import rethinkdb as r

r.connect('localhost', 28015, db='tp2').repl()

rows = r.db('tp2').table('eventos').order_by(r.desc('facturacionTotal')).limit(5).run()

pos = 1
for evento in rows:
    print(str(pos) + ": " + evento['nombre'] + " $" + str(evento['facturacionTotal']))
    pos += 1
