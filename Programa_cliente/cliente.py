import nltk
from nltk.tokenize import sent_tokenize
import json
import requests
def main():
    
    opcion = "";
    while opcion != "n":
        #inicio del programa que pide la ruta del archivo y la direccion del balanceador de google cloud
        print("PROGRAMA CLIENTE")
        autor = input("Nombre del autor del archivo: ")
        ruta_archivo = input("Ingrese ruta del archivo: ")
        ruta_balanceador = input("Ingrese IP del balanceador con (https): ")
        archivo = open("hello.txt", 'r')
        contenido = archivo.read()
        #iteramos la lista de oraciones para enviarlos al balanceador
        lista_contenido= sent_tokenize(contenido)
        for item in lista_contenido:
            json_publicacion ={
                "autor": autor,
                "nota" : item
            }
            publicacion=json.dumps(json_publicacion)
            newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            try:
                rq = requests.post(ruta_balanceador+'/balanceador',data=publicacion,headers=newHeaders)
                print(rq.status_code)
            except requests.exceptions.RequestException as e: 
                raise SystemExit(e)
        
            print("Nota Ingresada: " +publicacion) 
        archivo.close()
        
        opcion = input("Desea enviar otro archivo? (y/n): ")
        

    
    print("Fin del programa!!")

if __name__ == "__main__":
    main()