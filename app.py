from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        serie = request.form['serie']
        notaA = float(request.form['notaA'])
        notaB = float(request.form['notaB'])

        mediafinal = (notaA + notaB) / 2
        resultado = "aprovado" if mediafinal >= 7.0 else "reprovado"
        
        return render_template('index.html', media=mediafinal, resultado=resultado, nome=nome, serie=serie)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 