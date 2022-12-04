"""
Determiner Lists
"""
noun_dtmn_list = ["ang", "ng", "mga", "si", "ay", "ni", "sa", "y"] # Noun Determiners

adv_dtmn_list = ["nang"]

prepo_dtmn_list = ["sa", "nasa", "sumasa"]

adv_time_list = ['mamaya', 'ngayon', 'kahapon', 'bukas', 'pagkatapos', 'ngayong gabi', 'sa ngayon', 'kagabi', 'itong umaga', 'susunod na linggo', 'na', 'kamakailan lamang', 'kani-kanina lamang', 'maaga', 'kaagad', 'pa rin', 'pa', 'nakaraan']

adv_place_list = ['dito', 'doon', 'sa dako roon', 'sa lahat ng dako', 'kahit saan', 'wala kahit saan', 'tahanan', 'malayo', 'palabas']

adv_manner_list = ['tunay', 'lubos', 'medyo', 'mabilis', 'mabuti', 'mahirap', 'dahan-dahan', 'parang hindi', 'bahagya', 'halos lahat', 'halos', 'walang pasubali', 'sama-sama', 'nag-iisa']

adv_freq_list = ['lagi', 'madalas', 'karaniwan', 'kung minsan', 'paminsan-minsan', 'bihira', 'madalang', 'hindi kailanman'] 

adj_quantity_list = ['isang', 'kaunti', 'marami', 'maraming','ilan', 'i-ilan', 'ilang' ,'magkano', 'bahagi', 'buo']

adj_quality_list = ['masama', 'malinis', 'madilim', 'mahirap', 'marumi', 'tuyo', 'madali', 'walang laman', 'mahal', 'mabilis', 'dayuhan', 'puno', 'mabuti', 'mahirap', 'mabigat', 'mura', 'liwanag', 'lokal', 'bago', 'maingay', 'luma', 'malakas', 'tahimik', 'tama', 'mabagal', 'malambot', 'tunay', 'mahina', 'basa', 'mali', 'maling', 'bata']

adj_taste_list = ['mapait', 'sariwa', 'maalat', 'maasim', 'maanghang', 'matamis']

adj_shape_list = ['pabilog', 'tuwid', 'parisukat', 'tryanggulo']

adj_size_list = ['mahaba', 'malalim', 'makitid', 'maliit', 'matangkad', 'makapal', 'manipis', 'malawak', 'malalaking']

adj_color_list = ['itim', 'asul', 'kayumanggi', 'kulay-abo', 'berde', 'kahel', 'lila', 'pula','puti', 'dilaw']



""" 
    Affixes
"""
PREFIX_SET = [
    'nakikipag', 'pakikipag',
    'pinakama', 'pagpapa',
    'pinagka', 'panganga',
    'makapag', 'nakapag',
    'tagapag', 'makipag',
    'nakipag', 'tigapag',
    'pakiki', 'magpa',
    'napaka', 'pinaka',
    'ipinag', 'pagka',
    'pinag', 'mapag',
    'mapa', 'taga',
    'ipag', 'tiga',
    'pala', 'pina',
    'pang', 'naka',
    'nang', 'mang',
    'sing', 'ma', # 'ma' is a prefix in Tagalog for Adjectives, Adverbs, and Verbs
    'ipa', 'pam',
    'pan', 'pag',
    'tag', 'mai',
    'mag', 'nam',
    'nag', 'man',
    'may', 
    'na', 'ni',
    'pa', 'ka',
    'um', 'in',
    'i', 'nagpa', 
    'magka', 'nagka',
    'ini'    
]

Adj_Prefix = [
    'ma'
]

INFIX_SET = [
    'um', 'in',
]

SUFFIX_SET = [
    'syon','dor',
    'ita', 'han',
    'hin', 'ing',
    'ang', 'ng',
    'an', 'in',
    'g',
]

PREPO_SET = [
    'gitna',            #removed "sumasa", transferred to prepo_dtmn_list since it is often placed before prepositions
    'ibabaw', 'ilalim',
    'itaas', 'ibaba', 
    'baba', 'taas',
    'harap', 'likod', 
    'labas', 'loob',
    'pagitan', 'unahan', 
    'dulo', 'tabi', 'yan'
]

CONJ_SET = [
    'at', 'bali', 
    'dahil', 'datapwat', 
    'habang', 'kahit', 
    'kapag', 'kasi', 
    'kaso', 'kaya', 
    'kaysa', 'nang',
    'na', 'ngunit', 
    'ni',  'o', 
    'para', 'pati', 
    'pero', 'porket', 
    'saka', 'samantala', 
    'subalit', 'tsaka', 
    'tuwing', 'upang',
    'imbes' 
]

ADV_SET = [
    'rin', 'din', 'ring', 'ding'
]

PER_PRONOUN = [
    'ako', 'ikaw', 'siya', 'kami', 'kayo', 'sila',
    'akong', 'siyang', 'kaming', 'kayong', 'silang'
    'ko', 'akin', 'sakin', 'amin', 'atin', 'inyo',
    'kong', 'inyong', 'ating', 'saking', 'aming', 'aking',
    'kata', 'mo', 'kanila', 'kanya', 'namin', 'natin',
    'katang', 'mong', 'kanilang', 'kanyang', 'kaniyang',
    'ninyo', 'niya', 'kayoy', 'ikay', 'akoy', 'siyay', 'kamiy',
    'ninyong', 'niyang', 'mare', 'pare', 'kumpare', 'kumare'
    'silay', 'inyoy', 'kanilay', 'kanyay', 'niyay',
    'tayo', 'ka'
]



""" 
    Other Lists
"""
vowels = ['a', 'e', 'i', 'o', 'u']
