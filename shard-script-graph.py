import matplotlib.pyplot as plt
import csv


inputFile = 'shard-testing.csv'
outputFile = inputFile

entrada = csv.reader(open(inputFile, "rb"))

ejeCantidades = []
ejeUnaFila = []
ejeVariasFilas = []
ejeTodasFilas = []
linea = 0
for row in entrada:
    if linea > 0:
        ejeCantidades.append(row[0])
        ejeUnaFila.append(row[1])
        ejeVariasFilas.append(row[2])
        ejeTodasFilas.append(row[3])
    linea = linea + 1

plt.plot(ejeCantidades, ejeUnaFila)
plt.plot(ejeCantidades, ejeVariasFilas)
plt.plot(ejeCantidades, ejeTodasFilas)
plt.xlabel('Cantidad de filas')
plt.ylabel('Tiempo (ms)')
plt.title('Experimentacion con base de datos rethinkdb (3 shards)')
plt.legend(["Una fila", "Varias filas", "Todas las filas"], loc='right')

plt.savefig("shards-testing.png")
