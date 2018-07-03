#!/usr/bin/env python
import rethinkdb as r
import os
import sys

r.connect('localhost', 28015, db='tp2').repl()

print(r.db('tp2').table('eventos').order_by(r.desc('facturacionTotal')).limit(5).run())