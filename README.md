# weather_records
Study of a database to analyze patterns in passanger preferences for a ride-sharing company. It aims to analyze data from competitors, and hypothesis test on the impact of weather on ride frequency.

The files in the commit, in the order that they are relevant:

* create_dataframe.py: A Python code that performs web scraping against the database page to retrieve information.
* project_sql_results.txt: A list of SQL queries that check and analyze the scraped dataframe. Outputs into three different CSV files.
  * project_sql_result_1.csv: Contains taxi company name
  * project_sql_result_4.csv: Contains Chicago neighborhoods where rides ended
  * project_sql_result_7.csv: Contains pickup date/time, weather conditions at the time the ride started (set as good or bad), and ride duration (in seconds).
* weather_records.ipynb: Notebook of visualization and analysis.
