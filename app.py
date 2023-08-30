from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

nlp = spacy.load("es_core_news_sm")

@app.route('/', methods=['POST'])
def entity_recognize():
      try:
        data = request.get_json()
        text = data.get('text', '')

        # Procesa el texto con el modelo de SpaCy
        doc = nlp(text)

        # Extrae las entidades nombradas y sus etiquetas
        entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]

        return jsonify(entities)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
  
