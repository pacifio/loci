#! /usr/local/bin/python3

"""
Welcome to LOCI - Lines Of Codes Indicator

This is a simple program that finds total lines of codes you've written

Update ~/.loc.json file to update ignored files to accuretly count how many lines
of codes you've written .

The ./example folder is there to test . It contains nothing of the logix
"""

"""
TODO

1 > A nicely formatted box layout to show results
2 > Highest coded file (max int in an array)
3 > Lowest coded file (min int in an array)
4 > Total lines of code
5 > Status of which dir (just show os.currdir nicely)
6 > Create loci.json if not exists from PRE_JSON
"""

import os
import json
from data import PRE_JSON

class Loci:
	def __init__(self):
		self.json = {}
		self.lang = {}
		self.input = ''
		self.load_json()

	def load_json(self):
		self.json = json.loads(PRE_JSON)

	def loop_over_json(self):
		for k, v in self.json.items():
			if self.input in v['ids']:
				self.lang = self.json[k]

	def exec(self):
		extension_files = []

		print()

		for root, dirs, files in os.walk('./'):
			for name in files:
				formatted = os.path.join(root, name)
				if(formatted).endswith(self.lang['extension']):
					extension_files.append(formatted)

		data = {}
		for file in extension_files:
			read = open(file, 'r')
			lines = len(read.readlines())
			read.close()

			data[file] = lines

		if len(data.items()) == 0:
			print("No file found under extension %s" % (self.lang['extension']))
		else :
			print ("{:<30} {:<15}".format('Filename','Linecount'))

		for (k, v) in data.items():
			print("{:<30} {:<15}".format(k, v))

		print()

	def show_json(self):
		print(self.json)

	def run(self):
		extension = input('file extension >> ')
		
		self.input = extension
		self.loop_over_json()

		if self.lang == {}:
			print("Nothing found")
		else:
			self.exec()

if __name__ == '__main__':
	loci = Loci()
	loci.run()
