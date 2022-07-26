from typing import Iterator
import click
import random

from prettytable import PrettyTable
import psycopg2

from config import DBHOST, DBNAME, DBUSER, DBPASSWD


@click.group()
def entregas():
    """
        Comandos da tabela entregas.
    """


@entregas.command()
@click.option("--count", "-c", default=5, help="Numero de entregas a serem registradas.", show_default=True)
@click.option("--max_id_pedido", "-m", default=5, help="Id máximo do pedido para geração das entregas.", show_default=True)
@click.pass_context
def inserir(ctx, count: int, max_id_pedido: int):
    """
        Inserir dados mock na tabela de entregas.
    """
    with psycopg2.connect(
        host=DBHOST,
        dbname=DBNAME,
        user=DBUSER,
        password=DBPASSWD,
    ) as conn:

        with conn.cursor() as cursor:
            cursor.executemany("INSERT INTO entregas (status, id_pedido) "
                               "VALUES (%s, %s)", gerar_entregas(count, max_id_pedido))

            # Make the changes to the database persistent
            conn.commit()

    ctx.invoke(listar)


@entregas.command()
def listar():
    """
        Listar dados mock da tabela de entregas.
    """
    with psycopg2.connect(
        host=DBHOST,
        dbname=DBNAME,
        user=DBUSER,
        password=DBPASSWD,
    ) as conn:

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM entregas")

            table = PrettyTable()
            table.field_names = [i[0] for i in cursor.description]

            for record in cursor.fetchall():
                table.add_row(record)

            click.echo(table)


def gerar_entregas(count: int, max_id_pedido: int) -> Iterator[tuple]:
    for _ in range(count):
        status = random.choice(
            ["Em transito", "Em processamento", "Entregue", "Aguardando retirada", "A entrega não pode ser efetuada"]
        )
        id_pedido = random.randint(1, max_id_pedido)
        yield (status, id_pedido)
