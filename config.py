import pyodbc

SQLQUERRY = """SELECT *
FROM Пациент"""


def connectDB():
    connectionString = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-C53MJSE;'
        r'DATABASE=Больница;'
        r'Trusted_Connection=yes;')

    connect = pyodbc.connect(connectionString)
    if(connect):
        print("success")
    else:
        print("no connection")
