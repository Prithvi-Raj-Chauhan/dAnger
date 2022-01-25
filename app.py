from flask import render_template, request, Flask
import json

DATABASE = json.load(open('db.json'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dAnger():
    if request.method == 'POST':
        msg = request.form['msg']
        DATABASE.append(msg)
        json.dump(DATABASE, open('db.json', "w"))
    return render_template('index.html', db=DATABASE)

if __name__ == "__main__":
    app.run()