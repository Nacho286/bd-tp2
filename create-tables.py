import rethinkdb as r
tablelist = ['clientes', 'facturas', 'eventos', 'parques']

r.connect('localhost', 28015, db='tp2').repl()

# Crear base de datos
databases = r.db_list().run()
if 'tp2' not in databases:
    print 'creando bd'
    r.db_create('tp2').run()

# Crear tablas
tables = r.table_list().run()
for table in tablelist:
    if table not in tables:
        print 'creando tabla: ' + table
        r.table_create(table).run()
