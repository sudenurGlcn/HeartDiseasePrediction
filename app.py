from flask import Flask, render_template, request
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)

# Modeli yükle
model = load_model('model_kaydiSon1.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Kullanıcıdan gelen verileri al
    user_input = {
        'BMI': float(request.form['BMI']),
        'SmokerStatus': request.form['SmokerStatus'],
        'AlcoholDrinkers': request.form['AlcoholDrinkers'],
        'HadStroke': request.form['HadStroke'],
        'PhysicalHealthDays': float(request.form['PhysicalHealthDays']),
        'MentalHealthDays': float(request.form['MentalHealthDays']),
        'DifficultyWalking': request.form['DifficultyWalking'],
        'Sex': request.form['Sex'],
        'AgeCategory': request.form['AgeCategory'],
        'HadDiabetes': request.form['HadDiabetes'],
        'PhysicalActivities': request.form['PhysicalActivities'],
        'GeneralHealth': request.form['GeneralHealth'],
        'SleepHours': float(request.form['SleepHours']),
        'HadKidneyDisease': request.form['HadKidneyDisease']
    }

    # Veriyi DataFrame'e çevir
    user_df = pd.DataFrame([user_input])

    # LabelEncoder'ı kullanarak kategorik sütunları dönüştür
    label_encoder = LabelEncoder()
    categorical_columns = ['SmokerStatus', 'AlcoholDrinkers', 'HadStroke', 'DifficultyWalking', 'Sex', 'GeneralHealth', 'AgeCategory', 'HadDiabetes', 'PhysicalActivities', 'HadKidneyDisease']

    for column in categorical_columns:
        user_df[column] = label_encoder.fit_transform(user_df[column])

    # DataFrame'i NumPy dizisine çevir ve uygun türde dönüştür
    user_input_array = user_df.astype({'BMI': 'float32', 'PhysicalHealthDays': 'float32', 'MentalHealthDays': 'float32', 'PhysicalActivities': 'float32', 'SleepHours': 'float32'}).values

    # Modeli kullanarak tahmin yap
    prediction = model.predict(user_input_array)
    risk_score = prediction[0][0]

    return render_template('result.html', risk_score=(risk_score*100))

if __name__ == '__main__':
    app.run(debug=True)
