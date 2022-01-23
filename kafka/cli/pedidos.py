from datetime import datetime, timedelta
import random
import click

import psycopg2

from constantes import DBHOST, DBNAME, DBUSER, DBPASSWD


@click.group()
def pedidos():
    """
        Comandos da tabela pedidos.
    """


@pedidos.command()
@click.option("--count", "-c", default=5, help="Numero de pedidos a serem inseridos. Default = 5.")
def inserir(count: int):
    """
        Inserir dados mock.
    """
    with psycopg2.connect(host=DBHOST,
                          dbname=DBNAME,
                          user=DBUSER,
                          password=DBPASSWD) as conn:

        with conn.cursor() as cursor:
            cursor.executemany("INSERT INTO pedidos (data_criacao, id_cliente) VALUES (%s, %s)", gerar_pedidos(count))

            # Make the changes to the database persistent
            conn.commit()


@pedidos.command()
def listar():
    """
        Listar dados da tabela de pedidos.
    """
    with psycopg2.connect(host=DBHOST,
                          dbname=DBNAME,
                          user=DBUSER,
                          password=DBPASSWD) as conn:

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pedidos")
            for record in cursor.fetchall():
                click.echo(record)


def gerar_pedidos(num_pedidos: int):
    pedidos = []
    for _ in range(num_pedidos):
        data_pedido = gerar_data_random().strftime("%Y-%m-%d %H:%M:%S")
        id_cliente = random.randint(1, 5)
        pedidos.append((data_pedido, id_cliente))

    return pedidos


def gerar_data_random(start: str = "2021-01-01 00:00:00",
                      end: str = "2022-02-28 23:59:59",
                      fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    start = datetime.strptime(start, fmt)
    end = datetime.strptime(end, fmt)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds

    random_second = random.randrange(int_delta)

    return start + timedelta(seconds=random_second)
