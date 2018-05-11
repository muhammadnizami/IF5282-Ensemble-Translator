from naivew2wsmt import naivew2wsmt
from naivew2wsmt import naivew2wsmtwithmarkovlanguagemodel
import sys
import pickle
sys.modules['naivew2wsmt'] = naivew2wsmt
sys.modules['naivew2wsmtwithmarkovlanguagemodel'] = naivew2wsmtwithmarkovlanguagemodel

import ensemble_translator

if "--show-candidates" in sys.argv:
	showCandidates = True
else:
	showCandidates = False

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

while(True):
	s = input("Bahasa: ")
	s, candidates = ensemble.translate(s)
	print("English:" + s)
	if (showCandidates):
		print("translators: " + str(translators))
		for candidate in candidates:
			print("candidate:" + candidate)