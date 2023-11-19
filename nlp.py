"Implementation of NLP techniques"
import re
import spacy
import fitz

nlp = spacy.load("en_core_web_sm")

""" # Text preprocessing
def preprocess_text(text):
	text = text.lower()
	text = re.sub(r'[^\w\s]','',text) #Igual no quiero quitar .?
	return text """



def	find_high_risk_countries(text, high_risk_countries):
	matches = []
	for country in high_risk_countries:
		pattern = re.compile(r'\b{}\b'.format(re.escape(country.lower())))
		if re.search(pattern, text):
			matches.append(country)
	return matches

def context_aware_country_search(text, high_risk_countries):
    doc = nlp(text)
    matches = []

    for ent in doc.ents:
        if ent.text.lower() in high_risk_countries:
            matches.append(ent.text.lower())

    return matches

def read_pdf_and_search(file_path, high_risk_countries):
    # Open the PDF file
    with fitz.open(file_path) as pdf_document:
        text = ""

        # Iterate through pages and extract text
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
            #print(text)
    preprocessed_text = text.lower()

    # Perform country search
    matches = context_aware_country_search(preprocessed_text, high_risk_countries)

    # Output the matches
    if matches:
        print("¡Alerta! Países de alto riesgo encontrados:", matches)
    else:
        print("No se encontraron países de alto riesgo.")

# Example usage
#pdf_file_path = "C:\\Desktop\\integrated-managemet-report-2022.pdf" Esto lo quiero cambiar!!!
pdf = "integrated-management-report-2022.pdf"
high_risk_countries = ["february","españa","spain"] #tengo que controlar las distintas formas en las que se escriben ciertos paises!! EEUU y en varios idiomas

read_pdf_and_search(pdf, high_risk_countries)
