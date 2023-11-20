import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "I stayed at Hotel Maldives and enjoyed the food at Restaurant Cuba. Maldives is a beautiful country."
#si pongo Hotel Cuba, lo reconoce como pais :(


# Process the text with spaCy
doc = nlp(text)

# Filter out locations that are part of a larger entity (e.g., Hotel Cuba, Restaurant Cuba)
filtered_locations = set()

for ent in doc.ents:
    if ent.label_ == "GPE":  # GPE stands for geopolitical entity (countries, cities, states)
        print(ent.text)
        filtered_locations.add(ent.text)

# Remove filtered locations from the set of all locations
all_locations = {ent.text for ent in doc.ents if ent.label_ == "GPE"}
filtered_locations = {loc.lower() for loc in filtered_locations}
final_locations = all_locations - filtered_locations

# Print the final set of locations
print("Final locations:")
for loc in final_locations:
    print(loc)