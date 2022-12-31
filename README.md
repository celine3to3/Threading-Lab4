# Threading-Lab4
Scrapes data from https://gml.noaa.gov/aggi/aggi.html and stores it in a SQLite database.

Creates 6 threaded agents for the Global Radiative Forcing annual values. These agents extract the yearly data one at a time over the range 1990 thru 2019.

Threading rules:

    Only one threaded agent can access the database at a time. 

    The database inquiry only requests one cell of data per request. 

    The agents must make repeated requests for yearly data. 
  
After collecting the data, 6 plots pop up to display the linear regression for each gas using Matplotlib.

Output of program:
![plot output](https://user-images.githubusercontent.com/121079918/210127790-dab79da7-48e2-492f-a946-5167d440da6f.png)

Preview of database:
![database preview lab4](https://user-images.githubusercontent.com/121079918/210127920-d75836b8-5bd7-4b20-ba33-bf84e9c24982.png)
