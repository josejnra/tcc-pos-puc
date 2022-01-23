import click

import psycopg2

from constantes import DBHOST, DBNAME, DBUSER, DBPASSWD


@click.group()
def entregas():
    """
        Comandos da tabela entregas.
    """


@entregas.command()
def listar():
    """
        Listar dados da tabela de entregas.
    """
    with psycopg2.connect(host=DBHOST,
                          dbname=DBNAME,
                          user=DBUSER,
                          password=DBPASSWD) as conn:

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM entregas")
            for record in cursor.fetchall():
                click.echo(record)


def update_entregas_status():
    # Connect to an existing database
    with psycopg2.connect(host=DBHOST,
                          dbname=DBNAME,
                          user=DBUSER,
                          password=DBPASSWD) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cursor:
            print("PostgreSQL server information")
            print(conn.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute("SELECT version();")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

            # the correct conversion (no SQL injections!)
            # cur.execute(
            #     "INSERT INTO test (num, data) VALUES (%s, %s)",
            #     (100, "abc'def"))

            cursor.execute("SELECT * FROM pedidos")
            for record in cursor.fetchall():
                print(record)

            cursor.execute(
                "INSERT INTO pedidos (data_criacao, id_cliente) VALUES (%s, %s)",
                ('2022-01-04 12:34:34', 1))

            cursor.execute(
                "UPDATE pedidos SET data_criacao = %s, id_cliente = %s WHERE id = 2",
                ('2022-01-04 12:34:34', 1))

            cursor.execute("SELECT * FROM pedidos")
            for record in cursor.fetchall():
                print(record)

            # Make the changes to the database persistent
            conn.commit()
