## Heart Disease Predictor

This repository contains a machine learning model to predict the likelihood of heart disease based on various health parameters. The model is built using Logistic Regression and deployed using Streamlit.

## Overview

The Heart Disease Predictor application leverages machine learning to analyze various health metrics and predict the likelihood of heart disease. Users can input their health data, and the model will provide a prediction.

## Features

- **Input Parameters:** Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, Fasting Blood Sugar, Resting Electrocardiographic Results, Maximum Heart Rate Achieved, Exercise Induced Angina, ST Depression Induced by Exercise Relative to Rest, Slope of the Peak Exercise ST Segment, Number of Major Vessels Colored by Flourosopy, Thalassemia.
- **Model:** Logistic Regression.
- **Deployment:** Streamlit web application.

## Dataset

The dataset used to train the model is from Kaggle. It contains the following columns:

- `age`: Age of the patient
- `sex`: Sex of the patient (0 = Female, 1 = Male)
- `chest_pain_type`: Type of chest pain (0-3)
- `resting_bp`: Resting blood pressure (mm Hg)
- `cholestoral`: Cholesterol level (mg/dL)
- `fasting_blood_sugar`: Fasting blood sugar > 120 mg/dL (0 = No, 1 = Yes)
- `restecg`: Resting electrocardiographic results (0-2)
- `max_hr`: Maximum heart rate achieved
- `exang`: Exercise induced angina (0 = No, 1 = Yes)
- `oldpeak`: ST depression induced by exercise relative to rest
- `slope`: Slope of the peak exercise ST segment (0-2)
- `num_major_vessels`: Number of major vessels colored by flourosopy (0-3)
- `thal`: Thalassemia (0 = Normal, 1 = Fixed defect, 2 = Reversable defect)
- `target`: Diagnosis of heart disease (0 = No, 1 = Yes)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sayambar2004/Heart-Disease-Predictor.git
cd Heart-Disease-Predictor
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to the project directory:

```bash
cd Heart-Disease-Predictor
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Open your web browser and go to http://localhost:8501 to access the Heart Disease Predictor application.


## Model

The model was trained using a Logistic Regression algorithm and saved as a pickle file (LRM.pkl). The model's input features include various health metrics that are used to predict the likelihood of heart disease.

## Web Application

The web application is built using Streamlit, providing an interactive interface for users to input their health data and receive predictions.

## Creator

Sayambar Roy Chowdhury  
2nd year Undergraduate Student, Heritage Institute of Technology, Kolkata.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

The dataset used for training the model is from Kaggle.  
Special thanks to the open-source community for providing the tools and resources used in this project.
