import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict( final_features )

    if prediction==1:
        pred='Loan Approved!!'
    else:
        pred="Sorry! We cant approve your Loan"
    output = pred

    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
