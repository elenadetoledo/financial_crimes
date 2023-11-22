""" Code by Elena de Toledo Hernández
Implementation of NLP techniques for the detection of high-risk countries via entitiy analysis"""
import spacy
import fitz

#I load the model for nlp in english
nlp = spacy.load("en_core_web_sm")

#Function for checking if a word is part of a larger entity or if it's an entity on its own
def is_not_part_of_larger_entity(entity, root, dep):
    return not(dep not in ("punct", "conj") and entity != root)

#Function for looking for countries in the right context
def context_aware_country_search(text, high_risk_countries):
    doc = nlp(text)
    matches = []

    for ent in doc.ents:
        if ent.text.lower() in high_risk_countries:
            print(ent.text, ent.label_)
            matches.append(ent.text.lower())

    return matches

#Function to print a summary of the findings of the function
def printing_summary(matches):
    result_dict = {}
    
    for element in matches:
        if element in result_dict:
            result_dict[element] += 1
        else:
            result_dict[element] = 1
    for element, count in result_dict.items():
        print(f"{element}: {count} times")

#Function for opening the PDF file and iterating through the entities in the document to check for matches
def read_pdf_and_search(file_path, high_risk_countries):
    with fitz.open(file_path) as pdf_document:
        text = ""
        # Iterate through pages and extract text
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
    #Text preprocessin: writing everything in vowels to unify the format in the whole document
    preprocessed_text = text.lower()
    matches = []
    #Create a document
    doc = nlp(text)
    #Iterate the entities in the document
    for ent in doc.ents:
        if ent.text.lower() in high_risk_countries:
            #Checking whether the entity is part of a larger entity or not
            if is_not_part_of_larger_entity(ent.text, ent.root.text, ent.root.dep_):
                matches.append(ent.text.lower())
    # Output the matches
    if matches:
        print("Some high-risk countries have been detected:")
        printing_summary(matches)
    else:
        print("No high-risk countries have been found.")


# Example usage
pdf = "integrated-management-report-2022.pdf"
high_risk_countries = ["cuba","spain","belgium","britain","prague","italy"] #I'm aware this doesn't reflect reality, but these were countries that I found in the document

read_pdf_and_search(pdf, high_risk_countries)