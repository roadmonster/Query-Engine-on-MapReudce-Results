#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter

import sys

current_word = None
unique_id_count = 0
word = None
id_list = []
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, docid = line.split('\t', 1)
    
    if current_word == word:
        id_list.append(docid)
	
        
    else:
        if current_word:
            unique_id_count = len(set(id_list))
	    
            print '%s\t%s\t' %(word, unique_id_count)
        id_list = []
        id_list.append(docid)
	current_word = word


if current_word == word:
    print '%s\t%s' % (current_word, len(set(id_list)))


