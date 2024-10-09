import mysql.connector
from mysql.connector import Error
import os

def execute_sql_script(sql_file_path):
    try:
        # Connect to the MySQL database using secrets stored in environment variables
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),          # The MySQL host
            user=os.getenv('DB_USER'),          # The MySQL user
            password=os.getenv('DB_PASSWORD'),  # The MySQL password
            database=os.getenv('DB_NAME')       # The MySQL database name
        )
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Open and read the SQL file
            with open(sql_file_path, 'r') as sql_file:
                sql_script = sql_file.read()

            # Execute each command in the script
            for command in sql_script.split(';'):
                if command.strip():
                    cursor.execute(command)

            # Commit the changes
            connection.commit()
            print("Schema changes applied successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    # Provide the correct SQL file path when calling the function
    execute_sql_script('azuredb/update_companydb_schema.sql')
