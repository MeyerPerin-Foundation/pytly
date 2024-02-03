from pytly import pytly
from dotenv import load_dotenv
import os
import csv
# Create a new instance of Pytly

load_dotenv()
api_key = os.getenv("TLY_API_KEY")

with open('pexels.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        short_id = row[0]
        url = row[1]
        response = pytly.create_short_link(api_key, url, f"skv_{short_id}", "l.meyerperin.com")
        print(response)

