from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted!'