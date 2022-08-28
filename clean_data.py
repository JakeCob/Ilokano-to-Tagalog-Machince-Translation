import pandas as pd
import string
import re

# Opening the Stopwords
tagalog_stopwords = open("Data/stopwords-tl.txt").read()

# Parsing the stopwords
parsed_sw_tl = tagalog_stopwords.split('\n')

def remove_punct(pText):
    text_nopunct = "".join([char for char in pText if char not in string.punctuation])
    return text_nopunct

def tokenize(pText):
    tokens = re.split('\W+', pText)
    return tokens

def remove_stopwords(ptokenized_list):
    text = [word for word in ptokenized_list if word not in parsed_sw_tl]
    return text
