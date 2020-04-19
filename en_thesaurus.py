import json
from collections import namedtuple
# from nltk.stem import WordNetLemmatizer 
import spacy
from nltk.corpus import wordnet   #Import wordnet from the NLTK

# lemmatizer = WordNetLemmatizer()

nlp = spacy.load('en_core_web_lg', disable=['parser', 'ner'])

kata = namedtuple('kata',['word', 'key', 'pos', 'synonyms'])
katas = []

    
def load_dictionary(path) :
    # thesaurus = [json.loads(line) for line in open('D:/Dictionary/en_thesaurus.jsonl', 'r')]
    with open(path) as f :
        for line in f :
            l = json.loads(line) 
            katas.append(kata(l.get('word'), l.get('key'), l.get('pos'), l.get('synonyms')))
    

def find_synonyms(katakunci, kamus) :

    synonyms = []
    for katakata in kamus:
        if katakata.word == katakunci :
            for synonym in katakata.synonyms:
                synonyms.append(synonym)
    
    if len(synonyms) == 0 :
        print ('tidak ada di kamus, mencari di wordnet ...')
        for synset in wordnet.synsets(katakunci):
            for lemma in synset.lemmas():
                synonyms.append(lemma.name())

    return str(synonyms)

def check_similar(kata1, kata2, synonym1, synonym2) :

    if (kata1 in synonym2) or (kata2 in synonym1) :
        return True
    else :
        return False

def kata_dasar_spacy(katakunci) :
    doc = nlp(katakunci)
    return " ".join([token.lemma_ for token in doc])

def kata_dasar_wordnet(katakunci) :
    for synset in wordnet.synsets(katakunci):
        synset = wordnet.synsets(katakunci)
    return str(synset[0].lemmas()[0].name())

def input_check_similar() :

    print('Masukkan kata pertama : ', end = ' ')
    kata1 = str(input())
    # kata1 = kata_dasar_wordnet(kata1)
    kata1 = kata_dasar_spacy(kata1)
    print('Synonym dari ' + kata1 + ' adalah: ', end = '\n')
    synonym1 = find_synonyms(kata1, katas)
    print(synonym1)

    print('Masukkan kata kedua : ', end = '')
    kata2 = str(input())
    # kata2 = kata_dasar_wordnet(kata2)
    kata2 = kata_dasar_spacy(kata2)
    print('Synonym dari ' + kata2 + ' adalah: ', end = '\n')
    synonym2 = find_synonyms(kata2, katas)
    print(synonym2)

    if check_similar(kata1, kata2, synonym1, synonym2) :
        print (kata1 + ' dan ' + kata2 + ' adalah Synonym')
    else :
        print (kata1 + ' dan ' + kata2 + ' bukan Synonym')


path = 'D:/Dictionary/en_thesaurus.jsonl'
load_dictionary(path)

cek = True

while cek :
    input_check_similar()
    print('Cek lagi (Y/N) ? ', end = ' ')
    if str(input()).upper() == 'N' :
        cek = False
        break
    else :
        continue
        



