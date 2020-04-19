import json
import os

class Kamus(object):

    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        # self.db = json.load(open(self.location , "r"))
        self.db = [json.loads(line) for line in open(self.location, 'r')]

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))  
            return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True


kamusku =  Kamus('D:/Dictionary/en_thesaurus.jsonl')

print (kamusku.db)

# import json
# from collections import namedtuple

# class Dictionary(object):

#     __slots__ = ['key', 'word', 'pos', 'synonym']

#     def __init__(self, key, word, pos, synonym):
#         self.key = key
#         self.word = word
#         self.pos = pos
#         self.synonym = synonym

    # def addWord(self, Word):
    #     self.key = Word.key
    #     self.word = Word.word
    #     self.pos = Word.pos
    #     self.synonym = Word.synonym

    # def searchKey(self,keySearch):
    #     for Word in self.words:
    #         if Word.key == keySearch:
    #             return Word

    # def searchWordSynonym(self,wordSearch):
    #     synonymFound = []
    #     for Word in self.words:
    #         if Word.word == wordSearch:
    #             synonymFound.append(Word.synonym)
    #     return synonymFound

# kamus = Dictionary()

# Data = namedtuple('Data', 'key word pos synonym')

# thesaurus = [json.loads(line) for line in open('D:/Dictionary/en_thesaurus.jsonl', 'r')]

# for item in thesaurus:
#     Data = item
#     kamus.addWord(Data)

# print (kamus.words[10000:10010])

# print (kamus.searchWordSynonym('smart'))

# arraykata = [Data(**k) for k in thesaurus["arraykata"]]

# for item in thesaurus[:10]:
#     for key,val in item.items():
#         print ("{} {}".format(key, val))



# print (help(Data))
# print (help(Datas))

# for data in thesaurus:
#     print(data)
#     kamus.addWord(Data(data))

# print(kamus.searchKey('password_1'))
# print(kamus.searchWordSynonym('password'))




     


