#! /usr/local/bin/python3

"""
Welcome to LOCI - Lines Of Codes Indicator

This is a simple program that finds total lines of codes you've written

Update ~/.loci.json file to update ignored files to accuretly count how many lines
of codes you've written .

The ./example folder is there to test . It contains nothing of the logix
"""

import os
import json
import sys
from data import PRE_JSON

class Loci:
	def __init__(self):
		self.json = {}
		self.lang = {}
		self.input = ''
		self.load_json()

	def load_home_file(self):
		user = os.getlogin()
		return f'/Users/{user}/.loci.json'

	def load_json(self):
		if(os.path.exists(self.load_home_file())):
			json_file = open(self.load_home_file(), 'r')
			self.json = json.loads(''.join(json_file.readlines()))
			json_file.close()

		else:
			# TODO
			# See online docs on how to make a file

			os.mkdir(self.load_home_file())
			json_file = open(self.load_home_file(), 'w')
			json_file.writelines(PRE_JSON)
			self.json = json.loads(PRE_JSON)
			json_file.close()


	def loop_over_json(self):
		for k, v in self.json.items():
			if self.input in v['ids']:
				self.lang = self.json[k]

	def exec(self):
		print('Current directory \"%s\"' % (os.path.abspath(os.curdir)))
		print()

		extension_files = []

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

		max_len = 0
		total = 0

		if len(data.items()) == 0:
			print("No file found under extension %s" % (self.lang['extension']))
		else:
			max_len = len(max(data.keys(), key=len))

		for (k, v) in data.items():
			print("\"%s\"" % k + ' ' * (max_len - len(k)) + ' %s' % v)
			total += v
		
		print()
		print("Total %d lines" % (total))
		print()
		self.high(data)
		print()

	def high(self, data: dict):
		highest = max(data.values())
		lowest = min(data.values())
		highest_data = {}
		lowest_data = {}

		empty_files = []
		
		for (k, v) in data.items():
			if (v == highest):
				highest_data = {k:v}
			if (v == lowest):
				lowest_data = {k:v}
			if (v == 0):
				empty_files.append(k)

		for (k, v) in highest_data.items():
			print("Biggest file : \"%s\" with %d lines" % (k, v))	

		for (k, v) in lowest_data.items():
			print("Smallest file : \"%s\" with %d lines" % (k, v))

		if len(empty_files) != 0:
			print()
			print("Empty files")
			for file in empty_files:
				print("\"%s\"" % file)

	def show_json(self):
		print(self.json)

	def run(self):
		try:
			extension = sys.argv[1]
		except:
			extension = ""
		
		self.input = extension
		self.loop_over_json()

		if self.lang == {}:
			print("Nothing found")
		else:
			self.exec()

if __name__ == '__main__':
	loci = Loci()
	loci.run()
