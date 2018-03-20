print("========== problem 5a ==============")
import random
current_word1 = '<s>'
current_word2 = ''
text = " "

for i in range(1, 50):
	k = random.random()
	if (k < list(prob[current_word1].values())[0]):
		current_word2 = list(prob[current_word1].keys())[0]
	else:
		current_word2 = list(prob[current_word1].keys())[1]
	text = text + " " + current_word1
	current_word1 = current_word2

print(text)

###########
# Problem 5b:

print("========== problem 5b ==============")
import nltk

count = { }

corpus = open('corpus.txt', 'r').read()

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

current_word1 = 'START'
current_word2 = ''
text = " "

for i in range(1, 50):
	k = random.random()
	j = 0
	for i in range(0, len(list(proba[current_word1].values()))):
		j += list(proba[current_word1].values())[i]
		if (k < j):
			current_word2 = list(proba[current_word1].keys())[i]
			break

	text = text + " " + current_word1
	current_word1 = current_word2

print(text)