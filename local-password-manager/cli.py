import click
import logging

@click.group()
def cli():
    pass

@click.command()
def create_file():
    logging.info("Creating file.")

    logging.info("Created file.")

@click.command()
def add_password():
    logging.info("Adding password.")

    logging.info("Added password.")

@click.command()
def delete_password():
    logging.info("Deleting password.")

    logging.info("Deleted password.")

@click.command()
def load_password():
    logging.info("Loading password.")
    
    logging.info("Loaded password.")


logging.basicConfig(level=logging.INFO)

cli.add_command(create_file)
cli.add_command(add_password)
cli.add_command(delete_password)
cli.add_command(load_password)

if __name__ == '__main__':
    cli()
