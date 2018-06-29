#!/bin/bash
mkdir -p shards
mkdir -p shards/node0
mkdir -p shards/node1
mkdir -p shards/node2
mkdir -p shards/node3

echo 'Iniciando shards'
echo '------ PRESIONE UNA TECLA EN CUALQUIER MOMENTO PARA FINALIZAR -------'
sleep 2
(
  rethinkdb --directory shards/node0 --server-name tp2_node0 --pid-file shards/n0.pid &
  rethinkdb --port-offset 1 --directory shards/node1 --server-name tp2_node1 --join localhost:29015 --pid-file shards/n1.pid &
  rethinkdb --port-offset 2 --directory shards/node2 --server-name tp2_node2 --join localhost:29015 --pid-file shards/n2.pid &
  rethinkdb --port-offset 3 --directory shards/node3 --server-name tp2_node3 --join localhost:29015 --pid-file shards/n3.pid &
) &

read
echo 'Finalizando shards'
echo "-- Finaliza pid $(cat shards/n0.pid)"
kill $(cat shards/n0.pid)
echo "-- Finaliza pid $(cat shards/n1.pid)"
kill $(cat shards/n1.pid)
echo "-- Finaliza pid $(cat shards/n2.pid)"
kill $(cat shards/n2.pid)
echo "-- Finaliza pid $(cat shards/n3.pid)"
kill $(cat shards/n3.pid)
echo 'Shards finalizados'
