from flask import Flask
from flask import render_template
from flask import request
import csv

app = Flask(__name__)
registros = []
lista = []

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/cadastro.html', methods = ['GET'])
def sec():
    return render_template('cadastro.html')

@app.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        registros.append(request.form.get('nome'))  
        registros.append(request.form.get('telefone'))  
        registros.append(request.form.get('email'))
        registros.append(request.form.get('endereco'))
        registros.append(request.form.get('cidade'))
        registros.append(request.form.get('uf'))
        registros.append(request.form.get('marca'))
        registros.append(request.form.get('modelo'))
        registros.append(request.form.get('placa'))
        registros.append(request.form.get('ano'))
        registros.append(request.form.get('foto'))
        print(registros)
        with open('cadastro.csv', 'a', newline='\n') as insere_linha:
            arquivo = csv.writer(insere_linha)
            arquivo.writerow(registros)        
            insere_linha.close()
        registros.clear()
    return render_template('confirma.html')

@app.route('/lista_cadastro', methods = ['GET', 'POST'])
def lista_cadastro():
    lista.clear()
    with open('cadastro.csv') as listagem:
        csv_reader = csv.reader(listagem, delimiter=',')
        for row in csv_reader:
            print(row)
            lista.append(row)
    return str(lista)

app.run(debug = True)