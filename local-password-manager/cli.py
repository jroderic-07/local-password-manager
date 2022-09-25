import click
import logging

import password_manager

@click.group()
def cli():
    pass

@click.command()
@click.argument('path')
def create_file(path):
    logging.info("Creating file.")

    pm = password_manager.passwordManager()
    pm.create_file(path)

    logging.info("Created file.")

@click.command()
@click.argument('master_password')
@click.argument('website')
@click.argument('username')
@click.argument('password')
def add_password(master_password, website, username, password):
    logging.info("Adding password.")

    pm = password_manager.passwordManager()
    pm.add_password(master_password, website, username, password)

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
