import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
  
ex = 'The hurricane Laila has hit the shores of Los Angeles,North America at 12:30pm on 28/09/2019 recording a mass destruction of 25 buildings collapsed and a death toll of 800 people. Red Cross is summoning volunteers and a relief fund of $1.5 Billion is expected. '
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
pprint(iob_tagged)
ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)

import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

#import en_core_web_sm
#nlp= spacy.load('en_core_web_sm')
#nlp = en_core_web_sm.load()
doc = nlp(u"The Olympics has hit the shores of Mumbai at 12:30pm on 28/09/2019 recording a mass destruction of 25  Gateway of India building collapsed and a death toll of 800 people. Red Cross is summoning volunteers and a relief fund of $1.5 Billion is expected. ")
# pprint(doc)
pprint([(X.text, X.label_) for X in doc.ents])
#pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])