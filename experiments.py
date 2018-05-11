from naivew2wsmt import naivew2wsmt
from naivew2wsmt import naivew2wsmtwithmarkovlanguagemodel
from naivew2wsmt import data_load
import sys
import pickle
sys.modules['naivew2wsmt'] = naivew2wsmt
sys.modules['naivew2wsmtwithmarkovlanguagemodel'] = naivew2wsmtwithmarkovlanguagemodel

import ensemble_translator

with open("naivew2wsmt/models/smt","rb") as file:
     smt = pickle.load(file)
with open("naivew2wsmt/models/smtwindowed","rb") as file:
     smtwindowed = pickle.load(file)
with open("naivew2wsmt/models/markovsmt","rb") as file:
     markovsmt = pickle.load(file)
with open("naivew2wsmt/models/smtwindowed","rb") as file:
     markovsmtwindowed = pickle.load(file)

translators = [smt, smtwindowed, markovsmt, markovsmtwindowed]

ensemble = ensemble_translator.EnsembleTranslator(translators)

data_id_test = data_load.loadData("naivew2wsmt/data/data_id_test.txt")
data_en_test = data_load.loadData("naivew2wsmt/data/data_en_test.txt")

def untokenizedCorpusBLEU(ref,hyp):
	ref = [nltk.word_tokenize(x) for x in ref]
	hyp = [nltk.word_tokenize(x) for x in hyp]

	return bleu_score.corpus_bleu(ref,hyp)

hyp_en = ensemble.translateSentences(data_id_test)

print("BLEU:")
print(untokenizedCorpusBLEU(data_en_test,hyp_en))