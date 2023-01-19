import clean_data
import pandas as pd

# Opening the file
ilokano_raw = open("Data/Ilokano_Bible.txt").read()
tagalog_raw = open("Data/Tagalog_Bible.txt").read()


# Parsing the data
parsedIlokano = ilokano_raw.split('\n')
parsedTagalog = tagalog_raw.split('\n')


# Creating an Ilokano-Tagalog Dictionary
dict_bible = pd.DataFrame({
    'ilokano': parsedIlokano,
    'tagalog': parsedTagalog
})

dict_bible['ilokano_nopunc'] = dict_bible['ilokano'].apply(lambda x: clean_data.remove_punct(x))
dict_bible['tagalog_nopunc'] = dict_bible['tagalog'].apply(lambda x: clean_data.remove_punct(x))

dict_bible['ilokano_tokenized'] = dict_bible['ilokano_nopunc'].apply(lambda x: clean_data.tokenize(x.lower()))
dict_bible['tagalog_tokenized'] = dict_bible['tagalog_nopunc'].apply(lambda x: clean_data.tokenize(x.lower()))

dict_bible['tagalog_nostopwords'] = dict_bible['tagalog_tokenized'].apply(lambda x: clean_data.remove_stopwords(x))

print(dict_bible)
