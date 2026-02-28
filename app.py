from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "App is running"

@app.route('/compound-interest', methods=['GET', 'POST'])
def compound_interest():
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.form.get('principal', 0))
            rate = float(request.form.get('rate', 0)) / 100
            years = float(request.form.get('years', 0))
            result = principal * (1 + rate) ** years
        except:
            result = "Invalid input"

    return render_template('compound_interest.html', result=result)
