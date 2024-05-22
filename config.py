import pyodbc

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
    return connect

connection = connectDB()
cursor = connection.cursor()

def findEmployee():
    SQLQUERRY = """SELECT *
    FROM Сотрудник"""
    rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows

def findEmployeeColumns():
    list = []
    for row in cursor.columns(table='Сотрудник'):
        list.append(row.column_name)

    return list



findEmployeeColumns()



