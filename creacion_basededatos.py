import requests
from bs4 import BeautifulSoup
# Cosas a entender: hay una black list --> high-risk jurisdictions subject to call for action
# Luego hay una grey list --> jurisdictions under increased monitoring

high_risk = "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/Call-for-action-october-2023.html"
black_list_countries = []
response = requests.get(high_risk)
if response.status_code == 200:
	blist = BeautifulSoup(response.text,"html.parser")
else:
	print("Error connecting wiht the web page") #convertir en exeption
h3_tags = blist.find_all('h3')

for h3_tag in h3_tags:
	country_name = h3_tag.find('b')
	if country_name:
		print(country_name.text.strip())
		#black_list_countries.append()

increased_monitoring = "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/Increased-monitoring-october-2023.html"
grey_list_countries =[]
response = requests.get(increased_monitoring)
if response.status_code == 200:
	glist = BeautifulSoup(response.text,"html.parser")
else:
	print("Error connecting wiht the web page") #convertir en exeption
specific_div = glist.find('div', {'id': 'title-8b3c1aab42', 'class': 'cmp-title'})
#print(specific_div)
if specific_div:
	preceding_sections = specific_div.find_previous('div',class_ = 'section')
	preceding_section = preceding_sections[0] if preceding_sections else None 
	if preceding_section == None:
		print("h")
""" preceding_section = specific_div.find_previous('div',class_='section')
h3_tags = preceding_section.find_all('h3')
print("llego1")
for h3_tag in h3_tags:
	country_name = h3_tag.text.strip()
	if country_name:
		print(country_name)
else:
print("Specific div element not found") """