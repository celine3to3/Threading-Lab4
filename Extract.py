class Extract:
    def __init__(self, years, database):
        self.years = years
        self.database = database

    def retrieveData(self, columnNumber):
        # repeatedly access database and get one cell of data at a time for each year
        list = []
        for i in self.years:
            cellData = self.database.retrieveCell(i, columnNumber)
            list.append(cellData)
        # print(list)
        return list