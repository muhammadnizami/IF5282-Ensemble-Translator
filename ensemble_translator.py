from englishgrammarscoring import grammar_scoring
import sys
sys.modules['grammar_scoring'] = grammar_scoring #important for unpickling the pretrained model

class EnsembleTranslator:
	def __init__(self,translators=[],scorer=grammar_scoring.loadModel("englishgrammarscoring/pretrained_model")):
		self.translators=translators;
		self.scorer=scorer;

	def translate(self,sentence):
		candidateTranslations = [translator.translateSentence(sentence) for translator in self.translators]
		scores = self.scorer.predict(candidateTranslations)
		i = scores.index(max(scores))
		return candidateTranslations[i], candidateTranslations

	def translateSentences(self, sentences):
		return [self.translate(sentence) for sentence in sentences]