###  Assignment No 3 ###

#Assignment Title : Name Entity Recognition in python with spacy


import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)
    
    # Extract named entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

if __name__ == "__main__":
    # Example text
    text = "APJ Abdul Kalam was born in Rameswaram, India. He served as the 11th President of India from 2002 to 2007."


    # Perform Named Entity Recognition
    named_entities = perform_ner(text)

    # Print the results
    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} - {label}")


'''
**************    OUTPUT

Named Entities:
Earth - LOC
third - ORDINAL
Sun - ORG

'''
