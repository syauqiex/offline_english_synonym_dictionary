from PyDictionary import PyDictionary
import bs4

fitur = ["hotel","motel","house"]
kamus_fitur = PyDictionary(fitur)
for kata1 in kamus_fitur:
    for kata2 in kamus_fitur:
        if kata1 == kata2 :
            continue
        sinonim1 = kamus_fitur.getSynonyms(kata1)
        print(sinonim1)
        sinonim2 = kamus_fitur.getSynonyms(kata2)
        print(sinonim2)
        if set(sinonim1).issubset(set(sinonim2)) or set(sinonim2).issubset(set(sinonim1)) :
            print("kata: " + kata1 + " dan " + kata2 + " adalah synonym")
        else :
            print("kata: " + kata1 + " dan " + kata2 + " BUKAN synonym")

# for i in range(0,len(kamus_fitur)):
#     for j in range(i+1,len(kamus_fitur)):
#         sinonim1 = kamus_fitur.getSynonyms(kamus_fitur[i])
#         print(sinonim1)
#         sinonim2 = kamus_fitur.getSynonyms(kamus_fitur[j])
#         print(sinonim2)
#         if set(sinonim1).issubset(set(sinonim2)) or set(sinonim2).issubset(set(sinonim1)) :
#             print("kata: " + kamus_fitur[i] + " dan " + kamus_fitur[j] + " adalah synonym")
#         else :
#             print("kata: " + kamus_fitur[i] + " dan " + kamus_fitur[j] + " BUKAN synonym")

# dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")
# print(dictionary.printMeanings()) 
# print(dictionary.getMeanings()) 
# print (dictionary.getSynonyms())
# print (dictionary.translateTo("hi")) 