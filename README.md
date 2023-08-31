# Reconocimiento de instancias nombradas

API REST que recibe una lista de oraciones en español y devuelva una lista de las entidades nombradas identificadas en cada oración.

## Instrucciones de uso
* Crear un entorno virtual en python
		python3 -m venv venv

* Clonar el repositorio
        	https://github.com/alexrods/ner-api.git 

* Activar el entorno virtual 
		
		# Windows
		.\venv\Scripts\activate
		
		#Linux
		source venv/bin/activate

* Instalar las paqueterias necesarias para correr la aplicacion requirements.txt
		
		pip install -r requirements.txt

* Ejecutamos el archivo app.py

		python app.py

* Este script corre en el entorno local en el puerto 8080,

		http://localhost:8080/ner
