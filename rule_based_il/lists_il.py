from rule_based_il import dict_il

"""
Determiner Lists
"""
noun_dtmn_list = ["dagiti", "ti", "cadagiti", "kadagiti", "ni", "ken", "ni", "coma", "koma", "a", "iti"] # Noun Determiners * Tinanggal ko si ket

adv_dtmn_list = ["idi", "iti"]

prepo_dtmn_list = ["ti", "addaak", "iti"] # Preposition Determiners * Tinanggal ko muna yung adda
# added "iti" to the list (eg. nagtignay iti = ay sumasa)

adv_time_list = ['madamdama', 'ita', 'kalman', 'inton bigat', 'ditoy', 'idiay', 'ita a rabii', 'iti kaaldawantayo', 'idi rabii', 'sumaruno a lawas', 'nga', 'nabiit pay', 'nasapa', 'dagus', 'pay laeng', 'pay', 'napalabas']

adv_place_list = ['ditoy', 'sadiay', 'iti labesna', 'iti sadinoman a lugar', 'sadinoman', 'balay', 'pabuya']

adv_manner_list = ['naan-anay', 'medio', 'napartak', 'narigat', 'napartak', 'sibabannayat', 'kasla saan', 'dandani amin', 'dandani', 'awan pagpambarna', 'sangsangkamaysa', 'agmaymaysa']

adv_freq_list = ['masansan', 'kadawyan', 'maminsan', 'sagpaminsan', 'manmanon']

adj_quantity_list = []

adj_quality_list = []

adj_taste_list = []

adj_shape_list = []

adj_size_list = []

adj_color_list = []



""" 
    Affixes
"""
PREFIX_SET = [
'na', 'ag', 'ka', 'ca', 'nag', 'im', 'maipa',
'maki', 'panna', 'maka', 'naki', 'naka', 'nang', 'makapag',
'mang', 'agan', 'agay', 'pananga', 'agam', 'nagpa', 'magpa', 
'ipa', 'pag', 'pam', 'taga', 'i', 'napa', 'in', 'manang',
'ma' # a translation for 'ma'
'para', 'pang', 'panag', 'nai', 'manag', 'man', 'kina',
'nai', 'nai', 'nagpa', 'mapag' # nangi
]

Adj_Prefix =[
'ka', 
'na' # a translation for 'ma'
]

INFIX_SET = ['in'] # eg. 'in' in 'kinunana' (sinabi)
"""
infix sa tagalog ay prefix sa ilokano
sumigaw = inpukaw
"""

SUFFIX_SET = [
'to', 'nto', 'ak' 'en'
'na', 'an', 'm', 'nyo', 
'cayo', 'tayo',
'anda',
]

Adj_Suffix = [
'an'
]

ADV_SET = [
    'rin', 'din', 'ring', 'ding'
]

PREPO_SET = [
    'tengnga',
    'rabaw', 'rabao', 'baba', 'babaen', 
    'ngatuen', 'ngato', 'sirok', 'sidong',
    'sango', 'sarang', 'saklang', 'sanguanan' 'likud', 
    'ruar', 'uneg',
    'baet', 'sango', 'umuna'
    'ngudo', 'ungto', 'abay', 'igid'
]

CONJ_SET = [
    'ken', 'ket', # no  translation for word 'bali' 
    'gapu', 'ta', 'agsipud',    'laeng', 'ngem', 'nupay kasta',
    'bayat', 'uray', 
    'intono', 'no', 'ta', 'ngamin', 
    'kaso', 'gapuna', 
    'ngem', 'idi',
    'nga', 
    'ni',  'wenno', 
    'para', 'tapno', 'agraman', 
    'numpay kasta', 
    'ken', 'ket', 'kabayatanna', 'bayat', 
    'kada', 'cas'
]

PER_PRONOUN = [
    'siak', 'sika', 'isu', 'dakami', 'datayo', 'dakayo', 'kayo', 'da', 'caycayo', 'kaykayo'
    'dinak', 'diak', 'kaniak', # no translation for 'siyang' 
    'kadakami', 'kami', # -kami translation is usually connected to another word i.e., 'Maragsakankami'
    'kadakayo', 'dakayo', 'kayo', # -kayo translation is usually connected to another word i.e., 'Umaykayo'
    'ida', 'da', # -da translation is usually connected to another word i.e., 'nagtultuloyda'
    'ko', # -ko translation is usually connected to another word i.e., 'Kayatko'
    # no translation for 'sakin'
    'kukuami', 'kadatayo', 'kukuatayo', 'tayo', # -tayo translation is usually connected to another word i.e., 'Basaentayo'
    # no translation for 'kong' and 'inyong'
    'kata', 'mo', # -mo is usually connected to another word
    'cadacuada', 
    'kenkuana', 'kencuana','mi', # -mi translation is usually connected to another word i.e., 'Insuratmi'
    'yo', 'nyo' # both are usually connected to another word
    'na', # can stand alone and can be connected to another word
]

""" 
    Other Lists
"""
vowels = ['a', 'e', 'i', 'o', 'u']
