import os
from dotenv import load_dotenv

load_dotenv()

CLIENT = os.getenv('CLIENT')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

print(CLIENT, CLIENT_SECRET)