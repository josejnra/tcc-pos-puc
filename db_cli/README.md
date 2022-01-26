## DB CLI
Para gerar registros no banco de dados pode-se utilizar o CLI. Para isto, basta estar na raíz do [projeto](../) e executar os seguintes comandos:
```shell
python db_cli
```
Com o comando acima será apresentado todos os comandos disponíveis no CLI.

### Inserir novos clientes
```shell
python db_cli clientes inserir -c 10
```
Será inserido 10 novos clientes na base de dados.

### Inserir novos pedidos
```shell
python db_cli pedidos inserir -c 8
```
Será inserido 8 novos clientes na base de dados.

Para qualquer comando pode-se visualizar as opções disponíveis apenas passando a flag `-h` ou `--help`.
