import pyodbc

server_name = "thai-server.database.windows.net"
database_name = "Project-BwiBOW"
username = "bwibow"
password = "Thanawat3009"

try:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server_name};"
        f"DATABASE={database_name};"
        f"UID={username};"
        f"PWD={password};"
    )
    cursor = conn.cursor()
    print("Connected to Azure SQL Database")

    # Now you can execute SQL queries using the 'cursor' object

    # For example, you can retrieve data from a table
    cursor.execute("SELECT * FROM dbo.Member")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Don't forget to close the cursor and the connection when you're done
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", str(e))
