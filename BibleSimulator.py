import nltk
import random
from collections import defaultdict

def gen_trigrams():
	corpus = open('corpora/genesis.txt', 'r').read()
	words = corpus.split()
	trigrams = { }

	for word1, word2, word3 in nltk.trigrams(words):
		if (word1, word2) not in trigrams:
			trigrams[(word1, word2)] = { }

		if word3 not in trigrams[(word1, word2)]:
			trigrams[(word1, word2)][word3] = 1
		else:
			trigrams[(word1, word2)][word3] += 1

	for key in trigrams:
		total = 0
		for word in trigrams[key]:
			total += trigrams[key][word]
		for word in trigrams[key]:
			trigrams[key][word] = trigrams[key][word] / total

	return trigrams

def gen_verse(trigrams):

	w = '-1:-1'
	w0 = '<verse>'

	while (w0, w) not in trigrams:
		c = random.randint(1, 150)
		v = random.randint(1, 150)
		w = str(c) + ":" + str(v)

	ret = [w]
	
	text = ""
	while (True):
		if w == '</verse>':
			break;
		k = random.random()
		j = 0
		for i in range(0, len(list(trigrams[(w0, w)].values()))):
			j += list(trigrams[(w0, w)].values())[i]
			if (k < j):
				w1 = list(trigrams[(w0, w)].keys())[i]
				break

		if (w != "<verse>"):
			text = text + " " + w
		w0, w = w, w1

	return text

if __name__ == "__main__":
	trig = gen_trigrams()
	print(gen_verse(trig))