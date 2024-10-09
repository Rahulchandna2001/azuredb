import mysql.connector
from mysql.connector import Error

def execute_sql_script(update_companydb_schema.sql):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='your-host',
            database='your-database',
            user='your-username',
            password='your-password'
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
    execute_sql_script('update_companydb_schema.sql')
