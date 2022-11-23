import pandas as pd
from flask import Blueprint, render_template, request, jsonify
from doc_trans_tl import doc_trans
from scoring import scoring_bleu

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        source = request.form.get('source_lang')
        expected_op= request.form.get('expected_op')
        dict_tl_il_result = doc_trans(source, expected_op)
        dict_tl_il_result = pd.DataFrame(dict_tl_il_result)
        op_sen_list = dict_tl_il_result['System Output'].tolist()
        ave_bleu = scoring_bleu(dict_tl_il_result)
        temp_ter_score = 0
    else:
        source = ''
        expected_op = ''
        op_sen_list = []
        ave_bleu = 0
        temp_ter_score = 0
    
    return render_template('index.html', source = source , expected_op = expected_op, op_sen_list = op_sen_list, ave_bleu = ave_bleu, temp_ter_score = temp_ter_score)
# end of function