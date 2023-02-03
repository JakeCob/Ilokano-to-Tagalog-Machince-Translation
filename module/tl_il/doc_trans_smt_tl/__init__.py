from module.tl_il.rule_based_tl import dict_tl, remove_punct, tokenize, tag
from module.il_tl.rule_based_il import dict_il
from module.tl_il.doc_trans_tl import combine_tokens
from module.smt import encapsulate, ngram_var
import pandas as pd


def get_sum_tl(sen_poss_list, dict_source, not_in_sw, not_in_vb, not_in_nn, not_in_jj, not_in_rb, not_in_cc, not_in_pr, not_in_dt, not_tagged, sum_tf_idf_tl_list, vb_tl_tf_idf_list, nn_tl_tf_idf_list, jj_tl_tf_idf_list, rb_tl_tf_idf_list, cc_tl_tf_idf_list, pr_tl_tf_idf_list, dt_tl_tf_idf_list):
    sp_index = 0 # sentence POS index
    
    for sen_poss in sen_poss_list:
        # loop for getting the pos structure of every sentence
        """
        sen_poss is a list of POS of a sentence
        eg. ['VB', 'DT', 'NN', 'DT', 'NN']
        """
        sen_translation = []
        
        sum_tf_idf_tl = 0
        wp_index = 0 # word POS index
        
        for word_pos in sen_poss:
            word = dict_source['Tokenized'][sp_index][wp_index]
            # gets the word in every sentence
            
            # Matching Conditions    
            # 1. SW
            if word_pos == 'SW':
                """
                if the POS of the word is 'SW'
                """
                if word in dict_tl.sw_tl_list:
                    """
                    if the word is in the Tagalog list of single words
                    """
                    temp_index = dict_tl.sw_tl_list.index(word)
                    
                else:
                    not_in_sw.append(word) # for debugging purposes
                                
            # 2. SW
            elif word_pos == 'VB':
                """
                if the POS of the word is 'VB'
                """
                if word in dict_tl.vb_tl_list:
                    """
                    if the word is in the Tagalog list of verbs
                    """
                    temp_index = dict_tl.vb_tl_list.index(word)
                    sum_tf_idf_tl += vb_tl_tf_idf_list[temp_index]
                else:
                    not_in_vb.append(word) # for debugging purposes
            
            # 3. NN
            elif word_pos == 'NN':
                """
                if the POS of the word is 'NN'
                """
                if word in dict_tl.nn_tl_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_tl.nn_tl_list.index(word)
                    sum_tf_idf_tl += nn_tl_tf_idf_list[temp_index]
                else:
                    not_in_nn.append(word) # for debugging purposes
            
            # 4. JJ
            elif word_pos == 'JJ':
                """
                if the POS of the word is 'JJ'
                """
                if word in dict_tl.jj_tl_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_tl.jj_tl_list.index(word)
                    sum_tf_idf_tl += jj_tl_tf_idf_list[temp_index]
                else:
                    not_in_jj.append(word) # for debugging purposes
            
            # 5. RB
            elif word_pos == 'RB':
                """
                if the POS of the word is 'RB'
                """
                if word in dict_tl.rb_tl_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_tl.rb_tl_list.index(word)
                    sum_tf_idf_tl += rb_tl_tf_idf_list[temp_index]
                else:
                    not_in_rb.append(word) # for debugging purposes
                    
            # 6. CC
            elif word_pos == 'CC':
                """
                if the POS of the word is 'CC'
                """
                if word in dict_tl.cc_tl_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_tl.cc_tl_list.index(word)
                    sum_tf_idf_tl += cc_tl_tf_idf_list[temp_index]
                else:
                    not_in_cc.append(word) # for debugging purposes
                    
            # 7. PR
            elif word_pos == 'PR':
                """
                if the POS of the word is 'CC'
                """
                if word in dict_tl.pr_tl_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_tl.pr_tl_list.index(word)
                    sum_tf_idf_tl += pr_tl_tf_idf_list[temp_index]
                else:
                    not_in_pr.append(word) # for debugging purposes
            
             # 8. DT
            elif word_pos == 'DT':
                """
                if the POS of the word is 'DT'
                """
                if word in dict_tl.dt_tl_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_tl.dt_tl_list.index(word)
                    sum_tf_idf_tl += dt_tl_tf_idf_list[temp_index]
                else:
                    not_in_dt.append(word) # for debugging purposes
            
            else:
                not_tagged.append(word) # for debugging purposes
                
            wp_index += 1
        
        sum_tf_idf_tl_list.append(round(sum_tf_idf_tl, 5))
        sp_index += 1
        
    return sum_tf_idf_tl_list
# end of get_sum_tl


def trans_lm(ngram_data, tl_struct, il_struct, il_struct_count):
    trans_ngram_data = []
    for ngram_sen in ngram_data:
        trans_ngram_sen = []
        
        for ngram in ngram_sen:
            if ngram in tl_struct:
                temp_index = tl_struct.index(ngram)
                max_count = max(il_struct_count[temp_index])
                trans_index = il_struct_count[temp_index].index(max_count)
                trans_ngram = il_struct[temp_index][trans_index]
                trans_ngram_sen.append(trans_ngram)
            else:
                trans_ngram_sen.append(ngram)
                
            # np_index += 1
        
        trans_ngram_data.append(trans_ngram_sen)
        
    return trans_ngram_data
# end of function


def inFPhrases(word, word2, word3, word4, word5, tl_phrases):
    inFPhrases = False
    tl_phrase = []
    w_used = 0
    for phrase in tl_phrases:
        length = len(phrase)
        if length == 1:
            if word == phrase[0]:
                inFPhrases = True
                tl_phrase = phrase
                w_used = 1
        if length == 2:
            if word == phrase[0] and word2 == phrase[1]:
                inFPhrases = True
                tl_phrase = phrase
                w_used = 2
        if length == 3:
            if word == phrase[0] and word2 == phrase[1] and word3 == phrase[2]:
                inFPhrases = True
                tl_phrase = phrase
                w_used = 3
        if length == 4:
            if word == phrase[0] and word2 == phrase[1] and word3 == phrase[2] and word4 == phrase[3]:
                inFPhrases = True
                tl_phrase = phrase
                w_used = 4
        if length == 5:
            if word == phrase[0] and word2 == phrase[1] and word3 == phrase[2] and word4 == phrase[3] and word5 == phrase[4]:
                inFPhrases = True
                tl_phrase = phrase
                w_used = 5
                
    return inFPhrases, tl_phrase, w_used
# end of function


def translate_smt(sen_poss_list, dict_source, vb_tl_tf_idf_list, nn_tl_tf_idf_list, jj_tl_tf_idf_list, rb_tl_tf_idf_list, cc_tl_tf_idf_list, pr_tl_tf_idf_list, dt_tl_tf_idf_list, tl_struct, il_struct, il_struct_count):
    il_phrases = [remove_punct(word) for word in dict_il.il_phrases]
    il_phrases = [tokenize(word) for word in il_phrases]

    tl_phrases = [remove_punct(word) for word in dict_tl.tl_phrases]
    tl_phrases = [tokenize(word) for word in tl_phrases]
    
    not_in_sw = []
    not_in_vb = []
    not_in_nn = []
    not_in_jj = []
    not_in_rb = []
    not_in_cc = []
    not_in_pr = []
    not_in_dt = []
    not_tagged = []
    sum_tf_idf_tl_list = []

    sum_tf_idf_tl_list = get_sum_tl(sen_poss_list, dict_source, not_in_sw, not_in_vb, not_in_nn, not_in_jj, not_in_rb, not_in_cc, not_in_pr, not_in_dt, not_tagged, sum_tf_idf_tl_list, vb_tl_tf_idf_list, nn_tl_tf_idf_list, jj_tl_tf_idf_list, rb_tl_tf_idf_list, cc_tl_tf_idf_list, pr_tl_tf_idf_list, dt_tl_tf_idf_list)
    
    encapsulate(sen_poss_list, ngram_var.fourgram_list, ngram_var.trigram_list, ngram_var.bigram_list, ngram_var.unigram_list, ngram_var.ngram_list, ngram_var.notencap_list, ngram_var.fourgram_count_sen, ngram_var.trigram_count_sen, ngram_var.bigram_count_sen, ngram_var.unigram_count_sen, ngram_var.notencap_count_sen)
    
    ngram_data = ngram_var.ngram_list
    
    trans_ngram_data = trans_lm(ngram_data, tl_struct, il_struct, il_struct_count)
    
    sp_index = 0 # sentence POS index
    sen_translation_list = []
    
    for sen_poss in sen_poss_list:
        # loop for getting the pos structure of every sentence
        """
        sen_poss is a list of POS of a sentence
        eg. ['VB', 'DT', 'NN', 'DT', 'NN']
        """
        sen_translation = []
        wp_index = 0
        cur_wp_index = 0
        
        for word_pos in sen_poss:
            if wp_index == cur_wp_index:
                word = dict_source['Tokenized'][sp_index][wp_index]
                # gets the word in every sentence
                
                try: 
                    word2 = dict_source['Tokenized'][sp_index][wp_index+1]
                except:
                    word2 = None
                try:
                    word3 = dict_source['Tokenized'][sp_index][wp_index+2]
                except:
                    word3 = None
                try:
                    word4 = dict_source['Tokenized'][sp_index][wp_index+4]
                except:
                    word4 = None
                try:
                    word5 = dict_source['Tokenized'][sp_index][wp_index+4]
                except:
                    word5 = None                    
                    
                ans = inFPhrases(word, word2, word3, word4, word5, tl_phrases)
                inFPDict = ans[0]
                tl_phrase = ans[1]
                w_used = ans[2]                
                
                if inFPDict:
                    """
                    if the word is in the list of Tagalog phrases
                    """
                    p_index = tl_phrases.index(tl_phrase)
                    il_phrase = il_phrases[p_index]
                    for il_word in il_phrase:
                        sen_translation.append(il_word)
                    cur_wp_index = wp_index + w_used
                    
                else:
                    cur_wp_index = wp_index + 1
                
                    # Matching Conditions    
                    # 1. SW
                    if word_pos == 'SW':
                        """
                        if the POS of the word is 'SW'
                        """
                        if word in dict_tl.sw_tl_list:
                            temp_index = dict_tl.sw_tl_list.index(word)
                            if dict_tl.sw_il_list[temp_index][0] == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(dict_tl.sw_il_list[temp_index][0])
                        else:
                            sen_translation.append(word)
                    
                    # 2. VB
                    elif word_pos == 'VB':
                        """
                        if the POS of the word is 'VB'
                        """
                        if word in dict_tl.vb_tl_list:
                            """
                            if the word is in the Tagalog list of verbs
                            """
                            tl_index = dict_tl.vb_tl_list.index(word)
                            max_tlidf = max(dict_tl.vb_tfidf_il_list[tl_index])
                            il_index = dict_tl.vb_tfidf_il_list[tl_index].index(max_tlidf)
                            il_word = dict_tl.vb_il_list[tl_index][il_index]
                            
                            if il_word == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(il_word)
                        else:
                            sen_translation.append(word)
                    
                    # 3. NN
                    elif word_pos == 'NN':
                        """
                        if the POS of the word is 'NN'
                        """
                        if word in dict_tl.nn_tl_list:
                            """
                            if the word is in the Tagalog list of noun
                            """
                            tl_index = dict_tl.nn_tl_list.index(word)
                            max_tlidf = max(dict_tl.nn_tfidf_il_list[tl_index])
                            il_index = dict_tl.nn_tfidf_il_list[tl_index].index(max_tlidf)
                            il_word = dict_tl.nn_il_list[tl_index][il_index]
                            
                            if il_word == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(il_word)
                        else:
                            sen_translation.append(word)
                    
                    # 4. JJ
                    elif word_pos == 'JJ':
                        """
                        if the POS of the word is 'JJ'
                        """
                        if word in dict_tl.jj_tl_list:
                            """
                            if the word is in the Tagalog list of adjectives
                            """
                            tl_index = dict_tl.jj_tl_list.index(word)
                            max_tlidf = max(dict_tl.jj_tfidf_il_list[tl_index])
                            il_index = dict_tl.jj_tfidf_il_list[tl_index].index(max_tlidf)
                            il_word = dict_tl.jj_il_list[tl_index][il_index]
                            
                            if il_word == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(il_word)
                        else:
                            sen_translation.append(word)
                            
                    # 5. RB
                    elif word_pos == 'RB':
                        """
                        if the POS of the word is 'RB'
                        """
                        if word in dict_tl.rb_tl_list:
                            """
                            if the word is in the Tagalog list of adverbs
                            """
                            tl_index = dict_tl.rb_tl_list.index(word)
                            max_tlidf = max(dict_tl.rb_tfidf_il_list[tl_index])
                            il_index = dict_tl.rb_tfidf_il_list[tl_index].index(max_tlidf)
                            il_word = dict_tl.rb_il_list[tl_index][il_index]
                            
                            if il_word == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(il_word)
                        else:
                            sen_translation.append(word)
                    
                    # 6. CC
                    elif word_pos == 'CC':
                        """
                        if the POS of the word is 'CC'
                        """
                        if word in dict_tl.cc_tl_list:
                            """
                            if the word is in the Tagalog list of conjunctions
                            """
                            tl_index = dict_tl.cc_tl_list.index(word)
                            max_tlidf = max(dict_tl.cc_tfidf_il_list[tl_index])
                            il_index = dict_tl.cc_tfidf_il_list[tl_index].index(max_tlidf)
                            il_word = dict_tl.cc_il_list[tl_index][il_index]
                            
                            if il_word == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(il_word)
                        else:
                            sen_translation.append(word)
                            
                    # 7. PR
                    elif word_pos == 'PR':
                        """
                        if the POS of the word is 'PR'
                        """
                        if word in dict_tl.pr_tl_list:
                            """
                            if the word is in the Tagalog list of prepositions
                            """
                            tl_index = dict_tl.pr_tl_list.index(word)
                            max_tlidf = max(dict_tl.pr_tfidf_il_list[tl_index])
                            il_index = dict_tl.pr_tfidf_il_list[tl_index].index(max_tlidf)
                            il_word = dict_tl.pr_il_list[tl_index][il_index]
                            
                            if il_word == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(il_word)
                        else:
                            sen_translation.append(word)
                            
                    # 8. DT
                    elif word_pos == 'DT':
                        """
                        if the POS of the word is 'DT'
                        """
                        if word in dict_tl.dt_tl_list:
                            """
                            if the word is in the Tagalog list of determiners
                            """
                            tl_index = dict_tl.dt_tl_list.index(word)
                            max_tlidf = max(dict_tl.dt_tfidf_il_list[tl_index])
                            il_index = dict_tl.dt_tfidf_il_list[tl_index].index(max_tlidf)
                            il_word = dict_tl.dt_il_list[tl_index][il_index]
                            
                            if il_word == 'None':
                                sen_translation.append(word)
                            else:
                                sen_translation.append(il_word)
                        else:
                            sen_translation.append(word)
                    
                    else:
                        sen_translation.append(word)

            wp_index += 1
        sp_index += 1
        sen_translation_list.append(sen_translation)
    
    return sen_translation_list
# end of function

def smt_trans(source):
    parsed_source = source.split("\r\n")
    cleaned_source = [remove_punct(word) for word in parsed_source]
    toklenized_source = [tokenize(word) for word in cleaned_source]
    dict_source = pd.DataFrame({'Tokenized': toklenized_source}) 
    pos_sen_list = tag(dict_source['Tokenized'])
    dict_source['POS'] = pos_sen_list
    sen_translation_list = translate_smt(dict_source['POS'], dict_source, dict_tl.vb_tl_tf_idf_list, dict_tl.nn_tl_tf_idf_list, dict_tl.jj_tl_tf_idf_list, dict_tl.rb_tl_tf_idf_list, dict_tl.cc_tl_tf_idf_list, dict_tl.pr_tl_tf_idf_list, dict_tl.dt_tl_tf_idf_list, dict_tl.tl_struct, dict_tl.il_struct, dict_tl.il_struct_count)
    temp_sen_list = combine_tokens(sen_translation_list)
    # Dictionary of the system output and the expected output and their scores
    dict_op_ex = pd.DataFrame({'System Output': temp_sen_list})

    return dict_op_ex
# end of function