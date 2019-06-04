#!/usr/bin/env python3
# coding:utf8


import csv
import random
from janome.tokenizer import Tokenizer


tokenizer = Tokenizer()


class HomonymWord:

	def __init__(self):
		# super().__init__(self)

		self.postpositionals = ['が', 'を', 'に']

		with open('../mecab-ipadic/Verb.csv', 'r') as f:
			reader = csv.reader(f)

			self.verbs = {r[11]: r[0] for r in reader if r[9] == '基本形'}

	def word2verb(self, word):

		# change word to all katakana sentence
		tokens = tokenizer.tokenize(word)
		text = ''.join([token.reading for token in tokens])

		del tokens

		verb_list = [value for key, value in self.verbs.items() if key.find(text) >= 0]

		output_sen = word + self.postpositionals[0] + random.choice(verb_list) if len(verb_list) > 0 else 'no text'

		return output_sen


if __name__ == '__main__':
	h = HomonymWord()
	print(h.word2verb('電気'))
