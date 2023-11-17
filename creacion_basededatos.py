import requests
url = "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/Increased-monitoring-october-2023.html"
from bs4 import BeautifulSoup
response = requests.get(url)
if response.status_code == 200:
	soup = BeautifulSoup(response.text,"html.parser")

print(soup.title.text)