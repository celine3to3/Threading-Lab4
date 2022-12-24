# Celine Phan
# Lab 4 Threading

import threading
import FileStream
import Database
import Parser
import Extract
import Plot

connection = None

fs = FileStream.FileStream('https://gml.noaa.gov/aggi/aggi.html')
urlData = fs.retrieve_data()

p = Parser.Parser(urlData)
columnsLists = p.parseTable()
years = columnsLists[0]
years = [int(i) for i in years]
encapsulatedYears = [years]
# print("testing")
# print(encapsulatedYears)

db = Database.Database()
db.createTable()
db.insertData(columnsLists)

retrievedData = []


def extract(lock, listId):
    lock.acquire()
    e = Extract.Extract(years, db)
    # retrieveData in Extract class uses a loop to repeatedly request cell data and appends them to a list
    data = e.retrieveData(listId)     # accesses the database and method returns the list
    retrievedData.append(data)   # append list to 2d array
    lock.release()


the_lock = threading.Lock()
t1 = threading.Thread(target=extract, args=(the_lock, 1))
t2 = threading.Thread(target=extract, args=(the_lock, 2))
t3 = threading.Thread(target=extract, args=(the_lock, 3))
t4 = threading.Thread(target=extract, args=(the_lock, 4))
t5 = threading.Thread(target=extract, args=(the_lock, 5))
t6 = threading.Thread(target=extract, args=(the_lock, 6))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()


p = Plot.Plot(years)
p.plot(retrievedData)   # list of 6 lists of collected data, one list for each chemical
print("All data plotted")
