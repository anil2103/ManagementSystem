from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()

connect = connector.connect(
     user ='root',
     password = 'root',
     host = 'localhost',
     database = 'management_db'
 )


cursor = connect.cursor()