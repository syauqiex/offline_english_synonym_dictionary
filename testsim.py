from nltk.corpus import wordnet

dog = wordnet.synset('dog.n.01')
print(dog.lemma_names())

syns = wordnet.synsets("dog")
print(syns)

synonyms = []
antonyms = []

for syn in wordnet.synsets("login"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))