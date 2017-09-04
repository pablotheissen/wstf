# -*- coding: utf-8 -*-

import pyphen
import re
from collections import Counter, defaultdict

demotext = "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."

def count_sentences_german(text):
	""" Count number of sentences by counting end-dots but avoid counting
	abbrevations like »u.a.« """
	text = re.sub("[^a-zA-ZäöüÄÖÜß\.!? ]", " ", text)
	return len(re.findall(
		"[a-zäöüß)]{3}[\.?!][\n\s]", text)) + 1


def count_syllables_german(text):
	""" Count number of syllables:
		1. Clean up text
		2. Split text into seperate words seperated by a space
		3. Hyphenate every single word with pyphen
		4. Count number of words + number of hyphens
	"""
	dic = pyphen.Pyphen(lang='de_DE')

	# Optionally filter out some stuff from the text
	# text = re.sub("[-–\.,:;'()„“»«›‹/•0-9]", " ", text)
	text = re.sub("[^a-zA-ZäöüÄÖÜß ]", " ", text) # special chars/numbers
	# text = re.sub("\s[A-ZÄÖÜ]+\s", " ", text) # One-character words
	# text = re.sub("\s[a-zäöüß]\s", " ", text) # One-character words
	text = re.sub("\s+", " ", text)
  
	# print(text)

	number_of_syllables = 0
	syllables_per_word = defaultdict(int)
	characters_per_word = defaultdict(int)
	for word in text.split(" "):
		# print(word)
		syllable_counter = 0
		# hyphenate word
		syllables = dic.inserted(word)
		# count first syllable of word
		syllable_counter += 1
		# and count the other syllables
		syllable_counter += syllables.count("-")
		number_of_syllables += syllable_counter
		syllables_per_word[syllable_counter] += 1
		characters_per_word[len(word)] += 1
		# print("  Chars: " + str(len(word)))
		# print("  Syllables: " + str(syllable_counter))

	return number_of_syllables, syllables_per_word, characters_per_word


def wiener_sachtext_formel(ms, sl, iw, es):
	"""https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel

	Keyword arguments:
	MS -- Prozentanteil der Wörter mit drei oder mehr Silben,
	SL -- mittlere Satzlänge (Anzahl Wörter),
	IW -- Prozentanteil der Wörter mit mehr als sechs Buchstaben,
	ES -- Prozentanteil der einsilbigen Wörter.
	"""
	print("\nWIENER SACHTEXT FORMEL")
	print("   MS: {:.3}".format(ms))
	print("   SL: {:.3}".format(sl))
	print("   IW: {:.3}".format(iw))
	print("   ES: {:.3}".format(es))
	wsf = 0.1935 * ms + 0.1672 * sl + 0.1297 * iw - 0.0327 * es - 0.875
	return wsf

if __name__ == "__main__":
	demotext = re.sub("\s+", " ", demotext)
	number_of_words = demotext.count(" ") + 1
	demotext = re.sub("\.+", ".", demotext)
	number_of_sentences = count_sentences_german(demotext)
	number_of_syllables, syllables_per_word, characters_per_word = count_syllables_german(
		demotext)
	avg_sentence_length = number_of_words / number_of_sentences
	avg_number_of_syllables_per_word = number_of_syllables / number_of_words

	# Initialize Wiener Sachtext Formel
	# print(syllables_per_word.items())
	# count number of words with number of syllables >= 3
	# key of syllables_per_word is number of syllables, value is number of
	#   words with this syllable-number
	number_of_words_with_three_or_more_syllables = sum(
		[v for k, v in syllables_per_word.items() if k >= 3])
	print(characters_per_word.items())
	number_of_words_with_six_or_more_characters = sum(
		[v for k, v in characters_per_word.items() if k >= 6])
	wsf = wiener_sachtext_formel(
		number_of_words_with_three_or_more_syllables / number_of_words * 100,
		avg_sentence_length,
		number_of_words_with_six_or_more_characters / number_of_words * 100,
		syllables_per_word[1] / number_of_words * 100)
	print("{:.3}".format(wsf))
