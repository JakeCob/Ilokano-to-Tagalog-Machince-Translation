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

# Printing the first 5 elements of the dictionary
# dict_bible.head()

dict_bible['ilokano_clean'] = dict_bible['ilokano'].apply(lambda x: clean_data.remove_punct(x))
dict_bible['tagalog_clean'] = dict_bible['tagalog'].apply(lambda x: clean_data.remove_punct(x))
print(dict_bible)
