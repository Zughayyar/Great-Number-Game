from flask import Flask, render_template, session, request, redirect
from random import randrange

app = Flask(__name__)  
app.secret_key = "keep it safe"


@app.route('/')
def main():
    session['guessed_number'] = None
    if session['random_num'] is None:
        session['random_num'] = randrange(1,100,1)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():    
    session['guessed_number'] = int(request.form['guess'])
    return render_template("index.html")

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session['random_num'] = None
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    