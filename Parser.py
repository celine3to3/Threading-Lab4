from bs4 import BeautifulSoup

class Parser:
    def __init__(self, data):
        self.data = data
        self.soup = BeautifulSoup(self.data.text, "html.parser")
        self.table = self.soup.find("table", {"class": "table table-bordered table-condensed table-striped table-header"})

    def parseTable(self):
        table_data = []
        wiki_table = self.table.find_all("td")
        for data in wiki_table:
            data.get('td')
            table_data.append(data.text)
        length = len(table_data)
        years = table_data[0:length:11]
        co2 = table_data[1:length:11]
        ch4 = table_data[2:length:11]
        n2o = table_data[3:length:11]
        cfc = table_data[4:length:11]
        hcfc = table_data[5:length:11]
        hfc = table_data[6:length:11]


        '''print(years)
        print(co2)
        print(ch4)
        print(n2o)
        print(cfc)
        print(hcfc)
        print(hfc)'''

        return years, co2, ch4, n2o, cfc, hcfc, hfc