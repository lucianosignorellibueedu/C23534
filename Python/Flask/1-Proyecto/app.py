from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

#Programa principal
if __name__ == "__main__":
    app.run(debug=True, port=5500)