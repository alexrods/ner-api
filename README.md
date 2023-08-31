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