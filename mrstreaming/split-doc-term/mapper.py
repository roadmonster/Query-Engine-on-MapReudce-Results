#!/usr/bin/env python
"""mapper.py"""

import sys
import string

import re


for line in sys.stdin:
    
    line = line.strip();
    
    filenameword, count = line.split('\t', 1)
    
    filename, word = filenameword.split('+')
    
    print '%s\t%s\t%s\t' % (filename,word,count)
        
        
