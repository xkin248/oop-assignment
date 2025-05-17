import pyodbc

# Connection string configuration
def get_connection():
    conn_str = (
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=tcp:stdbst.database.windows.net,1433;"
        "Database=STDB;"
        "Uid=Henry;"
        "Pwd=Hello123;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    return pyodbc.connect(conn_str)
