import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
import requests
from json import loads,  dumps
app = Flask(__name__)
#Rutas de los dos servidores
Servidor1_url='http://10.128.0.2'
Servidor2_url='http://10.128.0.15'
newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
@app.route('/')
def hello():
    return "<h2>SERVIDOR 1</h2>"

@app.route('/balanceador',methods=['POST'])
def loadB():
    data=request.get_json()
    #print(data,flush=True)
#info acerca de ambos servidores
    #info servidor 1
    memoria_servidor1 =requests.get(Servidor1_url+'/memoria')
    cpu_servidor1 = requests.get(Servidor1_url+'/cpu')
    #info servidor 2
    memoria_servidor2 =requests.get(Servidor2_url+'/memoria')
    cpu_servidor2 = requests.get(Servidor2_url+'/cpu')

#colectar info servidor 1
    memoria_info_servidor1= memoria_servidor1.json()
    cpu_info_servidor1 = cpu_servidor1.json()
    cpu_usage_servidor1 = 100*((cpu_info_servidor1['CPU']['total time']/cpu_info_servidor1['CPU']['HZ'])/cpu_info_servidor1['CPU']['seconds '])
    #print(cpu_usage_servidor1, flush=True)

#colectar infor servidor 2
    memoria_info_servidor2= memoria_servidor2.json()
    cpu_info_servidor2 = cpu_servidor2.json()
    cpu_usage_servidor2 = 100*((cpu_info_servidor2['CPU']['total time']/cpu_info_servidor2['CPU']['HZ'])/cpu_info_servidor2['CPU']['seconds '])
    #print(cpu_usage_servidor2, flush=True)
    
#Porcentaje utilizacion RAM servidor 1
    porcentaje_utilizacion_servidor1 = 100-int(memoria_info_servidor1['Porcentaje Libre'])
    #print(porcentaje_utilizacion_servidor1, flush=True)
#Porcentaje utilizacion RAM servidor 2
    porcentaje_utilizacion_servidor2 = 100-int(memoria_info_servidor2['Porcentaje Libre'])
    #print(porcentaje_utilizacion_servidor1, flush=True)
    #Porcentaje utilizacion CPU servidor 1
    #Porcentaje utilizacion CPU servidor 2

#Numeros de entradas BD servidor 1
    count_servidor1 =requests.get(Servidor1_url+'/count')
    countS1_info =count_servidor1.json()
    countS1 = countS1_info['cantidad']
    #print(countS1, flush=True)
#Numeros de entradas BD servidor 2
    count_servidor2 =requests.get(Servidor2_url+'/count')
    countS2_info =count_servidor2.json()
    countS2 = countS2_info['cantidad']
    #print(countS2   , flush=True)
   
    if(countS1 > countS2):
        print("Insertar en B POR COUNT")
        
        try:
            rq = requests.post(Servidor2_url+'/new',data=dumps(data),headers=newHeaders)
            print(rq.status_code)
        except requests.exceptions.RequestException as e: 
                raise SystemExit(e)
    elif (countS1 < countS2):
        print("Insertar en A POR COUNT")
        try:
            rq = requests.post(Servidor1_url+'/new',data=dumps(data),headers=newHeaders)
            print(rq.status_code, flush=True)
        except requests.exceptions.RequestException as e: 
                raise SystemExit(e)
    elif (countS1== countS2):
#SI EL NUMERO ES IGUAL SE TOMA LA RAM
        if(porcentaje_utilizacion_servidor1>porcentaje_utilizacion_servidor2):
         
            print("Insertar en B por RAM")
            try:
                rq = requests.post(Servidor2_url+'/new',data=dumps(data),headers=newHeaders)
                #print(rq.status_code)
            except requests.exceptions.RequestException as e: 
                raise SystemExit(e)
        elif (porcentaje_utilizacion_servidor1<porcentaje_utilizacion_servidor2):
            print("Insertar en A por RAM")
            try:
                rq = requests.post(Servidor1_url+'/new',data=dumps(data),headers=newHeaders)
                #print(rq.status_code)
            except requests.exceptions.RequestException as e: 
                raise SystemExit(e)
        elif (porcentaje_utilizacion_servidor1== porcentaje_utilizacion_servidor2):
# SI LA RAM ES IGUAL SE TOMA EL CPU
            if(cpu_usage_servidor1>cpu_usage_servidor2):
         
                print("Insertar en B por CPU")
                try:
                    rq = requests.post(Servidor2_url+'/new',data=dumps(data),headers=newHeaders)
                    print(rq.status_code)
                except requests.exceptions.RequestException as e: 
                    raise SystemExit(e)
            elif (cpu_usage_servidor1<cpu_usage_servidor2):
                print("Insertar en A por CPU")
                try:
                    rq = requests.post(Servidor1_url+'/new',data=dumps(data),headers=newHeaders)
                    #print(rq.status_code)
                except requests.exceptions.RequestException as e: 
                    raise SystemExit(e)
            elif (cpu_usage_servidor1== cpu_usage_servidor2):
# SI LOS CPU SON IGUAL SE MANDA A SERVIDOR A
                print("INSERCION SERVIDOR A")
                try:
                    rq = requests.post(Servidor1_url+'/new',data=dumps(data),headers=newHeaders)
                    #print(rq.status_code)
                except requests.exceptions.RequestException as e: 
                    raise SystemExit(e)                 



    #Aqui hacemos los pasos para enviar

    return "Balanceador"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
