#!/usr/bin/env python
import rethinkdb as r
tablelist = ['clientes', 'facturas', 'eventos', 'parques']

r.connect('localhost', 28015, db='tp2').repl()
for table in tablelist:
    r.table(table).delete().run()

# Clientes
r.table('clientes').insert({
    'dni': 13241345,
    'nombre': 'Juan',
    'apellido': 'Garcia',
    'direccion': 'Calle Falsa 123, CABA',
    'telefono': '4444-4444',
    'atraccionesVisitadas': [{
        'idEntrada': 2,
        'idAtraccion': 1,
        'nombre': 'Tazas Locas',
        'fecha': '2017-01-16 11:30:00'
    }, {
        'idEntrada': 3,
        'idAtraccion': 1,
        'nombre': 'Tazas Locas',
        'fecha': '2017-01-16 13:00:00'
    }, {
        'idEntrada': 5,
        'idAtraccion': 2,
        'nombre': 'Samba',
        'fecha': '2017-02-17 11:00:00'
    }, {
        'idEntrada': 6,
        'idAtraccion': 1,
        'nombre': 'Tazas Locas',
        'fecha': '2017-02-17 11:45:00'
    }, {
        'idEntrada': 7,
        'idAtraccion': 2,
        'nombre': 'Samba',
        'fecha': '2017-02-17 15:00:00'
    }, {
        'idEntrada': 8,
        'idAtraccion': 2,
        'nombre': 'Samba',
        'fecha': '2017-02-17 15:20:00'
    }]
}).run()
r.table('clientes').insert({
    'dni': 24356543,
    'nombre': 'Roberto',
    'apellido': 'Perez',
    'direccion': 'Cangallo 4000, CABA',
    'telefono': '5555-5555',
    'atraccionesVisitadas': []
}).run()
r.table('clientes').insert({
    'dni': 32333444,
    'nombre': 'Agustin',
    'apellido': 'Sanchez',
    'direccion': 'Libertador 1431, CABA',
    'telefono': '4545-4545',
    'atraccionesVisitadas': [{
        'idEntrada': 12,
        'idAtraccion': 3,
        'nombre': 'Autitos Chocadores',
        'fecha': '2018-04-25 10:10:00'
    }, {
        'idEntrada': 13,
        'idAtraccion': 4,
        'nombre': 'Twister',
        'fecha': '2018-04-25 10:50:00'
    }]
}).run()
r.table('clientes').insert({
    'dni': 28123456,
    'nombre': 'Fabiana',
    'apellido': 'Fernandez',
    'direccion': 'Av Siempreviva 742',
    'telefono': '011 1234-5678',
    'atraccionesVisitadas': []
}).run()

# Eventos
r.table('eventos').insert({
    'idLocacion': 3,
    'nombre': 'Loolapalusa',
    'cuitEmpresa': 20314457769,
    'fechaInicio': '2017-04-04',
    'fechaFin': '2017-04-06',
    'visitas': [{
        'idEntrada': 9,
        'dni': 24356543,
        'precio': 1000,
        'numeroDeTarjeta': 2,
        'fecha': '2017-04-04 08:00:00'
    }, {
        'idEntrada': 10,
        'dni': 24356543,
        'precio': 1000,
        'numeroDeTarjeta': 2,
        'fecha': '2017-04-05 08:00:00'
    }],
    'facturacionTotal': 2000
}).run()
r.table('eventos').insert({
    'idLocacion': 4,
    'nombre': 'Copa Libertadores',
    'cuitEmpresa': 20344561703,
    'fechaInicio': '2017-04-05',
    'fechaFin': '2017-10-20',
    'visitas': [{
        'idEntrada': 14,
        'dni': 28123456,
        'precio': 400,
        'numeroDeTarjeta': 7,
        'fecha': '2018-04-28 21:15:00'
    }],
    'facturacionTotal': 400
}).run()

# Parques
r.table('parques').insert({
    'idLocacion': 1,
    'nombre': 'Parque de la Costa',
    'precio': 100,
    'atracciones': [{
        'idAtraccion': 1,
        'nombre': 'Tazas Locas',
        'precio': 50,
        'minimoEdad': 10,
        'minimoAltura': 140,
        'visitas': [{
            'idEntrada': 2,
            'dni': 13241345,
            'precio': 50,
            'numeroDeTarjeta': 1,
            'fecha': '2017-01-16 11:30:00'
        }, {
            'idEntrada': 3,
            'dni': 13241345,
            'precio': 50,
            'numeroDeTarjeta': 1,
            'fecha': '2017-01-16 13:00:00'
        }, {
            'idEntrada': 6,
            'dni': 13241345,
            'precio': 60,
            'numeroDeTarjeta': 4,
            'fecha': '2017-02-17 11:45:00'
        }],
        'cantidadVisitas': 3
    }, {
        'idAtraccion': 2,
        'nombre': 'Samba',
        'precio': 20,
        'minimoEdad': 8,
        'minimoAltura': 110,
        'visitas': [{
            'idEntrada': 5,
            'dni': 13241345,
            'precio': 20,
            'numeroDeTarjeta': 4,
            'fecha': '2017-02-17 11:00:00'
        }, {
            'idEntrada': 7,
            'dni': 13241345,
            'precio': 20,
            'numeroDeTarjeta': 4,
            'fecha': '2017-02-17 15:00:00'
        }, {
            'idEntrada': 8,
            'dni': 13241345,
            'precio': 20,
            'numeroDeTarjeta': 4,
            'fecha': '2017-02-17 15:10:00'
        }],
        'cantidadVisitas': 3
    }],
    'visitas': [{
        'idEntrada': 1,
        'dni': 13241345,
        'precio': 100,
        'numeroDeTarjeta': 1,
        'fecha': '2017-01-16 10:50:00'
    }, {
        'idEntrada': 4,
        'dni': 13241345,
        'precio': 100,
        'numeroDeTarjeta': 4,
        'fecha': '2017-02-17 09:35:00'
    }]
}).run()
r.table('parques').insert({
    'idLocacion': 2,
    'nombre': 'Italpark',
    'precio': 300,
    'atracciones': [{
        'idAtraccion': 3,
        'nombre': 'Autitos Chocadores',
        'precio': 60,
        'minimoEdad': 6,
        'minimoAltura': 100,
        'visitas': [{
            'idEntrada': 12,
            'dni': 32333444,
            'precio': 60,
            'numeroDeTarjeta': 3,
            'fecha': '2018-04-25 10:10:00'
        }],
        'totalImporte': 60,
        'cantidadVisitas': 1
    }, {
        'idAtraccion': 4,
        'nombre': 'Twister',
        'precio': 40,
        'minimoEdad': 7,
        'minimoAltura': 90,
        'visitas': [{
            'idEntrada': 13,
            'dni': 32333444,
            'precio': 40,
            'numeroDeTarjeta': 3,
            'fecha': '2018-04-25 10:50:00'
        }],
        'totalImporte': 40,
        'cantidadVisitas': 1
    }],
    'visitas': [{
        'idEntrada': 11,
        'dni': 32333444,
        'precio': 300,
        'numeroDeTarjeta': 3,
        'fecha': '2018-04-25 09:00:00'
    }]
}).run()

# Facturas
r.table('facturas').insert({
    'numeroDeFactura': 1,
    'dni': 13241345,
    'fecha': '2017-02-01',
    'monto': 210,
    'entradas': [{
        'idEntrada': 1,
        'precio': 100
    }, {
        'idEntrada': 2,
        'precio': 50
    }, {
        'idEntrada': 3,
        'precio': 50
    }]
}).run()
r.table('facturas').insert({
    'numeroDeFactura': 2,
    'dni': 13241345,
    'fecha': '2017-03-01',
    'monto': 220,
    'entradas': [{
        'idEntrada': 4,
        'precio': 100
    }, {
        'idEntrada': 5,
        'precio': 20
    }, {
        'idEntrada': 6,
        'precio': 60
    }, {
        'idEntrada': 7,
        'precio': 20
    }, {
        'idEntrada': 8,
        'precio': 20
    }]
}).run()
r.table('facturas').insert({
    'numeroDeFactura': 3,
    'dni': 24356543,
    'fecha': '2017-05-01',
    'monto': 2000,
    'entradas': [{
        'idEntrada': 9,
        'precio': 1000
    }, {
        'idEntrada': 10,
        'precio': 1000
    }]
}).run()

# r.table('clientes').rebalance().run()
