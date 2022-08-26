import pandas as pd
import string

def remove_punct(pText):
    text_nopunct = "".join([char for char in pText if char not in string.punctuation])
    return text_nopunct
