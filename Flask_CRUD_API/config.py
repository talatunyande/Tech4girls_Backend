from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
database_username = os.getenv("DB_USERNAME")
database_password = os.getenv("DB_PASSWORD")
database_name = os.getenv('DB_NAME')

#print(database_username, database_password, database_name)

connection_str = f'mysql+mysqlconnector://{database_username}:{database_password}@localhost/{database_name}'


engine = create_engine(connection_str)


try:
    # Try to establish a connection
    connection = engine.connect()
    print('Located and connected to database')
    connection.close()
except Exception as e:
    # Print the error message if something goes wrong
    print(f'An error occurred: {e}')

# Create a session factory and then an instance of the session
DBSession = sessionmaker(bind=engine)
session = DBSession()

