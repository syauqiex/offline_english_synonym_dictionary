import json
from collections import namedtuple

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
    return synonyms

def check_similar(kata1, kata2, kamus) :

    synonym1 = find_synonyms(kata1, kamus)
    synonym2 = find_synonyms(kata2, kamus)
    if (kata1 in synonym2) or (kata2 in synonym1) :
        return True
    else :
        return False

def input_check_similar() :

    print('Masukkan kata pertama : ', end = ' ')
    kata1 = str(input())
    print(find_synonyms(kata1, katas))
    print('Masukkan kata kedua : ', end = ' ')
    kata2 = str(input())
    print(find_synonyms(kata2, katas))

    if check_similar(kata1,kata2, katas) :
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
        



