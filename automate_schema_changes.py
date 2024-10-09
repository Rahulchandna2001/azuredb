import mysql.connector
from mysql.connector import Error

# Create the database connection directly
  connection = mysql.connector.connect(
    DB_HOST: ${{ secrets.DB_HOST }}
    DB_USER: ${{ secrets.DB_ADMIN_USER }}
    DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
    DB_NAME: ${{ secrets.DB_NAME }}
)


# Create a cursor object to execute SQL queries
cursor = connection.cursor() 

# Path to the SQL file
script_path = 'update_companydb_schema.sql'

# Read the SQL script from the file
with open(script_path, 'r') as file:
    sql_script = file.read()

# Execute each SQL statement individually (split by semicolon)
for statement in sql_script.split(';'):
    if statement.strip():  # Execute only non-empty statements
       cursor.execute(statement)

connection.commit()  # Commit all changes at once
cursor.close()  # Close the cursor
connection.close()  # Close the connection

print("Execution completed successfully")
