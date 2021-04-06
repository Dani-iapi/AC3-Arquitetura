from flask import Flask, render_template, request, flash, redirect, url_for, session, abort
from calcula import Calcular

app = Flask(__name__)
app.secret_key = 'AC3 Arquitetura'


def realiza_calculo(valor1, valor2, operacao):
    if operacao == 'soma':
        return Calcular().calculaSoma(valor1, valor2)  
    elif operacao == 'subtracao':
        return Calcular().calculaSubtracao(valor1, valor2)  
    elif operacao == 'multiplicacao':
        return Calcular().calculaMultiplicacao(valor1, valor2)  
    elif operacao == 'raiz':
        return Calcular().calculaRaiz(valor1, valor2)
    elif operacao == 'potenciacao':
        return Calcular().calculaPotencia(valor1, valor2)

@app.route('/')
def calcula():
    return render_template('Index.html')

@app.route('/exibe', methods=['POST',])
def exibe_resultado():
    
    valor1 = int(request.form['valor1'])
    valor2 = int(request.form['valor2'])
    operacao = str(request.form['operacoes'])
    
    if operacao == 'divisao':
        if valor2 != 0:
            resultado = Calcular().calculaDivisao(valor1, valor2)
            flash('O resultado da ' + operacao + ' entre os valores ' + str(valor1) + ' e ' + str(valor2) + ' é igual a ' + str(resultado))
            return redirect(url_for('calcula'))              
        else:
            flash('Não existe divisão por 0')
            return abort (422)
    else:
        resultado = realiza_calculo(valor1, valor2, operacao)
        flash('O resultado da ' + operacao + ' entre os valores ' + str(valor1) + ' e ' + str(valor2) + ' é igual a ' + str(resultado))
        return redirect(url_for('calcula'))


app.run(debug=True)