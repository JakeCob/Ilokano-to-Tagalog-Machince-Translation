#Bilingual Evaluation Understudy (BLEU) score functions
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

#takes in reference string and candidate string
def bleuScore(ref, cand):
    ref.split()
    cand.split()
    cc = SmoothingFunction() #smoothing is used for short sentences or sentences without 3/4-grams
    return sentence_bleu([ref], cand, smoothing_function=cc.method4)#sentenece_blue() requires sentences to be tokenized list


#takes in two reference strings and a candidate string
def bleuScore2Ref(ref,ref2, cand):
    ref.split()
    ref2.split()
    cand.split()
    cc = SmoothingFunction() #smoothing is used for short sentences or sentences without 3/4-grams
    return sentence_bleu([ref, ref2], cand, smoothing_function=cc.method4)#sentenece_blue() requires sentences to be tokenized list

df=open("bleu_scores.txt","w", encoding="utf-8")

with open("ref.txt") as ref_file, open("cand.txt") as hyp_file: # manually saved the translation to a txt file
   line = ref_file.readline()

   while line:
    line1 = ref_file.readline()
    ref = line1

    line2 = hyp_file.readline()
    hyp = line2

    score = bleuScore(ref , hyp)

    if score == 0:
        exit()

    else:
        print("Reference: ", ref)
        print("Machine Translation: ", hyp)
        print("BLEU Score: ", score)

        df.write('Reference: ' + ref)
        df.write('Machine Translation: ' + hyp)
        df.write('BLEU Score: ' + str(score))
        df.write('\n\n')

df.close()
ref_file.close()