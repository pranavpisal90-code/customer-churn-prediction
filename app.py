from flask import render_template,request
from flask import Flask
import pandas as pd
import joblib
model=joblib.load('best_rf.pkl')
scaler = joblib.load('scaler.pkl')

from sqlalchemy import create_engine
engine=create_engine('sqlite:///churn.db',echo=False)
import datetime



app=Flask(__name__)
@app.route('/predict',methods=["POST"])
def predict():
    input_data= {
    'gender': 1,
    'SeniorCitizen': 0,
    'Partner': 0,
    'Dependents': 0,
    'tenure': float(request.form['tenure']),
'PhoneService': 0,
'PaperlessBilling': 1,
'MonthlyCharges': float(request.form['monthlyCharges']),
'TotalCharges': float(request.form['TotalCharges']),
'MultipleLines_No phone service': 0,
'MultipleLines_Yes': 0,
'InternetService_Fiber optic': 0,
'InternetService_No': 0,
'OnlineSecurity_No internet service': 0,
'OnlineSecurity_Yes': 0,
'OnlineBackup_No internet service': 0,
'OnlineBackup_Yes': 0,
'DeviceProtection_No internet service': 0,
'DeviceProtection_Yes': 0,
'TechSupport_No internet service': 0,
'TechSupport_Yes': 0,
'StreamingTV_No internet service': 0,
'StreamingTV_Yes': 0,
'StreamingMovies_No internet service': 0,
'StreamingMovies_Yes': 0,
'Contract_One year': 0,
'Contract_Two year': 0,
'PaymentMethod_Credit card (automatic)': 0,
'PaymentMethod_Electronic check': 0,
'PaymentMethod_Mailed check': 0,
    
    
    
    

    }
    contract = request.form['Contract']
    input_data['Contract_One year'] = 1 if contract == 'One year' else 0
    input_data['Contract_Two year'] = 1 if contract == 'Two year' else 0

    internet = request.form['InternetService']
    input_data['InternetService_Fiber optic'] = 1 if internet == 'Fiber optic' else 0
    input_data['InternetService_No'] = 1 if internet == 'No' else 0


    input_df=pd.DataFrame([input_data])
    input_df[['tenure', 'MonthlyCharges', 'TotalCharges']] = scaler.transform(input_df[['tenure', 'MonthlyCharges', 'TotalCharges']])
    prediction = model.predict(input_df)[0]  # inside function
    
    if prediction == 1:
        result = "This customer is likely to CHURN"
    else:
        result = "This customer is likely to STAY"
    log = {
    'tenure': float(request.form['tenure']),
    'MonthlyCharges': float(request.form['monthlyCharges']),
    'TotalCharges': float(request.form['TotalCharges']),
    'Contract': request.form['Contract'],
    'InternetService': request.form['InternetService'],
    'prediction': result,
    'timestamp': datetime.datetime.now()
}
    x_df=pd.DataFrame([log])
    x_df.to_sql('predictions_log', con=engine, if_exists='append', index=False)
   
    print(input_df[['tenure', 'MonthlyCharges', 'TotalCharges']].values)

    return render_template('result.html', result=result) 
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
