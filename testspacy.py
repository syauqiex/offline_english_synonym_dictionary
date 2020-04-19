import spacy
import time

start = time.time()

with open('d:/dictionary/e-store.txt') as f:
    input = f.read()

word = 0
result = []

nlp = spacy.load("en_core_web_sm", disable = 'ner')
doc = nlp(input)

for token in doc:
    if token.pos_ == "NOUN":
        result.append(token.text)
    word += 1

elapsed = time.time() - start

print("From", word, "words, there is", len(result), "NOUN found in", elapsed, "seconds")

# for line in example:
#     sent = nlp(line)
#     token_result = []
#     for token in sent:
#         token_result.append(token)
#     result.append(token_result)

# print(result)
