import spacy
import time

start = time.time()

nlp = spacy.load('en_core_web_lg', disable=['parser', 'ner'])
doc = nlp('displaying')
print (" ".join([token.lemma_ for token in doc]))

print (time.time() - start)


