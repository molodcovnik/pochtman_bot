import os
from dotenv import load_dotenv
import logging


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


logging.basicConfig(filename='info.log', level=logging.INFO)


# Environments
token = os.getenv('token')
token_api = os.getenv('token_api')
base_url = os.getenv('base_url')
url = os.getenv('url')
