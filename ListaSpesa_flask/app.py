from flask import Flask, render_template

#inizializza l'app Flask
app = Flask(__name__)

listaSpesa=["mamma"]

#rotta principale
@app.route('/')
def home():
    return render_template('index.html')

def home():
    return "Per ora funziona tutto"

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)