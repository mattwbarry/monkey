import click

from .typewriter import MonkeyTypewriter

@click.group()
def cli():
    """
    This is a command line tool to monkeying around.
    """
    pass


@cli.command(name='write')
# @click.option('-r', '--random', is_flag=True,
#               help='Generate characters from a true random generation instead of a weighted spread.')
# @click.option('-w', '--work', default='Hamlet',
#               help='Name of one of Shakespeare\'s work to monkey on.')
@click.option('-u', '--upper', is_flag=True,
              help='Flag to treat upper and lowercase a separate')
@click.option('-s', '--spaces', is_flag=True,
              help='Flag to include spaces in text')
@click.option('-p', '--punctuation', is_flag=True,
              help='Flag to include punctuation in text')
def do_the_monkey(upper, spaces, punctuation):
    """

    :return:
    """
    writer = MonkeyTypewriter(upper, spaces, punctuation)
    writer.monkey_type()


if __name__ == '__main__':
    cli()