from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

species = {
    0: {
        "name": "Iris Setosa",
        "id": "setosa",
        "description": "Known for its distinctive purplish-blue petals with white and bright yellow signals. It is native to the subarctic regions, thriving in damp meadows and wetlands."
    },
    1: {
        "name": "Iris Versicolor",
        "id": "versicolor",
        "description": "Commonly called the blue flag, it features magnificent blue-violet blossoms with deep purple veins and yellow patches. It is native to eastern North America."
    },
    2: {
        "name": "Iris Virginica",
        "id": "virginica",
        "description": "Also known as the Virginia iris, this elegant species displays soft violet to deep blue petals. It is native to coastal marshes and wet soils in the eastern United States."
    }
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    features = np.array([[sepal_length,
                          sepal_width,
                          petal_length,
                          petal_width]])

    prediction = model.predict(features)[0]

    result = species[prediction]

    return render_template('index.html', 
                           prediction_text=result['name'],
                           prediction_id=result['id'],
                           prediction_description=result['description'])


if __name__ == '__main__':
    app.run(debug=True)