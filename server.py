from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = '3.141599876543210__CanYouKeepASecret??'

@app.route('/', methods=['GET','POST'])
def hello_work():
    try:
        intGuess = int(request.form['guess'])
        intRandom = int(session['randomNumber'])
        session['guess'] = intGuess
        # print '    Random number:' , intRandom , ' User Guess:',  int(session['guess'])

        if (intGuess == intRandom):
            session['guessResults'] = "<div class='guessBox green'>{} - Good Guess!</div>".format(intGuess)
            session['buttonName'] = 'Try Again'
        elif (intGuess < intRandom):
            session['guessResults'] = "<div class='guessBox red'>{} - Too Small!</div>".format(intGuess)
            session['buttonName'] = 'Submit'
        else:
            session['guessResults'] = "<div class='guessBox red'>{} - Too Large!</div>".format(intGuess)
            session['buttonName'] = 'Submit'

    except Exception as e:
        session['guessResults'] = "<div class='guessBox'></div>"
        session['buttonName'] = 'Submit'
        session['randomNumber'] = int(random.randrange(0,101))
    return render_template('index.html')

app.run(debug=True)
