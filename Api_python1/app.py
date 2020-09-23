import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
import requests
from json import loads,  dumps
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h2>SERVIDOR 1</h2>"

@app.route('/balanceador',methods=['POST'])
def loadB():
    data=request.get_json()
    #info acerca de ambos servidores
    #info servidor 1
    memoria_servidor1 =requests.get('http://34.72.97.125/memoria')
    #---cpu_servidor1 = requests.get('http://34.72.97.125/cpu')
    #info servidor 2
    memoria_servidor2 =requests.get('http://34.72.97.125/memoria')
    #---cpu_servidor2 = requests.get('http://34.72.97.125/cpu')

    #colectar info servidor 1
    memoria_info_servidor1= memoria_servidor1.json()
    #--cpu_info_servidor1 = cpu_servidor1.json

    #colectar infor servidor 2
    memoria_info_servidor2= memoria_servidor2.json()
    #---cpu_info_servidor2 = cpu_servidor2.json
    
    #Porcentaje utilizacion RAM servidor 1
    porcentaje_utilizacion_servidor1 = 100-int(memoria_info_servidor1['Porcentaje Libre'])
    #Porcentaje utilizacion RAM servidor 2
    porcentaje_utilizacion_servidor2 = 100-int(memoria_info_servidor2['Porcentaje libre'])
    #Porcentaje utilizacion CPU servidor 1
    #Porcentaje utilizacion CPU servidor 2

    #Numeros de entradas BD servidor 1
    count_servidor1 =requests.get('http://34.72.97.125/count')
    countS1_info =count_servidor1.json()
    countS1 = countS1_info['cantidad']
    #Numeros de entradas BD servidor 2
    count_servidor2 =requests.get('http://34.72.97.125/count')
    countS2_info =count_servidor2.json()
    countS2 = countS2_info['cantidad']

    if(countS1 > countS2):
        print("Insertar en A")
    elif (countS1 < countS2):
        print("Insertar en B")
    elif (countS1== countS2):
        #SI EL NUMERO ES IGUAL SE TOMA LA RAM
        if(porcentaje_utilizacion_servidor1>porcentaje_utilizacion_servidor2):
            print("Insertar en A por RAM")
        elif (porcentaje_utilizacion_servidor1<porcentaje_utilizacion_servidor2):
            print("Insertar en B por RAM")
        elif (porcentaje_utilizacion_servidor1== porcentaje_utilizacion_servidor2):
            # SI LA RAM ES IGUAL SE TOMA EL CPU
            print("aqui va la comparacion de CPUS")



    #Aqui hacemos los pasos para enviar

    return "Balanceador"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=81, debug=True)
