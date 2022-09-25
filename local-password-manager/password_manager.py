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

    def add_password(self, master_password, website, url, username, password, path):
        encrypted_password = cryptographic_algorithms.encrypt_password(master_password, password)
        encrypted_password_string = str(encrypted_password)

        password_dict = {
            "website": url,
            "username": username,
            "password": encrypted_password_string
        }

        with open('{}/passwords_file.json'.format(path), 'r') as f:
            try:
                json_data = json.load(f)
                json_data.update({website: password_dict})
                with open('{}/passwords_file.json'.format(path), 'w') as outfile:
                    json.dump(json_data, outfile)
            except JSONDecodeError:
                with open('{}/passwords_file.json'.format(path), 'w') as outfile:
                    json.dump({website: password_dict}, outfile)

    def retrieve_passwords(self, website, master_password, path):
        with open('{}/passwords_file.json'.format(path), 'r') as f:
            json_data = json.load(f)

        json_data[website]['password'] = cryptographic_algorithms.decrypt_password(master_password, json_data[website]['password'])

        return json_data[website]