text_file = open("src/text data/Bible_Tagalog.txt", "r")
sentence_array = []
lines = text_file.readlines()
sentence_array = lines

for sentence in sentence_array: # loop for going through each sentence in the array
    sentence = sentence.split()
    word_count = dict()
    term_frequency = dict()

    for word in sentence: # loop for each word in a sentence
        if word in word_count: 
            # to be added: if word matches POS of existing word in the list
            word_count[word] += 1
            # to be added: else if the word does not match the POS of existing word in the list
                # word_count[word] = 1
        else:
            word_count[word] = 1

    print("SENTENCE = ", sentence)
    print("WORD COUNT = ", word_count)

    for word in word_count:    
        term_frequency[word] = round(word_count[word]/len(sentence), 2)
    print("TERM FREQUENCY = ", term_frequency, "\n")