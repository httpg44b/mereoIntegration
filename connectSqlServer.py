import pyodbc as db
import os
from dotenv import load_dotenv
from getHistoryPosition import querySQL

load_dotenv()

SERVER = os.getenv('SERVER')
DATABASE = os.getenv('DATABASE')
USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

print(f'Conexão ao servidor {SERVER} feita')


def setup():
 connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
 conn = db.connect(connectionString)
 return conn