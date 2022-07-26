import random
from typing import Iterator

from prettytable import PrettyTable
import click
import psycopg2

from config import DBHOST
from config import DBNAME
from config import DBPASSWD
from config import DBUSER
from utils import gerar_data


@click.group()
def pedidos():
    """
        Comandos da tabela pedidos.
    """


@pedidos.command()
@click.option("--count", "-c", default=5, help="Numero de pedidos a serem inseridos.", show_default=True)
@click.option("--max_id_cliente", "-m", default=5, help="Id máximo do cliente para geração dos pedidos.", show_default=True)
@click.pass_context
def inserir(ctx, count: int, max_id_cliente: int):
    """
        Inserir dados mock na tabela de pedidos.
    """
    with psycopg2.connect(
        host=DBHOST,
        dbname=DBNAME,
        user=DBUSER,
        password=DBPASSWD,
    ) as conn:

        with conn.cursor() as cursor:
            cursor.executemany("INSERT INTO pedidos (data_criacao, id_cliente)"
                               "VALUES (%s, %s)", gerar_pedidos(count, max_id_cliente))

            # Make the changes to the database persistent
            conn.commit()

    ctx.invoke(listar)


@pedidos.command()
def listar():
    """
        Listar dados da tabela de pedidos.
    """
    with psycopg2.connect(
        host=DBHOST,
        dbname=DBNAME,
        user=DBUSER,
        password=DBPASSWD,
    ) as conn:

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pedidos")

            table = PrettyTable()
            table.field_names = [i[0] for i in cursor.description]

            for record in cursor.fetchall():
                table.add_row(record)

            click.echo(table)


def gerar_pedidos(num_pedidos: int, max_id_cliente: int) -> Iterator[tuple]:
    for _ in range(num_pedidos):
        data_pedido = gerar_data()
        id_cliente = random.randint(1, max_id_cliente)
        yield (data_pedido, id_cliente)
