#!/usr/bin/env python
import rethinkdb as r
import random
import time
max=1000000
oneClientId=0
initialPoint=500

def randomString(size):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz 0123456789') for _ in range(size))

def createClient(index):
    res = r.table('clientes').insert({
        'dni': index,
        'nombre': randomString(20),
        'apellido': randomString(10),
        'direccion': randomString(30),
        'telefono': randomString(9),
        'atraccionesVisitadas': []
    }).run()
    global oneClientId
    if oneClientId == 0 or random.randint(1, 100) > 90:
        oneClientId = res['generated_keys'][0]

def getClients():
    r.table('clientes').run()

def getOneClient():
    global oneClientId
    r.table('clientes').get(oneClientId).run()

def getGroupClients(currentPoint):
    global initialPoint
    size = initialPoint / 2
    start = random.randint(1,currentPoint-size)
    r.table('clientes').filter((r.row["dni"] >= start) & (r.row["dni"] < (start+size))).run()

print('Connecting')
r.connect('localhost', 28015, db='tp2').repl()
print('Droping table')
r.table('clientes').delete().run()

f = open('shard-testing.csv', 'w')
f.write("Rows, Get one, Get all, Get group\n")

print('Initializing')
point=initialPoint
for i in range(1,max):
    createClient(i)
    if i == point or i == max-1:
        print "---- " + str(i)
        point *= 2
        startTime=time.time()
        getClients()
        endTime=time.time()
        getAllTime=(endTime - startTime) * 1000
        print "Time get all: " + str(getAllTime)
        startTime=time.time()
        getOneClient()
        endTime=time.time()
        getOneTime=(endTime - startTime) * 1000
        print "Time get one: " + str(getOneTime)
        startTime=time.time()
        getGroupClients(i)
        endTime=time.time()
        getGroupTime=(endTime - startTime) * 1000
        print "Time get group: " + str(getGroupTime)
        f.write(str(i) + "," + str(getOneTime) + "," + str(getAllTime) + "," + str(getGroupTime) + "\n")
        print "--------"
