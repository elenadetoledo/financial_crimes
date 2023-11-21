"Implementation of NLP techniques for the detection of high-risk activities or countries clasified as high risk by the TAFT"
import spacy
import fitz

nlp = spacy.load("en_core_web_sm")

def is_not_part_of_larger_entity(entity, root, dep):
    return not(dep not in ("punct", "conj") and entity != root)

def context_aware_country_search(text, high_risk_countries):
    doc = nlp(text)
    matches = []

    for ent in doc.ents:
        if ent.text.lower() in high_risk_countries:
            print(ent.text, ent.label_)
            matches.append(ent.text.lower())

    return matches

def read_pdf_and_search(file_path, high_risk_countries):
    # Open the PDF file
	texto="I stayed at Hotel Britain and enjoyed the food at Restaurant of Prague in Southern Italy. I love Maldives"
	with fitz.open(file_path) as pdf_document:
    	text = ""
    	# Iterate through pages and extract text
        for page_num in range(pdf_document.page_count):
        	page = pdf_document[page_num]
            text += page.get_text()
    preprocessed_text = texto.lower()
    matches = []
    doc = nlp(texto)
    for ent in doc.ents:
        print(ent)
    for ent in doc.ents:
    	print(f"Entity: {ent.text}, Root: {ent.root.text}, Dependency: {ent.root.dep_}")
		if ent.text.lower() in lista:
			if is_not_part_of_larger_entity(ent.text, ent.root.text , ent.root.dep_):
				matches.append(ent.text.lower())
	print(matches)

    # Output the matches
i	if matches:
        print("¡Alerta! Países de alto riesgo encontrados:", matches)
    else:
        print("No se encontraron países de alto riesgo.")

# Example usage
#pdf_file_path = "C:\\Desktop\\integrated-managemet-report-2022.pdf" Esto lo quiero cambiar!!!
pdf = "integrated-management-report-2022.pdf"
#pdf = "pruebas_SCIB.pdf"
high_risk_countries = ["cuba","spain","toronto", "belgium", "maldives"] #tengo que controlar las distintas formas en las que se escriben ciertos paises!! EEUU y en varios idiomas

read_pdf_and_search(pdf, high_risk_countries)
print("Fin del programa")