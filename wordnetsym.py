from nltk.corpus import wordnet   #Import wordnet from the NLTK

syn = list()
ant = list()
for synset in wordnet.synsets("Displaying"):
   for lemma in synset.lemmas():
      syn.append(lemma.name())    #add the synonyms
print('Synonyms: ' + str(syn))

print (len(ant))

# synset = wordnet.synsets("Displaying")

# for syn in synset :
#     print ('Word and Type : ' , syn.name())
#     print ('Synonym is : ' , syn.lemmas())
#     print ('The meaning of the word : ' , syn.definition())
#     print ('Example : ' , syn.examples())

# print('Word and Type : ' + synset[0].name())
# print('Synonym is : ' + synset[0].lemmas()[0].name())
# print('The meaning of the word : ' + synset[0].definition())
# print('Example : ' + str(synset[0].examples()))