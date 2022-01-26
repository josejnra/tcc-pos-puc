import click

from comandos.clientes import clientes
from comandos.entregas import entregas
from comandos.pedidos import pedidos


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
def cli():
    """
        Script utilizado para gerar dados mock no banco de dados.
    """


cli.add_command(pedidos)
cli.add_command(entregas)
cli.add_command(clientes)
