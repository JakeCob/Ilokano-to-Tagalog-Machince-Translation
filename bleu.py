import nltk

def convert(lst):
    return (lst[0].split())

lst =  ["nanglukat a dagus malamig na a red si godo habang apaman si a nakalas sa kanilang iti paraanganda"]
hypothesis = ( convert(lst))
print(hypothesis)

lst1 = ["Nanglukat a dagus iti nakalamlamiis a red horse ni Godo apaman a nakalas-ud iti paraanganda ni Antokoy"]
reference = ( convert(lst1))
print(reference)

BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
print(BLEUscore)