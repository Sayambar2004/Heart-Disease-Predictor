import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('LRM.pkl', 'rb'))

# Define the prediction function
def predict_heart_disease(age, sex, chest_pain_type, resting_bp, cholestoral, fasting_blood_sugar,
                          restecg, max_hr, exang, oldpeak, slope, num_major_vessels, thal):
    input_data = np.array([age, sex, chest_pain_type, resting_bp, cholestoral, fasting_blood_sugar,
                           restecg, max_hr, exang, oldpeak, slope, num_major_vessels, thal]).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.set_page_config(page_title="Heart Disease Predictor", page_icon="🫀", layout="wide")

# Sidebar
st.sidebar.header("Heart Disease Predictor")
st.sidebar.write("""
This application uses a Logistic Regression model to predict the likelihood of heart disease based on various health parameters. 
Please provide the following information:
""")

# Main content
st.title("Heart Disease Predictor")
st.markdown("""
## Predict Your Heart Disease Risk
Enter your health details in the sidebar and click **Predict** to see the result.
""")

# Input fields
st.sidebar.subheader("Patient Information")
age = st.sidebar.number_input('Age', min_value=1, max_value=120, value=25)
sex = st.sidebar.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
chest_pain_type = st.sidebar.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, value=0)
resting_bp = st.sidebar.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=200, value=120)
cholestoral = st.sidebar.number_input('Cholesterol (mg/dL)', min_value=100, max_value=600, value=200)
fasting_blood_sugar = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dL', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
restecg = st.sidebar.number_input('Resting Electrocardiographic Results (0-2)', min_value=0, max_value=2, value=0)
max_hr = st.sidebar.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.sidebar.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
oldpeak = st.sidebar.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=1.0)
slope = st.sidebar.number_input('Slope of the Peak Exercise ST Segment (0-2)', min_value=0, max_value=2, value=1)
num_major_vessels = st.sidebar.number_input('Number of Major Vessels (0-3) Colored by Flourosopy', min_value=0, max_value=3, value=0)
thal = st.sidebar.number_input('Thalassemia (0=Normal; 1=Fixed Defect; 2=Reversable Defect)', min_value=0, max_value=2, value=1)

# Prediction
if st.sidebar.button('Predict'):
    result = predict_heart_disease(age, sex, chest_pain_type, resting_bp, cholestoral, fasting_blood_sugar,
                                   restecg, max_hr, exang, oldpeak, slope, num_major_vessels, thal)
    st.subheader("Prediction Result")
    if result == 1:
        st.error('The model predicts that you have heart disease.')
    else:
        st.success('The model predicts that you do not have heart disease.')

# About section
st.markdown("""
---
### About This App
This heart disease prediction app leverages machine learning to analyze various health metrics and predict the likelihood of heart disease. The model was trained on a dataset from Kaggle and uses Logistic Regression for prediction. The model has an accuracy of 0.82 on untrained data and 0.86 on trained data.
""")

# Footer
st.markdown("""
---
### Creator
Sayambar Roy Chowdhury

2nd year Undergraduate Student, Heritage Institute of Technology, Kolkata.

GitHub: [Sayambar2004](https://github.com/Sayambar2004)
""")
