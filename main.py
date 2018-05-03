#!/usr/bin/env python3

import csv # Standard library

import requests # Third-party module


# Read from a file
def read_from_a_file(pathname):
    with open(pathname, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            print(row)


# Write to a file
def write_to_a_file(pathname, resource):
    with open(pathname, 'w') as f:
        f.write(requests.get(resource).text)


def append_to_a_file(pathname):
    with open(pathname, 'a') as f:
        f.write('#thistoo')


if __name__ == '__main__':
    #read_from_a_file('level_1/level_2/level_3/short.csv')
    #write_to_a_file('level_1/example.html','http://byteacademy.co')
    append_to_a_file('level_1/level_2/example.json')
