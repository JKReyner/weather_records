import pandas as pd
import requests  # Import the library for sending requests to the server
import re
from bs4 import BeautifulSoup  # Import the library for webpage parsing
import json

url = 'https://code.s3.yandex.net/data-analyst-eng/chicago_weather_2017.html'
req = requests.get(url)  # GET-request
soup = BeautifulSoup(req.text, 'lxml')
heading_table = []

for row in soup.find_all(
    'th'
):  heading_table.append(
        row.text
    )

entries_table = []
for row in soup.find_all(
    'td'
):  entries_table.append(
        row.text
    )

content = []  # list where the table data will be stored
for row in soup.find_all('tr'):
    # Each row is wrapped in a <tr> tag, we need to loop through all the rows
    if not row.find_all('th'):
        # We need this condition to ignore the first row of the table, with headings
        content.append([element.text for element in row.find_all('td')])
        # Within each row the cell content is wrapped in <td> </td> tags
        # We need to loop through all <td> elements, extract the content from the cells, and add it to the list
        # Then add each of the lists to the content list
        
weather_records = pd.DataFrame(content, columns=heading_table)

print(weather_records)
