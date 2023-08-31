# Reconocimiento de instancias nombradas

API REST que recibe una lista de oraciones en español y devuelva una lista de las entidades nombradas identificadas en cada oración.

## Instrucciones de uso
Desde la terminal de comandos seguir los siguientes pasos:


* Clonar el repositorio
		https://github.com/alexrods/ner-api.git  

* Ve al directorio del repositorio
		cd ner-api

* Crear un entorno virtual en python
		python3 -m venv venv

* Activar el entorno virtual 
		
		# Windows
		.\venv\Scripts\activate
		
		#Linux
		source venv/bin/activate

* Instalar las paqueterias necesarias para correr la aplicacion requirements.txt
		
		pip install -r requirements.txt

* Ejecutamos el archivo app.py

		python3 app.py

* Este script corre en el entorno local en el puerto 8080,

		http://localhost:8080/ner

* Ejemplo para usar el endpoint:

	curl -X POST -H "Content-Type: application/json" -d '{"oraciones":["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.", "San Francisco considera prohibir los robots de entrega en la acera."]}' http://127.0.0.1:8080/ner

* Respuesta:

{
  "resultado": [
    {
      "entidades": {
        "Apple": "ORG",
        "Reino Unido": "LOC"
      },
      "oraci\u00f3n": "Apple est\u00e1 buscando comprar una startup del Reino Unido por mil millones de d\u00f3lares."
    },
    {
      "entidades": {
        "San Francisco": "LOC"
      },
      "oraci\u00f3n": "San Francisco considera prohibir los robots de entrega en la acera."
    }
  ]
}