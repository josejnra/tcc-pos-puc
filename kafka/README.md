## Requisitos
Para poder executar este projeto deve-se ter instalado o [docker](https://www.docker.com/) e o 
[docker-compose](https://docs.docker.com/compose/).

## Executando

Para executar o kafka e os demais serviços, basta rodar o seguinte comando:
```bash
docker-compose up -d 
```

Após isto, estará disponível os seguintes serviços:
- kafka
- kafka-connect
- control center, acessível em [http://localhost:9092](http://localhost:9021)
- postgres, com interface web em [http://localhost:8080](http://localhost:8080). Credenciais disponíveis no [docker-compose.yaml](docker-compose.yaml).
- minio, interface web acessível em  [http://localhost:9000](http://localhost:8080). Credenciais disponíveis no [docker-compose.yaml](docker-compose.yaml).

### Conector Source
Após executar o `docker-compose`, deve-se criar o conector source, que irá buscar registros no banco de dados e 
enviar para os tópicos kafka, com o seguinte comando abaixo:
```bash
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connect-source.json 
```

### Conector Sink
> Deve-se criar um bucket com o nome `lake-raw-zone` no [minio](http://localhost:9001).

Após isto, execute o comando abaixo para poder criar o agente responsável pela escrita no bucket:
```bash
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connect-sink.json 
```


### Zookeeper
Entre dentro do container `kafka-zookeeper`:
```shell
docker container exec -it kafka-zookeeper bash
```

Execute o seguinte comando para listar brokers disponíveis no cluster:
```shell
zookeeper-shell zookeeper:2181 ls /brokers/ids
```

Para mais detalhes de um broker:
```shell
zookeeper-shell zookeeper:2181 get /brokers/ids/1
```

### Kafka Connect
Entre dentro do container `kafka-connect`:
```shell
docker container exec -it kafka-connect bash
```
Execute o seguinte comando para listar brokers disponíveis no cluster:
```shell
kafka-broker-api-versions --bootstrap-server kafka-broker1:29092 | awk '/id/{print $1}'
```
Descrever um tópico:
```shell
kafka-topics --describe --topic dbserver1.public.pedidos --bootstrap-server kafka-broker1:29092
```
