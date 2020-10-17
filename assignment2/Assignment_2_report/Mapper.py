#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""
import json
import re
import sys

def read_input(file):
    for line in file:
	if line.strip():
            # split the line into words
	    parsed_json_line = json.loads(line)
	    if parsed_json_line['retweeted'] != True:
	        # split line to words using  space
	        yield parsed_json_line['text'].split(' ')

def main(separator='\t'):
    pronoun_list = ['han','hon','den','det','denna','denne','hen']
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
	    # check whether the words match from pronoun list
	    for i in range(7):
	        match_or_not = re.search(r'^'+str(pronoun_list[i])+'$',word.lower())
		if match_or_not:
		    print(str(pronoun_list[i])+str(separator)+"1")

if __name__ == "__main__":
    main()
