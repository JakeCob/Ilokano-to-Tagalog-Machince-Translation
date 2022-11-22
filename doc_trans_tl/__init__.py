from rule_based_tl import dict_tl, remove_punct, tokenize, tag
import pandas as pd


def combine_tokens(sen_translation_list):
    temp_sen_list = []

    for sen_translation in sen_translation_list:
        temp_sen = ''
        for word_translation in sen_translation:
            temp_index = sen_translation.index(word_translation)
            if temp_index == len(sen_translation) - 1:
                temp_sen += word_translation
            else:
                temp_sen += word_translation + ' '
        temp_sen_list.append(temp_sen)
    
    return temp_sen_list
# end of function


def translate(sen_poss_list, dict_source):
    sp_index = 0 # sentence POS index
    sen_translation_list = []
    
    for sen_poss in sen_poss_list:
        # loop for getting the pos structure of every sentence
        """
        sen_poss is a list of POS of a sentence
        eg. ['VB', 'DT', 'NN', 'DT', 'NN']
        """
        sen_translation = []
        
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
                    isNone = False
                    if dict_tl.sw_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.sw_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
            
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
                    isNone = False
                    if dict_tl.vb_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.vb_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
                    
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
                    isNone = False
                    if dict_tl.nn_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.nn_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
                                
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
                    isNone = False
                    if dict_tl.jj_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.jj_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
                            
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
                    isNone = False
                    if dict_tl.rb_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.rb_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
                    
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
                    isNone = False
                    if dict_tl.cc_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.cc_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
                            
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
                    if dict_tl.pr_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.pr_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
                    
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
                    if dict_tl.dt_il_list[temp_index][0] == 'None':
                        sen_translation.append(word)
                    else:
                        sen_translation.append(dict_tl.dt_il_list[temp_index][0])
                else:
                    sen_translation.append(word)
                    
            else:
                sen_translation.append(word)
            
            wp_index += 1
        sp_index += 1
        sen_translation_list.append(sen_translation)
    
    return sen_translation_list
# end of function


def doc_trans(source, expected_op):
    parsed_source = source.split("\r\n")
    cleaned_source = [remove_punct(word) for word in parsed_source]
    toklenized_source = [tokenize(word) for word in cleaned_source]
    dict_source = pd.DataFrame({'Tokenized': toklenized_source}) 
    pos_sen_list = tag(dict_source['Tokenized'])
    
    dict_source['POS'] = pos_sen_list
    sen_translation_list = translate(dict_source['POS'], dict_source)
    temp_sen_list = combine_tokens(sen_translation_list)
    
    # Dictionary of the system output and the expected output and their scores
    dict_op_ex = pd.DataFrame({'System Output': temp_sen_list})
    
    parsed_expected_op = expected_op.split("\r\n")
    cleaned_expected_op = [remove_punct(word) for word in parsed_expected_op]
    toklenized_expected_op = [tokenize(word) for word in cleaned_expected_op]
    combine_tokens_expected_op = combine_tokens(toklenized_expected_op)
    dict_op_ex['Target Output'] = combine_tokens_expected_op
    
    return dict_op_ex
# end of function
