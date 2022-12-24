import sqlite3
class Database:
    global connection
    connection = sqlite3.connect('Data.db', check_same_thread=False)

    def __init__(self):
        self.db = connection
        self.cursor = connection.cursor()
        self.database = ''

    def createTable(self):
        global connection
        c = connection.cursor()
        c.execute('''
           CREATE TABLE if not exists aggi_data(
               years numeric, 
               co2 numeric,
               ch4 numeric,
               n2o numeric,
               cfc numeric,
               hcfc numeric,
               hfc numeric   
           )''')
        connection.commit()

        print("\nDatabase created successfully!")

    def insertData(self, data):
        global connection
        c = connection.cursor()
        for i in range(len(data[0])):
            c.execute("INSERT INTO aggi_data VALUES (?, ?, ?, ?, ?, ?, ?)", (data[0][i], data[1][i], data[2][i], data[3][i], data[4][i], data[5][i], data[6][i]))
            connection.commit()


    def retrieveCell(self, year, column):
        # one cell of data is requested from a query at a time

        global connection
        c = connection.cursor()
        year = str(year)
        query1 = "SELECT co2 FROM aggi_data WHERE years = " + year + ""
        query2 = "SELECT ch4 FROM aggi_data WHERE years = " + year + ""
        query3 = "SELECT n2o FROM aggi_data WHERE years = " + year + ""
        query4 = "SELECT cfc FROM aggi_data WHERE years = " + year + ""
        query5 = "SELECT hcfc FROM aggi_data WHERE years = " + year + ""
        query6 = "SELECT hfc FROM aggi_data WHERE years = " + year + ""

        if column == 1:
            query = query1
        elif column == 2:
            query = query2
        elif column == 3:
            query = query3
        elif column == 4:
            query = query4
        elif column == 5:
            query = query5
        elif column == 6:
            query = query6

        c.row_factory = lambda cursor, row: row[0]
        c.execute(query)
        cellData = c.fetchone()
        # print("cellData =", cellData)
        return cellData