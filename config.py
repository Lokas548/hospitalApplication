import pyodbc

def connectDB():
    connectionString = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=KOMPUTER;'
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

def findEmployee(data):
    if(data[0] == "id_сотрудника"):
        SQLQUERRY = f"""SELECT *
        FROM Сотрудник
        WHERE {data[0]} = {data[1]}"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "НаименованиеОтделение"):
        print(9)
        SQLQUERRY = f"""SELECT *
                FROM Сотрудник
                WHERE id_отделения = (SELECT id_отделения
                FROM Отделение
                WHERE Отделение.Наименование = N'{data[1]}')"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif(data[0] == "НаименованиеДолжность"):
        print(9)
        SQLQUERRY = f"""SELECT *
        FROM Сотрудник
        WHERE id_должности = (SELECT id_должности
        FROM Должность
        WHERE Должность.Наименование = N'{data[1]}')"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif(data[0] == "Наименование"):
        SQLQUERRY = f"""SELECT *
            FROM Сотрудник
            WHERE {data[0]} = {data[1]}"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "ФИО"):
        SQLQUERRY = f"""SELECT *
                FROM Сотрудник
                WHERE Фамилия = N'{data[1]}' and Имя = N'{data[2]}' and Отчество = N'{data[3]}'"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    if(data[0] == "*"):
        SQLQUERRY = f"""SELECT *
        FROM Сотрудник"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows

def findEmployeeColumns():
    list = []
    for row in cursor.columns(table='Сотрудник'):
        list.append(row.column_name)

    return list

def findPatient(data):
    if(data[0] == "id_пациента"):
        SQLQUERRY = f"""SELECT *
        FROM Пациент
        WHERE {data[0]} = {data[1]}"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "ФИО"):
        SQLQUERRY = f"""SELECT *
                FROM Пациент
                WHERE Фамилия = N'{data[1]}' and Имя = N'{data[2]}' and Отчество = N'{data[3]}'"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    elif (data[0] == "Номер_полиса"):
        SQLQUERRY = f"""SELECT *
            FROM Пациент
            WHERE {data[0]} = '{data[1]}'"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    if (data[0] == "*"):
        SQLQUERRY = f"""SELECT *
            FROM Пациент"""
        rows = connection.cursor().execute(SQLQUERRY).fetchall()
    return rows

def findPatientColumns():
    list = []
    for row in cursor.columns(table='Пациент'):
        list.append(row.column_name)

    return list




