import pandas as pd

# Verb Dictionary
verb_dict = pd.read_json('src/json data/Tagalog to Ilokano/verb_dict.json')

# Adjective Dictionary
adj_dict = pd.read_json('src/json data/Tagalog to Ilokano/adj_dict.json')

# Tagalog to Ilokano Language Model Dictionary
dict_tl_il_lm = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/Language Model/dict_tl_il_lang_mod.json')

""""
    Tagalog to Ilokano Dictionaries
"""

# Single Words Dictionary
dict_sw = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_sw.json')
dict_vb = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_vb.json')
dict_nn = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_nn.json')
dict_jj = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_jj.json')
dict_rb = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_rb.json')
dict_cc = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_cc.json')
dict_pr = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_pr.json')
dict_dt = pd.read_json('src/json data/Tagalog to Ilokano/Example-Based/dict_dt.json')

"""
    Putting the columns in a list
"""
sw_tl_list = dict_sw['Tagalog Single Words'].tolist()
sw_il_list = dict_sw['Ilokano Single Words'].tolist()
vb_tl_list = dict_vb['Tagalog Verb'].tolist()
vb_il_list = dict_vb['Ilokano Verb'].tolist()
nn_tl_list = dict_nn['Tagalog Noun'].tolist()
nn_il_list = dict_nn['Ilokano Noun'].tolist()
jj_tl_list = dict_jj['Tagalog Adjective'].tolist()
jj_il_list = dict_jj['Ilokano Adjective'].tolist()
rb_tl_list = dict_rb['Tagalog Adverb'].tolist()
rb_il_list = dict_rb['Ilokano Adverb'].tolist()
cc_tl_list = dict_cc['Tagalog Conjunction'].tolist()
cc_il_list = dict_cc['Ilokano Conjunction'].tolist()
pr_tl_list = dict_pr['Tagalog Preposition'].tolist()
pr_il_list = dict_pr['Ilokano Preposition'].tolist()
dt_tl_list = dict_dt['Tagalog Determiner'].tolist()
dt_il_list = dict_dt['Ilokano Determiner'].tolist()


"""
    TF-IDF
"""
vb_tfidf_tl_list = dict_vb['Tagalog Verb TF-IDF'].tolist()
vb_tfidf_il_list = dict_vb['Ilokano Verb TF-IDF'].tolist()
nn_tfidf_tl_list = dict_nn['Tagalog Noun TF-IDF'].tolist()
nn_tfidf_il_list = dict_nn['Ilokano Noun TF-IDF'].tolist()
jj_tfidf_tl_list = dict_jj['Tagalog Adjective TF-IDF'].tolist()
jj_tfidf_il_list = dict_jj['Ilokano Adjective TF-IDF'].tolist()
rb_tfidf_tl_list = dict_rb['Tagalog Adverb TF-IDF'].tolist()
rb_tfidf_il_list = dict_rb['Ilokano Adverb TF-IDF'].tolist()
cc_tfidf_tl_list = dict_cc['Tagalog Conjunction TF-IDF'].tolist()
cc_tfidf_il_list = dict_cc['Ilokano Conjunction TF-IDF'].tolist()
pr_tfidf_tl_list = dict_pr['Tagalog Preposition TF-IDF'].tolist()
pr_tfidf_il_list = dict_pr['Ilokano Preposition TF-IDF'].tolist()
dt_tfidf_tl_list = dict_dt['Tagalog Determiner TF-IDF'].tolist()
dt_tfidf_il_list = dict_dt['Ilokano Determiner TF-IDF'].tolist()

"""
    TF-IDF
"""
vb_tl_tf_idf_list = dict_vb['Tagalog Verb TF-IDF'].tolist()
nn_tl_tf_idf_list = dict_nn['Tagalog Noun TF-IDF'].tolist()
jj_tl_tf_idf_list = dict_jj['Tagalog Adjective TF-IDF'].tolist()
rb_tl_tf_idf_list = dict_rb['Tagalog Adverb TF-IDF'].tolist()
cc_tl_tf_idf_list = dict_cc['Tagalog Conjunction TF-IDF'].tolist()
pr_tl_tf_idf_list = dict_pr['Tagalog Preposition TF-IDF'].tolist()
dt_tl_tf_idf_list = dict_dt['Tagalog Determiner TF-IDF'].tolist()


"""
    Tagalog to Ilokano Language Model Dictionary
"""
tl_struct = dict_tl_il_lm['Tagalog Structure'].tolist()
il_struct = dict_tl_il_lm['Ilokano Structure'].tolist()
il_struct_count = dict_tl_il_lm['Ilokano Structure Count'].tolist()
