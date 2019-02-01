from flask import Flask, flash, redirect, render_template, request, url_for
import MySQLdb
from flask_paginate import Pagination, get_page_parameter, get_page_args
import json
import sys
sys.path.append('./ml/')
sys.path.append('./ml/utils/')
sys.path.append('./ml/models/')
from prediction import predict

app = Flask(__name__)

app.secret_key  = "asdKJUvr9234"


def connection_db():
    app_db = MySQLdb.connect(host="************",
                            user="**********",
                            port=3306,
                            passwd="*********",
                            db="app_db")
    c = app_db.cursor()
    return c, app_db


def connection_sphinx():
    sphinx = MySQLdb.connect(host="***********",
                             user="******",
                             port=9306,
                             passwd="*************",
                             db="Index")
    c = sphinx.cursor()
    return c, sphinx



@app.route('/')
def search():
    return render_template('index.html', has_content=False)



@app.route('/questions', methods = ['POST', 'GET'])
def result():
    url_for('static', filename='style.css')
    if request.method == 'GET':
        cursor_db, app_db = connection_db()
        cursor_sphinx, sphinx = connection_sphinx()

        app_db.begin()
        sphinx.begin()

        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

        page = request.args.get(get_page_parameter(), type=int, default=1)
        dataset_type = request.args['search']
        text_input = request.args.get('q')


        if dataset_type == 'train':
            cursor_sphinx.execute("SELECT qid FROM test1 WHERE MATCH('%s') LIMIT 1000;" % (text_input))
            question_ids = cursor_sphinx.fetchall()

            if len(question_ids) == 0:
                    return render_template('index.html', has_content=False)
            format_strings = ','.join(['%s'] * len(question_ids))
            cursor_db.execute("SELECT * FROM questions_train WHERE qid IN (%s);" % format_strings, tuple(question_ids))
        else:
            cursor_sphinx.execute("SELECT qid FROM test2 WHERE MATCH('%s') LIMIT 1000;" % (text_input))
            question_ids = cursor_sphinx.fetchall()

            if len(question_ids) == 0:
                    return render_template('index.html', has_content=False)
            format_strings = ','.join(['%s'] * len(question_ids))
            cursor_db.execute("SELECT * FROM questions_test WHERE qid IN (%s);" % format_strings, tuple(question_ids))


        questions = cursor_db.fetchall()
        cursor_sphinx.close()
        cursor_db.close()
        q_for_render = questions[offset:offset+per_page]
        pagination = Pagination(page=page, per_page=per_page, offset=offset, total=len(questions), css_framework='foundation', record_name='questions', format_total=True, format_number=True)
        return render_template('index.html', has_content=True, questions=q_for_render, pagination=pagination, train=dataset_type=='train')



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/classify_tab')
def classify_tab():
    return render_template('classify.html', question="")


@app.route('/classify', methods = ['POST', 'GET'])
def classify():
    if request.method == 'POST':
        data = request.get_json(force=True)
        result = predict(data['question'], data['model'])

        if result is not None:
            return json.dumps({"result": int(result)})
        return json.dumps({"result": "None"})

    if request.method == 'GET':

        dataset_type = request.args['search']
        text_input = request.args.get('q')
        result = predict(text_input, dataset_type)
        return render_template('classify.html', result=result, question=text_input, model=dataset_type)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
