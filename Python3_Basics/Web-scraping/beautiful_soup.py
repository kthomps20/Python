import requests
from bs4 import BeautifulSoup
import pandas as pd
#url in LinkedIn search for companies hiring, the role, position seniority

url = 'https://www.linkedin.com/jobs/search/?geoId=102356711&keywords=data%20scientist&location=Cleveland%2C%20Ohio%2C%20United%20States'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")
print(soup)
job_title = (soup.h3)

for job in job_title:
    print(job)

job_company = (soup.find_all('h4'))
job_location = (soup.find_all('span'))
