import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import jsonlines
  
ex = 'The 2019 Hurricane Katrina has hit the shores of Mumbai on 28/09/2019 recording a mass destruction of 25 building collapsed and a death toll of 800 people. Red Cross is summoning volunteers and a relief fund of $1.5 Billion is expected. '
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent
sent = preprocess(ex)
#print(sent)
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
#print(cs)

from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
nltk.download('maxent_ne_chunker')
nltk.download('words')
iob_tagged = tree2conlltags(cs)
# pprint(iob_tagged)
ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(ex)))
# print(ne_tree)

import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

#import en_core_web_sm
#nlp= spacy.load('en_core_web_sm')
#nlp = en_core_web_sm.load()
doc = nlp("The 2019 Hurricane Katrina has hit the shores of Mumbai on 28/09/2019 recording a mass destruction of 25 building collapsed and a death toll of 800 people. Red Cross is summoning volunteers and a relief fund of $1.5 Billion is expected.")
# pprint(doc)
dis=[(str(X.label_),str(X.text)) for X in doc.ents]
pprint(dis)
disaster=dict(dis)
disaster["location"] = disaster.pop("GPE")
disaster["req_money"] = disaster.pop("MONEY")
disaster["event"] = disaster.pop("EVENT")
disaster["req_food"] = 1500
disaster["req_cloth"] = 1500
disaster["req_med"] = 1500
disaster["death_toll"] = 0
del disaster["CARDINAL"]
del disaster["ORG"]
del disaster["DATE"]
# disaster["location"] = disaster.pop(old_key)
 
print(disaster)
with jsonlines.open('static/disaster.jsonl', mode='a') as writer:
  writer.write(disaster)
#pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])