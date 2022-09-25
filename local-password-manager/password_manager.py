import json
import logging

import cryptographic_algorithms

class passwordManager:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def create_file(self, path):
        with open('{}/passwords_file.json'.format(path), 'w') as f:
            logging.info("File created.")

    def add_password(self, master_password, website, username, password):
        password_dict = {
            "website": website,
            "username": username,
            "password": password
        }
