import pyodbc
import bcrypt
from datetime import datetime

# --- Database Connection ---
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

# --- User Registration Data ---
username = "john_doe"
email = "john@example.com"
password_plain = "securepassword123"
gender = "male"  # Ensure your app enforces values like: 'male', 'female', 'other'

# --- Hash Password ---
password_hashed = bcrypt.hashpw(password_plain.encode(), bcrypt.gensalt()).decode()

# --- Current Time (for created_at) ---
created_at = datetime.now()

# --- Insert into SQL Server ---
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO dbo.Users (username, email, password, gender, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (username, email, password_hashed, gender, created_at))

    conn.commit()
    print("✅ User registered successfully.")

except pyodbc.IntegrityError as e:
    print("❌ Registration failed: Username or email might already exist.")
except Exception as e:
    print("❌ Registration error:", e)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
