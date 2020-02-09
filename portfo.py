from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return 'form submitted!'
    database = open("database.txt", "a")
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        database.write(str(data))
        database.close()
        return 'form submitted!'
    else:
        return "something went wrong, try again!"



# export FLASK_ENV=development
# export FLASK_DEBUG=1
# export FLASK_APP=portfo.py
# flask run