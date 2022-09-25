import json
import logging

class passwordManager:
    def __init__(self, path):
        logging.basicConfig(level=logging.INFO)
        
        self.path = path

    def create_file(self):
        with open('{}/passwords_file.json'.format(self.path), 'w') as f:
            logging.info("File created.")