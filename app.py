from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the ML API!'})

@app.route('/predict')
def predict():
    # Placeholder for ML model prediction
    return jsonify({'prediction': 'This is where the ML model output will go'})

if __name__ == '__main__':
    app.run(debug=True)
