# db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
SSL_CERT = os.environ.get("SSL_CERT", "DigiCertGlobalRootCA.crt.pem")

# Build MySQL connection string with SSL
connection_string = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    f"?ssl_ca={SSL_CERT}"
)

# Create SQLAlchemy engine and session
engine = create_engine(connection_string, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Optional: function to run raw SQL queries
def query_db(query, params=(), fetch_one=False):
    with engine.connect() as conn:
        result = conn.execute(query, params)
        return result.fetchone() if fetch_one else result.fetchall()
