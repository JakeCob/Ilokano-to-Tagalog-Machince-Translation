import pandas as pd

# Opening the file
ilokano_raw = open("Data/Ilokano_Bible.txt").read()
tagalog_raw = open("Data/Tagalog_Bible.txt").read()
# Printing the Raw Data
# ilokano_raw[0:500]
# tagalog_raw[0:500]


# Parsing the data
parsedIlokano = ilokano_raw.split('\n')
parsedTagalog = tagalog_raw.split('\n')
# Printing the parsed data
# parsedIlokano[0:3]
# parsedTagalog[0:3]


# Creating an Ilokano-Tagalog Dictionary
dict_bible = pd.DataFrame({
    'ilokano': parsedIlokano,
    'tagalog': parsedTagalog
})

# Printing the first 5 elements of the dictionary
# dict_bible.head()
