from flask import Flask, render_template, request, jsonify
#import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
import pickle


app = Flask(__name__)

modelo = pickle.load(open('modeloSVM.sav', 'rb'))

colunas = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']


@app.route('/')
def home():
    return render_template("novo.html", titulo='Titanic: Previsão de Sobrevivência usando Aprendizado de Máquina')

@app.route('/classifica/', methods=['POST'])
def classifica():
    dados=request.form
    dados_input=[float(dados[col]) for col in colunas]
    print(dados_input)
    classe = modelo.predict([dados_input])
    if classe == 0:
        classe = '<div style="display: flex; height: 100%; align-items: center; justify-content: center"><h1 style="border: solid; border-radius: 10px; padding: 50px;">Não sobreviveu ☹</h1></div>'  
    else:
        classe = '<div style="display: flex; height: 100%; align-items: center; justify-content: center"><h1 style="border: solid; border-radius: 10px; padding: 50px;>Sobreviveu ☺</h1></div>'  
    return str(classe)


app.run()

