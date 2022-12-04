import pandas as pd
import string
import re
from rule_based_tl import dict_tl
from rule_based_tl import lists_tl

def remove_punct(pText):
    text_nopunct = "".join([char for char in pText if char not in string.punctuation])
    
    return text_nopunct
# end of function


def tokenize(text):
    tokens = re.split('\W+', text.lower())
    
    for token in tokens:
        if token == '':
            tokens.remove(token)
    
    return tokens
# end of function


"""
    Determiner Checker Function
"""
def isDtmn(word, noun_dtmn_list, adv_dtmn_list, prepo_dtmn_list, adv_time_list):
    """
    This function checks if the specific word in the sentence is a determiner, and extracts it.
    """
    if word in (noun_dtmn_list + adv_dtmn_list + prepo_dtmn_list + adv_time_list):
        ans = True
    else:
        ans = False

    return ans
# end of function


"""
    Verb Affixer Checker Function
"""
def check_verb_affixes(word, prev2_word, prev_word, next_word, isTagged, hasVerbAffixes, PREFIX_SET, vowels, INFIX_SET, SUFFIX_SET):
    """
    This function checks if the specific word in the sentence has an affix, and extracts it.
    """
    for prefix in PREFIX_SET:
        if word.startswith(prefix) and not isTagged:
            if word.startswith("mag") or word.startswith("nag"):
                if  word[3:5] == word[5:7] and not isTagged:
                    """
                    verbs starting with "mag" or "nag" always repeat the next 4 letters of the word 
                    e.g. maglalakad, maglalaro, magbibihis | naglalakad, naglalaro, nagbibihis
                    issue: magkakampi,
                    """
                    hasVerbAffixes = True
                    isTagged = True

                if word[3] in (vowels):
                    """
                    verbs starting with "mag" and if the next letter is a vowel, the vowel is repeated 
                    e.g. magiikot, magaayos, maguusap | nagiikot, nag-aayos, nag-uusap
                    """
                    if word[3] == word[4] and not isTagged:
                        hasVerbAffixes = True
                        isTagged = True
                        
                if (word.startswith("magka") or word.startswith("nagka")) and not isTagged:
                    """
                    verbs starting with "magka" or "nagka"  
                    e.g. magkaroon, magkasama, magkasundo (usually r,s, or vowels)
                    issue: magkapatid, magkatyempo
                    """
                    hasVerbAffixes = True
                    isTagged = True
                    
            else:
                hasVerbAffixes = True
                isTagged = True
                
    for infix in INFIX_SET:
        if word.__contains__(infix) and not isTagged:
            hasVerbAffixes = True
            isTagged = True
            
    for suffix in SUFFIX_SET:
        """
        words ending with 'ang' are adverbs and after the adverbs are the nouns 
        """
        if word.endswith(suffix) and not isTagged and not word.endswith("ang") and not prev_word.endswith("ang"):
            hasVerbAffixes = True
            isTagged = True

    if len(word) >= 4:
        if word[:2] == word[2:4] and not isTagged:
            """
            if the first four characters of a word is repeated, then it is a verb
            """
            hasVerbAffixes = True
            isTagged = True
    
    return hasVerbAffixes
# end of function


"""
    Verb Checker Function
"""
def isVerb(word, prev_word, next_word, hasVerbAffixes, PREPO_SET, PER_PRONOUN, CONJ_SET, ADV_SET, noun_dtmn_list, adv_dtmn_list, prepo_dtmn_list, vowels):
    """
    This function tags if the specific word in the sentence is a verb, and extracts it.
    """
    isDone = False
    isVerb = False
    
    if word in  dict_tl.verb_dict and not isDone:
        """If word is in the verb dictionary and is not done, is a verb"""
        isVerb = True
        isDone = True
    
    if word not in (PREPO_SET + PER_PRONOUN + CONJ_SET + ADV_SET):
        if prev_word not in (noun_dtmn_list + adv_dtmn_list + prepo_dtmn_list): 
            if next_word in (noun_dtmn_list): 
                """
                if the previous word is not in the noun, adverb, and preposition determiner and 
                the next word is a noun determiner
                eg. !(sayaw ng bata)
                """
                if hasVerbAffixes:
                    """
                    if the current word has a verb affix/es, then it is a verb
                    """
                    isVerb = True
                    isDone = True
            
            if next_word in PER_PRONOUN and not isDone:
                """
                if the next word is a personal pronoun
                eg. sayaw ka
                issue: if the next word is a personal pronoun, it is not always a verb
                eg. bastos ka
                """
                isVerb = True
                isDone = True

        if prev_word == "ay" and hasVerbAffixes and not isDone:
            if next_word in ("ng", "sa", "nang", "na") or next_word is None:
                """
                if the previous word is 'ay' and the next word is 'ng' or 'sa', then it is a verb
                eg. ay naglalakad na bata | ay naglalakad
                isse: ay nanay
                """
                isVerb = True
                isDone = True
                
        if prev_word == 'na' and hasVerbAffixes and not isDone:
            """
            if the previous word is 'na' and the current word has a verb affix/es, then it is a verb
            eg. na naglakad
            issue: na mabait
            """
            if word.startswith("ma") and len(word) == 5:
                if word[4] in vowels:
                    isVerb = False
                    isAdj = True
                    isDone = True
            if word.startswith("nag"):
               isVerb = True
               isDone = True
            if word.startswith("mag"):
               isVerb = True
               isDone = True 
               
        if word[:3] in ("nag"):
                if next_word in (PER_PRONOUN, "sa", "ni", "nang"):
                    """
                    if the first three characters of a word start with "mag", then it is a verb
                    eg. nag-ayos ka
                    """
                    isVerb = True
                    isDone = True

        if not isDone:
        #if word and not isDone:
            if word[:5] in ("magpa", "nagka") or word[:4] in ("napa", "naka") or word[:3] in ("nag"):
            # if hasAffixes and not isDone:
                """
                if the first five characters of a word start with "magpa" or "nagka" of "pagkla", then it is a verb
                eg. magpapakain, nagkakasakit
                """
                isVerb = True
                isDone = True
            if word[:3] in ("mag"):
                if next_word in (PER_PRONOUN, "sa", "ni", "nang"):
                    """
                    if the first three characters of a word start with "mag", then it is a verb
                    eg. mag-ayos ka
                    """
                    isVerb = True
                    isDone = True
    
        if hasVerbAffixes and prev_word == None and not isDone:
            if next_word in PER_PRONOUN or (next_word in noun_dtmn_list and next_word not in ('ng', 'mga')):
                """
                Isinulat niya
                """
                isVerb = True
                isDone = True
                
        # The Algorithm Below is for the words that are not tagged yet
        for verb_su in dict_tl.verb_dict['Salitang-ugat']:
            """
            for every verb in the verb dictionary salitang-ugat
            """
            if word == verb_su and not isDone:
                """
                if the current word is in the verb dictionary salitang-ugat, then it is a verb
                """
                isVerb = True
                isDone = True
        
        for verb_pn in dict_tl.verb_dict['Pangnagdaan']:
            """
            for every verb in the verb dictionary Pangnagdaan
            """
            if word == verb_pn and not isDone:
                """
                if the current word is in the verb dictionary Pangnagdaan, then it is a verb
                """
                isVerb = True
                isDone = True
                
        for verb_pk in dict_tl.verb_dict['Pangkasalukuyan']:
            """
            for every verb in the verb dictionary Pangkasalukuyan
            """
            if word == verb_pk and not isDone:
                """
                if the current word is in the verb dictionary Pangkasalukuyan, then it is a verb
                """
                isVerb = True
                isDone = True
                
        for verb_ph in dict_tl.verb_dict['Panghinaharap']:
            """
            for every verb in the verb dictionary Panghinaharap
            """
            if word == verb_ph and not isDone:
                """
                if the current word is in the verb dictionary Panghinaharap, then it is a verb
                """
                isVerb = True
                isDone = True
                
        for verb_pw in dict_tl.verb_dict['Pawatas']:
            """
            for every verb in the verb dictionary Pawatas
            """
            if word == verb_pw and not isDone:
                """
                if the current word is in the verb dictionary Pawatas, then it is a verb
                """
                isVerb = True
                isDone = True
                
        for verb_kt in dict_tl.verb_dict['Katatapos']:
            """
            for every verb in the verb dictionary Katatapos
            """
            if word == verb_kt and not isDone:
                """
                if the current word is in the verb dictionary Katatapos, then it is a verb
                """
                isVerb = True
                isDone = True
            
    return isVerb
# end of function

"""
    Noun Checker Function
"""
def isNoun(word, prev_word, prev2_word, next_word, next2_word, noun_dtmn_list, PREPO_SET, CONJ_SET, adv_dtmn_list, PER_PRONOUN):
    """
    This function tags if the specific word in the sentence is a noun, and extracts it.
    """
    isDone = False
    isNoun = False
    adj_prefix = ["ika", "pinaka", "pang"]
    adj_suffix = ["ng"]

    if prev_word in (noun_dtmn_list) and word not in noun_dtmn_list and not isDone:
        """
        if the previous word is a determiner and the word is not a determiner, then it is a noun
        eg. !(ng mga)
        """
        isAdj = False
        
        if word.endswith("ng") and len(word.replace("ng", "")) > 3:
            """
            if the word ends with 'ng' and length of the word when 'ng' is removed is greater than 3, then it is an adjective
            eg. ang mabuting tao
            """
            isAdj = True
        
        if not isAdj:
            for prefix in adj_prefix:
                """
                if the word is an adjective it has an adjective prefix
                eg. ika-ayos, pinakamahusay, pangaraw-araw
                """
                if not isDone:
                    isAdj = word.startswith(prefix)
                if not isAdj and not isDone:
                    if prev_word == 'ang':
                        """
                        if the previous word is 'ang' and not an adjective, then it is a noun
                        eg. ang espiritu
                        """
                        isNoun = True
                        isDone = True
                        
                    if next_word != 'ng' and not isDone:
                        isNoun = True
                        isDone = True
                if isAdj:  
                    isDone = True
    
    if prev_word == "sa" and word not in(PREPO_SET)and not isDone:
        """
        if the previous word is "sa" and the word is not in the PREPO_SET then it is a noun
        eg. sa simbahan <- tags "simbahan"
        """
        isNoun = True
        isDone = True
        
    if prev2_word == "ay" and prev_word.endswith("ang") and word not in noun_dtmn_list and not isDone:
        """
        if the previous previous word is "ay" and the previous word is "ang" 
        and the word is not a determiner then the word is a noun
        eg. ay ang bata
        """
        isNoun = True
        isDone = True
    
    if prev_word.endswith("ng"):
        """
        if the previous word ends with "ng" and the prev word is not in noun_dtmn_list/conj_set/adv_dtm_list then it is a noun
        eg. upang magpuno sa gabi <- prevents magpuno to be tagged as noun | ikalawang araw <- tags araw
        """
        if prev_word not in (noun_dtmn_list + CONJ_SET + adv_dtmn_list) and not isDone:
            isNoun = True
            isDone = True
        
        if prev_word.startswith("ma") and prev_word.endswith("ng") and not isDone:
            if not word.endswith("ng"):
                isNoun = True
                isDone = True

    if prev_word == "na" and not isDone:
        if prev2_word.startswith("ma") or prev2_word.startswith("ika") or prev2_word ==  CONJ_SET:
            isNoun = True
            isDone = True

    if next_word == "na":
        if next2_word.startswith("na") or next2_word.startswith("ma"):
            isNoun = True
            isDone = True
    
    if prev_word == "ng" and next_word == "na":
        if next2_word.startswith("ma"): # nagpagawa siya ng gusali na mataas
            isNoun = True
            isDone = True
        else:
            isNoun = False
            isDone = True

    if prev_word.endswith("ng") and word.endswith("ng"):
            # untags "dalawang malaking" <- untags malaking
            isNoun = False
            isDone = False
            isAdj = True

    if prev_word in (noun_dtmn_list) and word.endswith("ng"): 
        # this untags words like "unang" e.g. "ang unang araw" <- untags "unang" as a noun and tags it as an adj
        isDone = True
        isNoun = False
    
    if prev_word == "sa" and next_word == "na":
        # untags adjectives placed between "sa" and "na" e.g. "sa maliit na lamesa"
        isNoun = False
        isDone = False

    if word in PER_PRONOUN:
        """
        if the word is a personal pronoun, then it is a noun
        eg. ako, ikaw, tayo, etc.
        """
        isNoun = True
        isDone = True
    
    return isNoun
# end of function


"""
    Adjective Checker Function
"""
def isAdj(word, prev_word, prev2_word, next_word, hasVerbAffixes, noun_dtmn_list, adv_dtmn_list, prepo_dtmn_list, PREPO_SET, PER_PRONOUN, CONJ_SET):
    """
    This function tags if the specific word in the sentence is an adjective, and extracts it.
    """
    isDone = False
    isAdj = False
    
    if word not in (noun_dtmn_list + adv_dtmn_list + prepo_dtmn_list + PREPO_SET + PER_PRONOUN + CONJ_SET):
        if word.startswith("ma") and (next_word in noun_dtmn_list or next_word == 'na') and next_word not in ('ay', 'ng', 'mga') and  not hasVerbAffixes and not isDone:
            """
            if the word is an adjective it has an adjective prefix 'ma' and the next word is noun determiner
            eg. maayos na ang kalsada
            """
            isAdj = True
            isDone = True
        
        if word.startswith("napaka") or word.startswith("pinakama") or word.startswith("pinaka") and not hasVerbAffixes and not isDone:
            """
            if the word starts with 'pinakama' or 'pinaka' or 'napaka', then it is an adjective
            eg. pinakamaganda, pinakagusto, napakaganda
            """
            isAdj = True
            isDone = True
        
        if word.startswith("nag") and word[3:5] == word[5:7] and word.endswith("han") and not hasVerbAffixes and not isDone:
            """
            if the word starts with 'nag' then followed by repeating syllable then ends with 'han', then it is an adjective
            eg. naglalakihan, naggagandahan
            """
            isAdj = True
            isDone = True
        
        if word.startswith("ma") and word[2:4] == word[4:6] and not hasVerbAffixes and not isDone:
            """
            if the word starts with 'ma' then followed by repeating syllable, then it is an adjective
            eg. malalaki, magaganda
            """
            isAdj = True
            isDone = True
        
        if word.startswith("an") and not hasVerbAffixes and not isDone:
            """
            if the word starts with 'an' then it is an adjective
            eg. anlaki, ansarap
            """
            isAdj = True
            isDone = True
            
        if prev_word == 'ang' and next_word == 'ng' and not hasVerbAffixes and not isDone:
            """
            if the prev word is 'ang' then the word is an adjective
            eg. ang ganda ng bulaklak
            """
            isAdj = True
            isDone = True
            
        if word.startswith("ma") and prev_word in noun_dtmn_list  and (next_word == 'na') and not hasVerbAffixes and not isDone:
            """
            if the prev word is 'ang' then the word is an adjective
            eg. naghanda ng malamig na coke
            """
            isAdj = True
            isDone = True
            
        if prev_word == 'mas' and not hasVerbAffixes and not isDone:
            """
            if the prev word is 'mas' then the word is an adjective
            eg. mas maganda
            """
            isAdj = True
            isDone = True
        
        if word.endswith("ng") and not hasVerbAffixes and not isDone:
            """
            if the word ends with 'ng', then it is an adjective
            eg. dalawang bahay
            """
            isAdj = True
            isDone = True
        
        if prev_word in ('ay', 'na') and not prev2_word.startswith('ika') and (not hasVerbAffixes or word.startswith('ma')) and not isDone:
            """
            if the previous word is 'ay' or 'na', then it is an adjective
            eg. salamin na parihaba
            """
            isAdj = True
            isDone = True
            
        if word in  lists_tl.adj_dict and not isDone:
            """If word is in the adj dictionary and is not done, is a adj"""
            isAdj = True
            isDone = True
            
        if word[:3] in ("ika") and not isDone:
            """If word starts with ika and is not done, is a adj"""
            isAdj= True
            isDone= True
            
        if word in lists_tl.adj_quantity_list and not isDone:
            """
            if the word is in the adj quantity list, then it is an adjective
       
            """
            isAdj = True
            isDone = True
            
        if word in lists_tl.adj_quality_list and not isDone:
            """
            if the word is in the adj quality list, then it is an adjective
       
            """
            isAdj = True
            isDone = True
            
        if word in lists_tl.adj_taste_list and not isDone:
            """
            if the word is in the adj taste list, then it is an adjective
       
            """
            isAdj = True
            isDone = True
            
        if word in lists_tl.adj_shape_list and not isDone:
            """
            if the word is in the adj shape list, then it is an adjective
       
            """
            isAdj = True
            isDone = True 
              
        if word in lists_tl.adj_size_list and not isDone:
            """
            if the word is in the adj size list, then it is an adjective
       
            """
            isAdj = True
            isDone = True
             
        if word in lists_tl.adj_color_list and not isDone:
            """
            if the word is in the adj color list, then it is an adjective
       
            """
            isAdj = True
            isDone = True
        
    return isAdj
# end of function


"""
    Palindrome Checker Function
"""
def isPalindrome(word): 
    """
    This function checks if the word is a palindrome.
    """
    
    """
    gets the half length of the word
    """
    half_len = len(word)/2
    half_len = int(half_len)
    
    if word[:half_len] == word[half_len:] and half_len > 2:
        return True
    else:
        return False
# end of function


"""
    Adverb Checker Function
"""
def isAdv(word, prev_word, next_word, hasVerbAffixes, PER_PRONOUN, adv_time_list, adv_freq_list, adv_place_list, adv_manner_list):
    """
    This function tags if the specific word in the sentence is an adverb, and extracts it.
    """
    isDone = False
    isAdv = False

    if word.startswith('ma') and not word.startswith('mag') and (next_word in PER_PRONOUN or next_word == 'na') and next_word not in ('ay', 'ng', 'mga') and not isDone:
        """
        if the word is an adverb it has an adverb prefix 'ma' and the next word is a pronoun
        eg. mabilis na magsulat
        """
        isAdv = True
        isDone = True
    
    if prev_word == 'nang' and not isDone:
    # if prev_word == 'nang' and (not hasVerbAffixes or (word.startswith('ma') and not word.startswith('mag'))) and next_word not in ('ay', 'ng', 'mga') and not isDone:
        """
        if the previous word is 'nang'
        """
        if next_word not in ('ay', 'ng', 'mga'):
            """
            if the next word is not "ay, ng, or mga"
            """
            if not hasVerbAffixes: 
                """
                if word not have verb affixes, then it is an adverb
                eg. nang husto
                """
                isAdv = True
                isDone = True
                
            if word.startswith('ma') and not isNoun and not isDone:
                """
                if starts with 'ma', then it is an adverb
                eg. nang mabilis
                """
                isAdv = True
                isDone = True
            
        # if next_word == 'ay' and not isDone: 
        #    """
        #    """   
        #     if word.startswith('pa') and not isDone:
        #         """
        #         if ends with 'pa', then it is an adverb
        #         eg. nang pasimula ay
        #         """
        #         isAdv = True
        #         isDone = True
        
    if word in adv_time_list and not isDone:
        """
        if the word is an adverb of time, then it is an adverb
        eg. aalis bukas
        """
        isAdv = True
        isDone = True
        
    if word in adv_freq_list and not isDone:
        """
        if the word is an adverb of frequency, then it is an adverb
        
        """
        isAdv = True
        isDone = True
        
    if word in adv_place_list and not isDone:
        """
        if the word is an adverb of place, then it is an adverb
        
        """
        isAdv = True
        isDone = True    
        
    if word in adv_manner_list and not isDone:
        """
        if the word is an adverb of manner, then it is an adverb
        
        """
        isAdv = True
        isDone = True
        
    if next_word == 'na' and not hasVerbAffixes and not isDone:
        """
        if the next word is 'na' then the word is an adverb
        eg. tunay na maganda
        """
        isAdv = True
        isDone = True
    
    if prev_word.startswith('ma') and not prev_word.startswith('mag') and (hasVerbAffixes or word.startswith('mag')) and not isDone:
        """
        if the previous word is an adverb the word is a verb
        eg. mabagal magpalit
        """
        isAdv = True
        isDone = True
        
    if isPalindrome(word) and not isDone:
        """
        if the word is a palindrome then it is an adverb
        eg. dahandahan (dahan-dahan) siya
        """
        isAdv = True
        isDone = True
    
    if word.__contains__('ng') and not isDone:
        """
        if the word contains 'ng' then it is an adverb
        """
        
        temp_word = word.replace('ng', '')
        
        if isPalindrome(temp_word):
            """
            if the temporary word is a palindrome then it is an adverb
            eg. sobrangsobra (sobrang-sobra) siya
            """
            isAdv = True
            isDone = True
                       
    return isAdv
# end of function


"""
    Preposition Checker Function
"""
def isPrepo(word, prev_word, prepo_dtmn_list, PREPO_SET):
    """
    This function checks if the specific word in the sentence is a preposition, and extracts it.
    """
    isPrepo = False
    
    if prev_word in (prepo_dtmn_list) and word in (PREPO_SET):
        isPrepo = True
        
    return isPrepo
# end of function


"""
    Conjunction Checker Function
"""

def isConj(word, CONJ_SET):
    """
    This function checks if the specific word in the sentence is a conjunction
    """
    if word in CONJ_SET:
        return True
    else:
        return False
# end of function


def tag(sentence_list):
    isTagged = None
    hasVerbAffixes = None
    pos_sen_list = []
    """
    instantiations of the variables
    """

    for sentence in sentence_list:
        pos_list = []
        prev_word = ""
        prev2_word = ""
        sen_len = len(sentence)
        """
        instantiations of the variables
        """
        
        for word in sentence:
            
            isTagged = False
            hasVerbAffixes = False
            """
            instantiations of the variables
            """
            
            try:
                next_word = sentence[sentence.index(word) + 1]
            except (ValueError, IndexError):
                next_word = ""
            """
            gets the next word in the sentence
            """
            
            try:
                next2_word = sentence[sentence.index(word) + 2]
            except (ValueError, IndexError):
                next2_word = ""
            """
            gets the next word in the sentence
            """
                
            try:
                hasVerbAffixes = check_verb_affixes(word, prev2_word, prev_word, next_word, isTagged, hasVerbAffixes, lists_tl.PREFIX_SET, lists_tl.vowels, lists_tl.INFIX_SET, lists_tl.SUFFIX_SET)
            except (ValueError, IndexError):
                hasVerbAffixes = False
            """
            checks if the word has verb affixes
            """
            
            if sen_len == 1:
                """
                if the sentence is only one word long
                """
                pos_list.append('SW')
                isTagged = True

            elif isDtmn(word, lists_tl.noun_dtmn_list, lists_tl.adv_dtmn_list, lists_tl.prepo_dtmn_list, lists_tl.adv_time_list) and not isTagged:
                """
                checks if the word is a determiner
                """
                pos_list.append('DT')
                isTagged = True
                
            elif isConj(word, lists_tl.CONJ_SET) and not isTagged:
                """
                checks if the word is a conjunction and not tagged
                """
                pos_list.append('CC')
                isTagged = True
                
            elif isVerb(word, prev_word, next_word, hasVerbAffixes, lists_tl.PREPO_SET, lists_tl.PER_PRONOUN, lists_tl.CONJ_SET, lists_tl.ADV_SET, lists_tl.noun_dtmn_list, lists_tl.adv_dtmn_list, lists_tl.prepo_dtmn_list, lists_tl.vowels) and not isTagged:
                """
                checks if the word is a verb and not tagged
                """
                pos_list.append('VB')
                isTagged = True

            elif isNoun(word, prev_word, prev2_word, next_word, next2_word, lists_tl.noun_dtmn_list, lists_tl.PREPO_SET, lists_tl.CONJ_SET, lists_tl.adv_dtmn_list, lists_tl.PER_PRONOUN) and not isTagged:
                """
                checks if the word is a noun and not tagged
                """
                pos_list.append('NN')
                isTagged = True
            
            elif isAdj(word, prev_word, prev2_word, next_word, hasVerbAffixes, lists_tl.noun_dtmn_list, lists_tl.adv_dtmn_list, lists_tl.prepo_dtmn_list, lists_tl.PREPO_SET, lists_tl.PER_PRONOUN, lists_tl.CONJ_SET) and not isTagged:
                """
                checks if the word is an adjective and not tagged
                """
                pos_list.append('JJ')
                isTagged = True
               
            elif isAdv(word, prev_word, next_word, hasVerbAffixes, lists_tl.PER_PRONOUN, lists_tl.adv_time_list, lists_tl.adv_freq_list, lists_tl.adv_place_list, lists_tl.adv_manner_list) and not isTagged:
                """
                checks if the word is an adverb and not tagged
                """
                pos_list.append('RB')
                isTagged = True
                
            elif isPrepo(word, prev_word, lists_tl.prepo_dtmn_list, lists_tl.PREPO_SET) and not isTagged:
                """
                checks if the word is a preposition and not tagged
                """
                pos_list.append('PR')
                isTagged = True
                        
            else:
                """
                if the word is not tagged, then it is an unknown word
                """
                pos_list.append('UNK')
                isTagged = True
            
            prev_word = word
            """
            getting the previous word
            """
            
            try:
                prev2_word = sentence[sentence.index(word) - 1]
            except (ValueError, IndexError):
                prev2_word = None
            """
            getting the previous after the previous word
            """
            
        pos_sen_list.append(pos_list)
        """
        storing the words in the list to the list of sentences
        """
        
    return pos_sen_list
# end of function

