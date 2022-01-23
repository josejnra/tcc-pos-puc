import click

from constantes import CONTEXT_SETTINGS
from entregas import entregas
from pedidos import pedidos


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
        Script utilizado para gerar dados mock no banco de dados.
    """


cli.add_command(pedidos)
cli.add_command(entregas)


if __name__ == '__main__':
    cli()
