""" import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "I stayed at Hotel Cuba and enjoyed the food at Restaurant España. Maldives is a beautiful country."
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
    print(loc) """

import spacy

# Check if an entity is part of a larger entity
def is_not_part_of_larger_entity(entity, root, dep):
    return not(dep not in ("punct", "conj") and entity != root)

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "I stayed at Hotel Britain and enjoyed the food at Restaurant of Prague in Southern Italy. My beautiful house in the North of Spain is a beautiful country."
matches = []
# Process the text with spaCy
doc = nlp(text)
lista = ["belgium","spain","maldives","croatia", "prague", "cuba","france"]

for ent in doc.ents:
    print(ent)
for ent in doc.ents:
    print(f"Entity: {ent.text}, Root: {ent.root.text}, Dependency: {ent.root.dep_}")
    if ent.text.lower() in lista:
        if is_not_part_of_larger_entity(ent.text, ent.root.text , ent.root.dep_):
            matches.append(ent.text.lower())
print(matches)
        
""" # Extract named entities and their syntactic dependencies
entity_relations = [(ent.text, ent.root.text, ent.root.dep_) for ent in doc.ents]

# Print the named entities and their syntactic dependencies
for entity, root, dep in entity_relations:
    print(f"Entity: {entity}, Root: {root}, Dependency: {dep}") """


""" 
# Identify entities that are part of a larger entity
for entity, root, dep in entity_relations:
    if is_part_of_larger_entity(entity, root, dep):
        print(f"{entity} is part of a larger entity.") """