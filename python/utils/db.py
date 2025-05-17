import pyodbc
import bcrypt
from datetime import datetime

# --- Configuration ---
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

def create_connection():
    try:
        connection = pyodbc.connect(conn_str)
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()

def query_db(query, args=(), fetch_one=False, commit=False):
    """
    Execute a SQL query. 
    - For SELECT: returns list of dicts (or single dict if fetch_one=True)
    - For INSERT/UPDATE/DELETE: returns lastrowid if commit=True, else nothing
    """
    conn = create_connection()
    if not conn:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute(query, args)
        if commit:
            conn.commit()
            try:
                # For SQL Server, get last inserted ID
                cursor.execute("SELECT SCOPE_IDENTITY()")
                row = cursor.fetchone()
                return row[0] if row else None
            except Exception:
                return None
        else:
            columns = [column[0] for column in cursor.description] if cursor.description else []
            if fetch_one:
                row = cursor.fetchone()
                if not row:
                    return None
                return dict(zip(columns, row))
            else:
                rows = cursor.fetchall()
                return [dict(zip(columns, r)) for r in rows]
    except pyodbc.IntegrityError:
        print("Integrity error: likely duplicate key/unique constraint.")
        return None
    except Exception as e:
        print(f"Database query error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
