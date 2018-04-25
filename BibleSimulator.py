# inspired and adapted from https://github.com/rdcolema/trigram-random-sentence-generator/blob/master/trigram_sentence_gen.py

import nltk
import random
from collections import defaultdict

def gen_trigrams(path):
	corpus = open('corpora/' + path, 'r').read()
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
		c = random.randint(1, 100)
		v = random.randint(1, 100)
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

def gen_verse_seed(seed, trigrams):
	w = seed
	w0 = '<verse>'

	if (w0, w) not in trigrams:
		return "<empty verse>"

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

def gen_book(trigrams):
	text = ""

	for i in range(1, 101):
		for j in range(1, 101):
			v = str(i) + ":" + str(j)
			verse = gen_verse_seed(v, trigrams)
			if verse != "<empty verse>":
				text += verse
				text += "\n\n"

	return text

if __name__ == "__main__":
	help_str = "Commands:\n - 'file' allows you to change the file you are working with.\n   - 'which-file' prints the name of the training file currently being dealt with. \n - 'book' generates a book in fake-books.\n - 'verse' generates a single verse.\n - 'quit' exits out of the program.\n - 'help' gives a list of the commands."

	print("Welcome to the Bible Simulator!")
	inp = input("Please enter the name of the desired file to process: ")
	trig = gen_trigrams(inp)
	ended = False
	print(help_str)
	while (ended == False):
		inp2 = input(">>> ")
		if (inp2 == "book"):
			with open('fake-books/' + inp, 'w') as b:
				b.write(gen_book(trig))
			print("Book written to fake-books/" + inp + ".")
		elif (inp2 == "verse"):
			print(gen_verse(trig))
		elif (inp2 == "quit"):
			print("Exiting. May the LORD guide you.")
			ended = True
		elif (inp2 == "help"):
			print(help_str)
		elif (inp2 == "file"):
			inp = input("Please enter the name of the desired file to process: ")
			trig = gen_trigrams(inp)
		elif (inp2 == "which-file"):
			print(inp)
		else:
			print("Command '" + inp2 + "' unrecognized.")