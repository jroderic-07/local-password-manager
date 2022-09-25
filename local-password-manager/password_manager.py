import json
import logging
from json.decoder import JSONDecodeError

import cryptographic_algorithms

class passwordManager:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def create_file(self, path):
        with open('{}/passwords_file.json'.format(path), 'w') as f:
            logging.info("File created.")

    def add_password(self, master_password, website, username, password, path):
        encrypted_password = cryptographic_algorithms.encrypt_password(master_password, password)
        encrypted_password_string = str(encrypted_password)

        password_dict = {
            "website": website,
            "username": username,
            "password": encrypted_password_string
        }

        with open('{}/passwords_file.json'.format(path), 'r') as f:
            try:
                json_data = json.load(f)
                json_data.append({"test": password_dict})
                with open('{}/passwords_file.json'.format(path), 'w') as outfile:
                    json.dump(json_data, outfile)
            except JSONDecodeError:
                with open('{}/passwords_file.json'.format(path), 'w') as outfile:
                    json.dump([{"test": password_dict}], outfile)
