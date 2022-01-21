## Executando

### Conector Source
Após executar o `docker-compose`, deve-se criar o conector source com o seguinte comando abaixo:
```bash
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connect-source.json 
```

### Conector Sink
Deve-se criar o bucket `lake-raw-zone` no [minio](http://localhost:9001). Após isto, execute o comando abaixo:
```bash
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @connect-sink.json 
```
