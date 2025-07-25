import streamlit as st
from prediction_helper import predict
import base64

# Set the page title
st.title('Health Insurance Premium Predictor ')

# Define categorical options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)


with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[1]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row2[2]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[0]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[1]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row3[2]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[0]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[1]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values (excluding Genetical Risk)
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,

    'Medical History': medical_history
}

# Prediction button
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')

# Background image functions
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def set_background(image_path):
    encoded = get_base64(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image
set_background("image.png")

