from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

try:
    nlp = spacy.load("es_core_news_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "es_core_news_sm"])
    nlp = spacy.load("es_core_news_sm")

@app.route('/ner', methods=['POST'])
def entity_recognize():
    try:
        data = request.get_json()

        if "oraciones" not in data:
            return jsonify({'error': 'La clave oraciones no se encuentra en los datos de entrada'}), 400
        
        texts = data.get('oraciones', [])

        results = []
        for text in texts:
            # Procesa el texto con el modelo de SpaCy
            doc = nlp(text)
            # Extrae las entidades nombradas y sus etiquetas
            entities = {f'{ent.text}': ent.label_ for ent in doc.ents}
            sentence_result = {
                'oración': text,
                'entidades': entities
            }

            results.append(sentence_result)

        return jsonify({'resultado': results})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
  
