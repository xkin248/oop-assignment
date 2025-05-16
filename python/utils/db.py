import sqlalchemy

server = 'sarawaktourismsqlserver.database.windows.net'
database = 'sarawktourismdb'
username = 'Henry'
password = 'Mesopro123'
driver = 'ODBC Driver 17 for SQL Server'

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:1433/"
    f"{database}?driver={driver.replace(' ', '+')}"
)
engine = sqlalchemy.create_engine(connection_string)

# Run all SQL commands in database.sql
with open('database.sql', 'r', encoding='utf-8') as sql_file:
    sql_commands = sql_file.read()

with engine.connect() as conn:
    for command in sql_commands.split(';'):
        cmd = command.strip()
        if cmd:
            conn.execute(sqlalchemy.text(cmd))

print("Database initialized successfully!")