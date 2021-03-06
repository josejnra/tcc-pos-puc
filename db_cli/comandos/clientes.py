from typing import Iterator

import click
import psycopg2
from prettytable import PrettyTable

from config import DBHOST
from config import DBNAME
from config import DBPASSWD
from config import DBUSER
from utils import gerar_cidade
from utils import gerar_data
from utils import gerar_endereco
from utils import gerar_estado_sigla
from utils import gerar_nome_client


@click.group()
def clientes():
    """
        Comandos da tabela clientes.
    """


@clientes.command()
@click.option("--count", "-c", default=5, help="Numero de clientes a serem inseridos.", show_default=True)
@click.pass_context
def inserir(ctx, count: int):
    """
        Inserir dados mock na tabela de clientes.
    """
    with psycopg2.connect(
        host=DBHOST,
        dbname=DBNAME,
        user=DBUSER,
        password=DBPASSWD,
    ) as conn:

        with conn.cursor() as cursor:
            cursor.executemany(
                "INSERT INTO clientes (nome, endereco, cidade, estado, data_criacao) "
                "VALUES (%s, %s, %s, %s, %s)", gerar_clientes(count),
            )

            # Make the changes to the database persistent
            conn.commit()

    ctx.invoke(listar)


@clientes.command()
def listar():
    """
        Listar dados da tabela de clientes.
    """
    with psycopg2.connect(
        host=DBHOST,
        dbname=DBNAME,
        user=DBUSER,
        password=DBPASSWD,
    ) as conn:

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes")

            table = PrettyTable()
            table.field_names = [i[0] for i in cursor.description]

            for record in cursor.fetchall():
                table.add_row(record)

            click.echo(table)


def gerar_clientes(count: int) -> Iterator[tuple]:
    for _ in range(count):
        nome = gerar_nome_client()
        endereco = gerar_endereco()
        cidade = gerar_cidade()
        estado = gerar_estado_sigla()
        data_criacao = gerar_data()
        yield (nome, endereco, cidade, estado, data_criacao)
