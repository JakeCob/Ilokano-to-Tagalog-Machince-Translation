from rule_based_il import dict_il, lists_il, remove_punct, tokenize, tag
from doc_trans_tl import combine_tokens
from smt import encapsulate, ngram_var
import pandas as pd

def get_sum_il(sen_poss_list, dict_source, not_in_sw, not_in_vb, not_in_nn, not_in_jj, not_in_rb, not_in_cc, not_in_pr, not_in_dt, not_tagged, sum_tf_idf_il_list, vb_il_tf_idf_list, nn_il_tf_idf_list, jj_il_tf_idf_list, rb_il_tf_idf_list, cc_il_tf_idf_list, pr_il_tf_idf_list, dt_il_tf_idf_list):
    sp_index = 0 # sentence POS index
    
    for sen_poss in sen_poss_list:
        # loop for getting the pos structure of every sentence
        """
        sen_poss is a list of POS of a sentence
        eg. ['VB', 'DT', 'NN', 'DT', 'NN']
        """
        sen_translation = []
        
        sum_tf_idf_il = 0
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
                if word in dict_il.sw_il_list:
                    """
                    if the word is in the Tagalog list of single words
                    """
                    temp_index = dict_il.sw_il_list.index(word)
                    
                else:
                    not_in_sw.append(word) # for debugging purposes
                                
            # 2. SW
            elif word_pos == 'VB':
                """
                if the POS of the word is 'VB'
                """
                if word in dict_il.vb_il_list:
                    """
                    if the word is in the Tagalog list of verbs
                    """
                    temp_index = dict_il.vb_il_list.index(word)
                    sum_tf_idf_il += vb_il_tf_idf_list[temp_index]
                else:
                    not_in_vb.append(word) # for debugging purposes
            
            # 3. NN
            elif word_pos == 'NN':
                """
                if the POS of the word is 'NN'
                """
                if word in dict_il.nn_il_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_il.nn_il_list.index(word)
                    sum_tf_idf_il += nn_il_tf_idf_list[temp_index]
                else:
                    not_in_nn.append(word) # for debugging purposes
            
            # 4. JJ
            elif word_pos == 'JJ':
                """
                if the POS of the word is 'JJ'
                """
                if word in dict_il.jj_il_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_il.jj_il_list.index(word)
                    sum_tf_idf_il += jj_il_tf_idf_list[temp_index]
                else:
                    not_in_jj.append(word) # for debugging purposes
            
            # 5. RB
            elif word_pos == 'RB':
                """
                if the POS of the word is 'RB'
                """
                if word in dict_il.rb_il_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_il.rb_il_list.index(word)
                    sum_tf_idf_il += rb_il_tf_idf_list[temp_index]
                else:
                    not_in_rb.append(word) # for debugging purposes
                    
            # 6. CC
            elif word_pos == 'CC':
                """
                if the POS of the word is 'CC'
                """
                if word in dict_il.cc_il_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_il.cc_il_list.index(word)
                    sum_tf_idf_il += cc_il_tf_idf_list[temp_index]
                else:
                    not_in_cc.append(word) # for debugging purposes
                    
            # 7. PR
            elif word_pos == 'PR':
                """
                if the POS of the word is 'CC'
                """
                if word in dict_il.pr_il_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_il.pr_il_list.index(word)
                    sum_tf_idf_il += pr_il_tf_idf_list[temp_index]
                else:
                    not_in_pr.append(word) # for debugging purposes
            
             # 8. DT
            elif word_pos == 'DT':
                """
                if the POS of the word is 'DT'
                """
                if word in dict_il.dt_il_list:
                    """
                    if the word is in the Tagalog list of nouns
                    """
                    temp_index = dict_il.dt_il_list.index(word)
                    sum_tf_idf_il += dt_il_tf_idf_list[temp_index]
                else:
                    not_in_dt.append(word) # for debugging purposes
            
            else:
                not_tagged.append(word) # for debugging purposes
                
            wp_index += 1
        
        sum_tf_idf_il_list.append(round(sum_tf_idf_il, 5))
        sp_index += 1
        
    return sum_tf_idf_il_list
# end of get_sum_il

def il_trans_lm(ngram_data, il_struct, tl_struct, tl_struct_count):
    trans_ngram_data = []
    for ngram_sen in ngram_data:
        trans_ngram_sen = []
        
        for ngram in ngram_sen:
            if ngram in il_struct:
                temp_index = il_struct.index(ngram)
                max_count = max(tl_struct_count[temp_index])
                trans_index = tl_struct_count[temp_index].index(max_count)
                trans_ngram = tl_struct[temp_index][trans_index]
                trans_ngram_sen.append(trans_ngram)
            else:
                trans_ngram_sen.append(ngram)
                
            # np_index += 1
        
        trans_ngram_data.append(trans_ngram_sen)
        
    return trans_ngram_data
# end of function

def il_translate_smt(sen_poss_list, dict_source, vb_il_tf_idf_list, nn_il_tf_idf_list, jj_il_tf_idf_list, rb_il_tf_idf_list, cc_il_tf_idf_list, pr_il_tf_idf_list, dt_il_tf_idf_list, il_struct, tl_struct, tl_struct_count):
    not_in_sw = []
    not_in_vb = []
    not_in_nn = []
    not_in_jj = []
    not_in_rb = []
    not_in_cc = []
    not_in_pr = []
    not_in_dt = []
    not_tagged = []
    sum_tf_idf_il_list = []

    sum_tf_idf_il_list = get_sum_il(sen_poss_list, dict_source, not_in_sw, not_in_vb, not_in_nn, not_in_jj, not_in_rb, not_in_cc, not_in_pr, not_in_dt, not_tagged, sum_tf_idf_il_list, vb_il_tf_idf_list, nn_il_tf_idf_list, jj_il_tf_idf_list, rb_il_tf_idf_list, cc_il_tf_idf_list, pr_il_tf_idf_list, dt_il_tf_idf_list)
    
    encapsulate(sen_poss_list, ngram_var.fourgram_list, ngram_var.trigram_list, ngram_var.bigram_list, ngram_var.unigram_list, ngram_var.ngram_list, ngram_var.notencap_list, ngram_var.fourgram_count_sen, ngram_var.trigram_count_sen, ngram_var.bigram_count_sen, ngram_var.unigram_count_sen, ngram_var.notencap_count_sen)
    
    ngram_data = ngram_var.ngram_list
    
    trans_ngram_data = il_trans_lm(ngram_data, il_struct, tl_struct, tl_struct_count)
    
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
        
        for word_pos in sen_poss:
            word = dict_source['Tokenized'][sp_index][wp_index]
            # gets the word in every sentence
            
            # Matching Conditions    
            # 1. SW
            if word_pos == 'SW':
                """
                if the POS of the word is 'SW'
                """
                if word in dict_il.sw_il_list:
                    temp_index = dict_il.sw_il_list.index(word)
                    if dict_il.sw_tl_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_il.sw_tl_list[temp_index][0])
                else:
                    sen_translation.append(word)
            
            # 2. VB
            elif word_pos == 'VB':
                """
                if the POS of the word is 'VB'
                """
                if word in dict_il.vb_il_list:
                    """
                    if the word is in the Tagalog list of verbs
                    """
                    il_index = dict_il.vb_il_list.index(word)
                    max_ilidf = max(dict_il.vb_tfidf_tl_list[il_index])
                    tl_index = dict_il.vb_tfidf_tl_list[il_index].index(max_ilidf)
                    tl_word = dict_il.vb_tl_list[il_index][tl_index]
                    
                    if tl_word == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(tl_word)
                else:
                    sen_translation.append(word)
            
            # 3. NN
            elif word_pos == 'NN':
                """
                if the POS of the word is 'NN'
                """
                if word in dict_il.nn_il_list:
                    """
                    if the word is in the Tagalog list of noun
                    """
                    il_index = dict_il.nn_il_list.index(word)
                    max_ilidf = max(dict_il.nn_tfidf_tl_list[il_index])
                    tl_index = dict_il.nn_tfidf_tl_list[il_index].index(max_ilidf)
                    tl_word = dict_il.nn_tl_list[il_index][tl_index]
                    
                    if tl_word == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(tl_word)
                else:
                    sen_translation.append(word)
            
            # 4. JJ
            elif word_pos == 'JJ':
                """
                if the POS of the word is 'JJ'
                """
                if word in dict_il.jj_il_list:
                    """
                    if the word is in the Tagalog list of adjectives
                    """
                    il_index = dict_il.jj_il_list.index(word)
                    max_ilidf = max(dict_il.jj_tfidf_tl_list[il_index])
                    tl_index = dict_il.jj_tfidf_tl_list[il_index].index(max_ilidf)
                    tl_word = dict_il.jj_tl_list[il_index][tl_index]
                    
                    if tl_word == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(tl_word)
                else:
                    sen_translation.append(word)
                    
            # 5. RB
            elif word_pos == 'RB':
                """
                if the POS of the word is 'RB'
                """
                if word in dict_il.rb_il_list:
                    """
                    if the word is in the Tagalog list of adverbs
                    """
                    il_index = dict_il.rb_il_list.index(word)
                    max_ilidf = max(dict_il.rb_tfidf_tl_list[il_index])
                    tl_index = dict_il.rb_tfidf_tl_list[il_index].index(max_ilidf)
                    tl_word = dict_il.rb_tl_list[il_index][tl_index]
                    
                    if tl_word == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(tl_word)
                else:
                    sen_translation.append(word)
            
            # 6. CC
            elif word_pos == 'CC':
                """
                if the POS of the word is 'CC'
                """
                if word in dict_il.cc_il_list:
                    """
                    if the word is in the Tagalog list of conjunctions
                    """
                    il_index = dict_il.cc_il_list.index(word)
                    max_ilidf = max(dict_il.cc_tfidf_tl_list[il_index])
                    tl_index = dict_il.cc_tfidf_tl_list[il_index].index(max_ilidf)
                    tl_word = dict_il.cc_tl_list[il_index][tl_index]
                    
                    if tl_word == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(tl_word)
                else:
                    sen_translation.append(word)
                    
            # 7. PR
            elif word_pos == 'PR':
                """
                if the POS of the word is 'PR'
                """
                if word in dict_il.pr_il_list:
                    """
                    if the word is in the Tagalog list of prepositions
                    """
                    il_index = dict_il.pr_il_list.index(word)
                    max_ilidf = max(dict_il.pr_tfidf_tl_list[il_index])
                    tl_index = dict_il.pr_tfidf_tl_list[il_index].index(max_ilidf)
                    tl_word = dict_il.pr_tl_list[il_index][tl_index]
                    
                    if tl_word == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(tl_word)
                else:
                    sen_translation.append(word)
                    
            # 8. DT
            elif word_pos == 'DT':
                """
                if the POS of the word is 'DT'
                """
                if word in dict_il.dt_il_list:
                    """
                    if the word is in the Tagalog list of determiners
                    """
                    il_index = dict_il.dt_il_list.index(word)
                    max_ilidf = max(dict_il.dt_tfidf_tl_list[il_index])
                    tl_index = dict_il.dt_tfidf_tl_list[il_index].index(max_ilidf)
                    tl_word = dict_il.dt_tl_list[il_index][tl_index]
                    
                    if tl_word == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(tl_word)
                else:
                    sen_translation.append(word)
            
            else:
                sen_translation.append(word)

            wp_index += 1
        sp_index += 1
        sen_translation_list.append(sen_translation)
    
    return sen_translation_list
# end of function

def il_smt_trans(source):
    parsed_source = source.split("\r\n")
    cleaned_source = [remove_punct(word) for word in parsed_source]
    toklenized_source = [tokenize(word) for word in cleaned_source]
    dict_source = pd.DataFrame({'Tokenized': toklenized_source}) 
    pos_sen_list = tag(dict_source['Tokenized'])
    dict_source['POS'] = pos_sen_list
    sen_translation_list = il_translate_smt(dict_source['POS'], dict_source, dict_il.vb_il_tf_idf_list, dict_il.nn_il_tf_idf_list, dict_il.jj_il_tf_idf_list, dict_il.rb_il_tf_idf_list, dict_il.cc_il_tf_idf_list, dict_il.pr_il_tf_idf_list, dict_il.dt_il_tf_idf_list, dict_il.il_struct, dict_il.tl_struct, dict_il.tl_struct_count)
    temp_sen_list = combine_tokens(sen_translation_list)
    # Dictionary of the system output and the expected output and their scores
    dict_il_op_ex = pd.DataFrame({'System Output': temp_sen_list})
    
    return dict_il_op_ex
# end of function