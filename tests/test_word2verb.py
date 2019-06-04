#!/usr/bin/env python3
# coding:utf8


import unittest
from maplepecans.word2verb import HomonymWord


class TestHomonymWord(unittest.TestCase):

	def setUp(self) -> None:
		self.obj = HomonymWord()
