# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/verifica', methods=['POST'])
def verifica():
    testo = request.form['testo']
    if testo.isalpha():
        return "✅ Hai inserito solo lettere!"
    else:
        return "⚠️ Inserimento non valido: ci sono numeri o simboli!"

if __name__ == "__main__":
    app.run(debug=True)
