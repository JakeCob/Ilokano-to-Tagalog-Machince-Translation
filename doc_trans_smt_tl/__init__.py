from rule_based_tl import dict_tl, remove_punct, tokenize, tag
from doc_trans_tl import combine_tokens
from smt import encapsulate, ngram_var
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


def translate_smt(sen_poss_list, dict_source, vb_tl_tf_idf_list, nn_tl_tf_idf_list, jj_tl_tf_idf_list, rb_tl_tf_idf_list, cc_tl_tf_idf_list, pr_tl_tf_idf_list, dt_tl_tf_idf_list, tl_struct, il_struct, il_struct_count):
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