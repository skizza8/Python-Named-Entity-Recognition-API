
# importing necessary libraries
import spacy
from spacy import displacy
import json

# creating an object and loading the pre-trained model for "English"
nlp = spacy.load("en_core_web_sm")

class NER_Model:

    def get_ner(self, sentence):
        print(sentence)
        doc = nlp(sentence)
        print(doc)
        print(doc.ents)
        
        sentences, entity = [], []
        
        for ent in doc.ents:
            sentences.append(ent.text)
        
        for ent in doc.ents:
            entity.append(ent.label_)
        
            
        sentence_entity = [{"sentence": s, "entity": et} for s, et in zip(sentences, entity)]

        return json.dumps(sentence_entity)

