# Threading-Lab4
Scrape data from https://gml.noaa.gov/aggi/aggi.html and store in SQLite database.

Create 6 threaded agents for the Global Radiative Forcing annual values. These agents extract the yearly data one at a time over the range 1990 thru 2019.

Threading rules:
  Only one threaded agent can access the database at a time. 
  The database inquiry only requests one cell of data per request. 
  The agents must make repeated requests for yearly data. 
  
After collecting the data, plot the liner regression for each gas using either Matplotlib or Plotly.
