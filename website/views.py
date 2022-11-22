from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)

temp_sen_list = ['sentence 1', 'sentence 2', 'sentence 3']
temp_bleu_score = 0.5
temp_ter_score = 0.7


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        source_lang = request.form.get('source_lang')
        expected_op = request.form.get('expected_op')
        print(source_lang, expected_op)
    
    return render_template('index.html')


@views.route('/results')
def results():
    return render_template('results.html', temp_sen_list = temp_sen_list, temp_bleu_score = temp_bleu_score, temp_ter_score = temp_ter_score)

