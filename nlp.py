"Implementation of NLP techniques"
import re
import spacy
import fitz

nlp = spacy.load("en_core_web_sm")

""" def	find_high_risk_countries(text, high_risk_countries):
	matches = []
	for country in high_risk_countries:
		pattern = re.compile(r'\b{}\b'.format(re.escape(country.lower())))
		if re.search(pattern, text):
			matches.append(country)
	return matches """

def remove_non_printable(doc): #ver como usar esto, pero voy a tener que usarlo
    filtered_tokens = [token.text for token in doc if re.match(r'^[ -~]+$', token.text)]
    return spacy.tokens.Doc(doc.vocab, words=filtered_tokens)

def context_aware_country_search(text, high_risk_countries):
    doc = nlp(text)
    matches = []

    for ent in doc.ents:
        if ent.text.lower() in high_risk_countries:
            print(ent.text, ent.label_)
            matches.append(ent.text.lower())

    return matches

def is_part_of_larger_entity(entity, root, dep):
    print(entity)
    print(root)
    return dep not in ("punct", "conj") and entity != root

def context_aware_country_search_prueba2(text, high_risk_countries): #añadir q la tag sea GPE
    doc = nlp(text)
    matches = []

    for ent in doc.ents:
        if ent.text.lower() in high_risk_countries:
            print(ent.text, ent.label_)
            print(ent.root.dep_)
            if is_part_of_larger_entity(ent.text, ent.root, ent.root.dep_):
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
    
    text = "I stayed at Avenue of Belgium and enjoyed the food at Restaurant Spain. Maldives is a beautiful country."
    preprocessed_text = text.lower()

    # Perform country search
    matches = context_aware_country_search_prueba2(preprocessed_text, high_risk_countries)

    # Output the matches
    if matches:
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