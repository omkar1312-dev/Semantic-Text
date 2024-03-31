from flask import Flask, request, render_template, jsonify
from fuzzywuzzy import fuzz

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate_similarity/", methods=['POST'])
def calculate_similarity():
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    
    # Calculate similarity score using the calculate_similarity_colab function
    similarity_score = calculate_similarity_fuzzywuzzy(text1, text2)
    
    return jsonify({"text1": text1, "text2": text2, "similarity_score": similarity_score})

# Function to calculate similarity score based on the fuzzywuzzy library
def calculate_similarity_fuzzywuzzy(text1, text2):
    similarity_score = fuzz.ratio(text1, text2) / 100
    return similarity_score

if __name__ == "__main__":
    app.run(debug=True)
