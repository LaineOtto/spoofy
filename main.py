from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ.get('client_id'))
print(os.environ.get('client_secret'))
