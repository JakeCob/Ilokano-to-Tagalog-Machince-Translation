import pandas as pd
from flask import Blueprint, render_template, request, jsonify
from module.tl_il.doc_trans_tl import doc_trans
from module.tl_il.doc_trans_smt_tl import smt_trans
from module.il_tl.doc_trans_smt_il import il_smt_trans

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == 'GET':
    
    return render_template("index.html")
# end of home()


@views.route('/il_tag', methods=['GET', 'POST'])
def il_tag():
    
    if request.method == 'POST':
        source = request.form.get('source_lang')
        dict_il_tl_result = il_smt_trans(source)
        dict_il_tl_result = pd.DataFrame(dict_il_tl_result)
        op_sen_list = dict_il_tl_result['System Output'].tolist()

    else:
        source = ''
        op_sen_list = []
    
    return render_template('il-tg_translator.html', source = source, op_sen_list = op_sen_list)
# end of function

@views.route('/tag_il', methods=['GET', 'POST'])
def tag_il():
    
    if request.method == 'POST':
        source = request.form.get('source_lang')
        dict_tl_il_result = smt_trans(source)
        dict_tl_il_result = pd.DataFrame(dict_tl_il_result)
        op_sen_list = dict_tl_il_result['System Output'].tolist()
    else:
        source = ''
        op_sen_list = []
    
    return render_template('tg-il_translator.html', source = source, op_sen_list = op_sen_list)
# end of function

@views.route('/home')
def landing_page():

    return render_template('index.html')

@views.route('/il_tag')
def standard():

    return render_template('il-tg_translator.html')

@views.route('/tag_il')
def hybrid():

    return render_template('tg-il_translator.html')