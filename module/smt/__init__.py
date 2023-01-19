import pandas as pd
import numpy as np


def nGram(text, n):
    
    ngrams=[]
    #collect n-gram
    for i in range(len(text)-n+1): # i is the index of the first word of the n-gram
        temp=[text[j] for j in range(i, i+n)] # j is the index of the word in the n-gram
        ngrams.append(" ".join(temp))
        
    return ngrams
# end of nGram


def encapsulate(pos_sen_list, fourgram_list, trigram_list, bigram_list, unigram_list, ngram_list, notencap_list,fourgram_count_sen, trigram_count_sen, bigram_count_sen, unigram_count_sen, notencap_count_sen):
  for pos_sen in pos_sen_list: # loop for going through all the POS sentence structures
    unigram = []
    bigram = []
    trigram = []
    fourgram = []
    ngram = []
    notencap = []
    
    unigram_count = 0
    bigram_count = 0
    trigram_count=0
    fourgram_count=0
    notencap_count = 0

    pos_index = 0
    curr_pos = 0
    next_pos = ""
    next2_pos= ""
    next3_pos= ""
    
    
    for pos in pos_sen: # loop for all the POS in a sentence
      if pos_index != curr_pos and pos_index != 0:
        pass
      
      else:
        if pos_index < (len(pos_sen) - 1):
          next_pos = pos_sen[pos_index+1]
        
        if pos_index < (len(pos_sen) - 2):
          next2_pos = pos_sen[pos_index + 2]
            
        if pos_index < (len(pos_sen) - 3):
          next3_pos = pos_sen[pos_index + 3]
        
        # FOURGRAMS
        if pos == 'VB' and next_pos == 'DT'  and next2_pos == 'JJ' and next3_pos == 'NN':
          fourgram.extend([[pos, next_pos, next2_pos, next3_pos]])
          ngram.extend([[pos, next_pos, next2_pos, next3_pos]])
          fourgram_count += 1
          curr_pos = pos_index + 4

        elif pos == 'NN' and next_pos == 'DT'  and next2_pos == 'JJ' and next3_pos == 'VB':
          fourgram.extend([[pos, next_pos, next2_pos, next3_pos]])
          ngram.extend([[pos, next_pos, next2_pos, next3_pos]])
          fourgram_count += 1
          curr_pos = pos_index + 4
          
        elif pos == 'JJ' and next_pos == 'NN'  and next2_pos == 'RB' and next3_pos == 'VB':
          fourgram.extend([[pos, next_pos, next2_pos, next3_pos]])
          ngram.extend([[pos, next_pos, next2_pos, next3_pos]])
          fourgram_count += 1
          curr_pos = pos_index + 4
          
        elif pos == 'DT' and next_pos == 'NN'  and next2_pos == 'DT' and next3_pos == 'VB':
          fourgram.extend([[pos, next_pos, next2_pos, next3_pos]])
          ngram.extend([[pos, next_pos, next2_pos, next3_pos]])
          fourgram_count += 1
          curr_pos = pos_index + 4
          
        elif pos == 'DT' and next_pos == 'VB'  and next2_pos == 'DT' and next3_pos == 'NN':
          fourgram.extend([[pos, next_pos, next2_pos, next3_pos]])
          ngram.extend([[pos, next_pos, next2_pos, next3_pos]])
          fourgram_count += 1
          curr_pos = pos_index + 4
          
        elif pos == 'DT' and next_pos == 'NN'  and next2_pos == 'DT' and next3_pos == 'JJ':
          fourgram.extend([[pos, next_pos, next2_pos, next3_pos]])
          ngram.extend([[pos, next_pos, next2_pos, next3_pos]])
          fourgram_count += 1
          curr_pos = pos_index + 4
        
        elif pos == 'DT' and next_pos == 'JJ'  and next2_pos == 'DT' and next3_pos == 'NN':
          fourgram.extend([[pos, next_pos, next2_pos, next3_pos]])
          ngram.extend([[pos, next_pos, next2_pos, next3_pos]])
          fourgram_count += 1
          curr_pos = pos_index + 4
          
        # TRIGRAMS
        elif pos == 'VB' and next_pos == 'DT'  and next2_pos == 'NN':
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3

        elif pos == 'RB' and next_pos == 'DT'  and next2_pos == 'VB':
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3
          
        elif pos == 'DT' and next_pos == 'JJ'  and next2_pos == 'NN':
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3
          
        elif pos == 'DT' and next_pos == 'NN'  and next2_pos == 'VB': # from IL
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3
        
        elif pos == 'DT' and next_pos == 'NN'  and next2_pos == 'JJ': # from IL
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3
          
        elif pos == 'VB' and next_pos == 'DT'  and next2_pos == 'JJ':
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3 
          
        elif pos == 'JJ' and next_pos == 'DT'  and next2_pos == 'VB':
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3 
        
        elif pos == 'RB' and next_pos == 'DT'  and next2_pos == 'JJ':
          trigram.extend([[pos, next_pos, next2_pos]])
          ngram.extend([[pos, next_pos, next2_pos]])
          trigram_count += 1
          curr_pos = pos_index + 3

        # BIGRAMS
        elif len(pos_sen) == 2:
          bigram.extend([[pos, next_pos]])
          ngram.extend([[pos, next_pos]])
          bigram_count += 1
          curr_pos = pos_index + 2

        elif pos == 'DT' and next_pos == 'NN':
          bigram.extend([[pos, next_pos]])
          ngram.extend([[pos, next_pos]])
          bigram_count += 1
          curr_pos = pos_index + 2
        
        elif pos == 'VB' and next_pos == 'NN':
          bigram.extend([[pos, next_pos]])
          ngram.extend([[pos, next_pos]])
          bigram_count += 1
          curr_pos = pos_index + 2

        elif pos == 'JJ' and next_pos == 'NN':
          bigram.extend([[pos, next_pos]])
          ngram.extend([[pos, next_pos]])
          bigram_count += 1
          curr_pos = pos_index + 2
          
        elif pos == 'NN' and next_pos == 'VB':
          bigram.extend([[pos, next_pos]])
          ngram.extend([[pos, next_pos]])
          bigram_count += 1
          curr_pos = pos_index + 2

        # UNIGRAMS
        elif pos == 'CC' or pos == 'SW':
          unigram.append([pos])
          ngram.append([pos])
          unigram_count += 1
          curr_pos = pos_index + 1
          
        else:
          notencap.append([pos])
          ngram.append([pos])
          notencap_count += 1
          curr_pos = pos_index + 1
          
          
      pos_index += 1
    
    fourgram_list.append(fourgram)
    trigram_list.append(trigram)
    bigram_list.append(bigram)
    unigram_list.append(unigram)
    ngram_list.append(ngram)
    notencap_list.append(notencap)
    
    fourgram_count_sen.append(fourgram_count) 
    trigram_count_sen.append(trigram_count)
    bigram_count_sen.append(bigram_count)
    unigram_count_sen.append(unigram_count)
    notencap_count_sen.append(notencap_count)
    
    fourgram_count_list = np.array(fourgram_count_sen)
    trigram_count_list = np.array(trigram_count_sen)
    bigram_count_list = np.array(bigram_count_sen)
    unigram_count_list = np.array(unigram_count_sen)
    notencap_count_list = np.array(notencap_count_sen)

    ngram_count = fourgram_count_list + trigram_count_list + bigram_count_list + unigram_count_list + notencap_count_list
  return ngram_count
# end of function

