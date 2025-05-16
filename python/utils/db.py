import sqlalchemy

# SQLAlchemy connection string (edit password if you change it)
connection_string = (
    "mssql+pyodbc://Henry:Mesopro123@"
    "sarawaktourismsqlserver.database.windows.net:1433/"
    "sarawktourismdb"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&encrypt=yes"
    "&trustServerCertificate=no"
)

engine = sqlalchemy.create_engine(connection_string)

# Example: test connection
with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT 1"))
    print(result.fetchone())