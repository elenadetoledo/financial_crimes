"""Code by Elena de Toledo Hernández
Connection to FATF website to extract information about countries lised in their black and grey lists."""
import requests
from bs4 import BeautifulSoup

#I'll first analyze the black list:
high_risk = "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/Call-for-action-october-2023.html"
black_list_countries = []
#Connection to web page
response = requests.get(high_risk)
#Checking if connection is successful
if response.status_code == 200:
	blist = BeautifulSoup(response.text,"html.parser")
else:
	print("Error connecting wiht the web page")
#After inspecting HTML code, I find that this is the structure followed in the web page 
h3_tags = blist.find_all('h3')

for h3_tag in h3_tags:
	country_name = h3_tag.find('b')
	if country_name:
		black_list_countries.append(country_name.text.strip())
#Outputing the results:
if len(black_list_countries) == 0:
	print("There are no high risk jurisdictions.")
else:
	print("The high risk jurisdictions are:")
	for c in black_list_countries:
		print(c)

 #Now, I'll analyze the grey list:
increased_monitoring = "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/Increased-monitoring-october-2023.html"
grey_list_countries =[]
response = requests.get(increased_monitoring)
if response.status_code == 200:
	glist = BeautifulSoup(response.text,"html.parser")
else:
	print("Error connecting wiht the web page")
country_names = [element.text for element in glist.find_all('h3', class_='cmp-title__text')]
for i in country_names:
	grey_list_countries.append(i.lower())
# It's important to note that I still need to improve this last part of the code, as I should only look for countries above the line "Jurisdictions No Longer Subject to Increased Monitoring by the FATF"
if len(grey_list_countries) == 0:
	print("There are no high risk jurisdictions.")
else:
	print("Increased monitoring jurisdictions:")
	for c in grey_list_countries:
		print(c) 
