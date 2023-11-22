""" Code by Elena de Toledo Hernández
Implementation of NLP techniques for the detection of high-risk activities by analyzing the words lemmas"""
import spacy
import fitz

#I load the model for nlp in english
nlp = spacy.load("en_core_web_sm")

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
def read_pdf_and_search(file_path, high_risk_activities):
    with fitz.open(file_path) as pdf_document:
        text = ""
        # Iterate through pages and extract text
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
    #Text preprocessin: writing everything in vowels to unify the format in the whole document
    preprocessed_text = text.lower()
    matches = []
    lemmatized_text = " ".join([token.lemma_ for token in nlp(" ".join(high_risk_activities))])
    # Tokenize the lemmatized text to get a list of lemmatized elements
    lemmatized_list = [token.text for token in nlp(lemmatized_text)]
    high_risk_activities_lemmas = []
    #Create a document
    doc = nlp(text)
    #Iterate the entities in the document
    for token in doc:
        if token.lemma in lemmatized_list:
            matches.append(token.text)
    # Output the matches
    if matches:
        print("Some high-risk activities have been found:")
        printing_summary(matches)
    else:
        print("No high-risk activities have been found.")


# Example usage
pdf = "integrated-management-report-2022.pdf"
#I have written some of the activities in which it makes sense this search by lemma. For other activities, such as "real state", this doesn't make sense
high_risk_activities = ["arms","casino","gambling","forestry","fishing","mineral","gas","oil",
				 "petroleum","carbon","nuclear","pharmaceutical", "tourism"]

read_pdf_and_search(pdf, high_risk_activities)