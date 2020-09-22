import nltk
from nltk.tokenize import sent_tokenize
import json
import requests
def main():
    
    opcion = "";
    while opcion != "n":
        #inicio del programa que pide la ruta del archivo y la direccion del balanceador de google cloud
        print("PROGRAMA CLIENTE")
        ruta_archivo = input("Ingrese ruta del archivo: ")
        ruta_balanceador = input(f"Ingrese direccion del balanceador: ")
        archivo = open("hello.txt", 'r')
        contenido = archivo.read()
        #iteramos la lista de oraciones para enviarlos al balanceador
        lista_contenido= sent_tokenize(contenido)
        for item in lista_contenido:
            json_publicacion ={
                "autor": "Gary",
                "nota" : item
            }
            publicacion=json.dumps(json_publicacion)
            try:
                rq = requests.post(ruta_balanceador,data=publicacion)
                print(rq)
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                raise SystemExit(e)
        
            print(publicacion) 
        archivo.close()
        
        opcion = input("Desea enviar otro archivo? (y/n): ")
        

    
    print("Fin del programa!!")

if __name__ == "__main__":
    main()