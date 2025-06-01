# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model and vectorizer (assuming they're saved together)
model = None
cv = None

def load_model():
    global model, cv
    # Load your model and vectorizer here
    # Assuming you've saved them together or separately
    model = joblib.load('./model/final_model.sav')
    cv = joblib.load('./model/count_vectorizer.pkl') 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        # Transform and predict
        transformed_text = cv.transform([text])
        prediction = model.predict(transformed_text)[0]
        
        category = "political news" if prediction == 0 else "sport news"
        
        return jsonify({
            'category': category,
            'prediction': int(prediction)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=5000, debug=True)