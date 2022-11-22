from flask import Blueprint, render_template, request, jsonify
# import doc_trans_tl

views = Blueprint('views', __name__)

def execute():
    sysout = 'not yet connected to .py file'
    return sysout

@views.route('/')
def home():
    return render_template('index.html', sysout= execute())
