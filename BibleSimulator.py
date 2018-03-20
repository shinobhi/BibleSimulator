import nltk
import random

count = { }

corpus = open('corpus-genesis.txt', 'r').read()

words = corpus.split()

for word1, word2 in nltk.bigrams(words):
    if word1 not in count:
        count[word1] = { }

    if word2 not in count[word1]:
        count[word1][word2] = 1
    else:
        count[word1][word2] += 1

proba = count
proba2 = { }

for word1 in proba:
	for word2 in proba[word1]:
		if word1 not in proba2:
			proba2[word1] = proba[word1][word2]
		else:
			proba2[word1] += proba[word1][word2]
	for word2 in proba[word1]:
		proba[word1][word2] = proba[word1][word2]/proba2[word1]

# print(proba)
# prints my dictionary

current_word1 = '<verse>'
current_word2 = ''
text = " "

while(True):
	if current_word1 == '</verse>':
		break;
	k = random.random()
	j = 0
	for i in range(0, len(list(proba[current_word1].values()))):
		j += list(proba[current_word1].values())[i]
		if (k < j):
			current_word2 = list(proba[current_word1].keys())[i]
			break

	if (current_word1 != "<verse>"):
		text = text + " " + current_word1
	current_word1 = current_word2

print(text)