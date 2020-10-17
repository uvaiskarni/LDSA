#!/usr/bin/env python
import sys
import json
import re

pronouns = ['hen','hon','den','det','denna','denne','han']

def read_input(file):
    for line in file:
        if line.strip():
           json_line = json.loads(line)
           if json_line['retweeted'] == False:
              yield json_line['text'].split(' ')

def match_word(word):
    #Match the pronoun for each word of the tweet text
    for i in range(len(pronouns)):
        raw_string = "\\b" + pronouns[i] + "\\b"
        regex_name = re.compile(raw_string,re.IGNORECASE)
        x = regex_name.search(word)
        if x:
           return i,x
    return i,0

def main(separator='\t'):
            data = read_input(sys.stdin)
            for words in data:
                for word in words:
                    i,x = match_word(word)
                    if x:
                       print '%s%s%d' % (pronouns[i],separator,1)


if __name__ == "__main__":
    main()
