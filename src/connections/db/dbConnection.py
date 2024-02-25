import mysql.connector
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Replace these values with your own database information
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("dataBase")

# Establish a connection to the MySQL server


def insertMetaData(rawJSON):

    parsed_data = json.loads(rawJSON)
    
    connection = mysql.connector.connect(host=host,user=user,password=password,database=database)
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Replace 'your_table' with the actual table name
    table_name = "Metadata"

    # Example data to insert
    data_to_insert = {
        "MAQUINA":parsed_data["Maquina"],
        "ID": parsed_data["id"],
        "CPU": parsed_data["CPU"],
        "MEMORIA": parsed_data["Memoria"],
        "RECEPCION": parsed_data["Recepcion"],
        "DISCO": parsed_data["Disco"],
        "inserDT": parsed_data["inserDT"],
    }

    # Build the SQL INSERT statement
    insert_query = f"INSERT INTO {table_name} ({', '.join(data_to_insert.keys())}) VALUES ({', '.join(['%s']*len(data_to_insert))})"

    # Execute the query with the data
    cursor.execute(insert_query, tuple(data_to_insert.values()))

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()