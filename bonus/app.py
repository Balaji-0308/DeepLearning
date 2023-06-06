import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the request form
    assessed_value = float(request.form['assessed_value'])
    list_year_code = int(request.form['list_year_code'])
    sales_ratio = float(request.form['sales_ratio'])
    sale_amount = float(request.form['sale_amount'])

    # Make the prediction
    input_data = [[assessed_value, list_year_code, sales_ratio, sale_amount]]
    prediction = model.predict(input_data)[0]

    # Return the prediction result
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run()
