#!/usr/bin/env python3
import argparse
"""
Welcome to LOCI - Lines Of Codes Indicator

This is a simple program that finds total lines of codes you've written

Update ~/.config/.loci.json file to update ignored files to accuretly count how many lines
of codes you've written .

The ./example folder is there to test . It contains nothing of the logic
"""

import os
import json
import sys
from data import PRE_JSON


class Loci:
    def __init__(self):
        self.json: dict = {}
        self.lang: dict = {}
        self.input: str = ''
        self.load_json()

    def load_home_file(self):
        return os.path.join(os.path.expanduser('~/.config'), 'loci.json')

    def load_json(self):
        if(os.path.exists(self.load_home_file())):
            json_file = open(self.load_home_file(), 'r')
            self.json = json.loads(''.join(json_file.readlines()))
            json_file.close()

        else:
            json_file = open(self.load_home_file(), 'x')
            json_file.writelines(PRE_JSON)
            self.json = json.loads(PRE_JSON)
            json_file.close()

    def loop_over_json(self):
        for k, v in self.json.items():
            if self.input in v['ids']:
                self.lang = self.json[k]

    def exec(self, directory):
        print()
        print('Directory \"%s\"' % (os.path.abspath(directory)))
        print()

        extension_files = []

        for root, _, files in os.walk(os.path.abspath(directory)):
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
            print("No file found under extension %s" %
                  (self.lang['extension']))
        else:
            max_len = len(max(data.keys(), key=len))

        for (k, v) in data.items():
            print("\"%s\"" % k + ' ' * (max_len - len(k)) + ' %s' % v)
            total += v

        print()
        print("Total %d lines" % (total))
        print()
        self.high_low(data)
        print()

    def high_low(self, data: dict):
        highest = max(data.values())
        lowest = min(data.values())
        highest_data = {}
        lowest_data = {}

        empty_files = []

        for (k, v) in data.items():
            if (v == highest):
                highest_data = {k: v}
            if (v == lowest):
                lowest_data = {k: v}
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

    def run(self, extension, directory):

        self.input = extension
        self.loop_over_json()

        if self.lang == {}:
            print("Nothing found")
        else:
            self.exec(directory)


def create_parser():
    parser = argparse.ArgumentParser(description='Line of Code Indicator')
    parser.add_argument('extension', help='file extension to parse')
    parser.add_argument('-i', '--input', nargs=1, help='files to')
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    directory = args.input[0] if args.input else os.curdir

    loci = Loci()
    loci.run(args.extension, directory)
