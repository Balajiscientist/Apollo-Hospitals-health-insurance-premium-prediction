#  Apollo Health Insurance Premium Prediction

This project is an Apollo Health Insurance Premium Prediction system that provides a user-friendly Streamlit frontend and uses machine learning models to estimate health insurance premiums based on user input and medical history. This project was developed at the Centre for Digital Health and Precision Medicine (CDHPM) during an internship.

# Objectives

- ✅ Achieved **>97% prediction accuracy** on test data.
- 🎯 Maintained a **<10% error margin** in over 95% of predictions.
- ☁️ Deployed on cloud with an easy-to-use **Streamlit** interface.
- 👩‍⚕️ Designed for **insurance underwriters** to estimate premiums interactively based on applicant details.

# App Result

![Apollo App Screenshot](https://github.com/Balajiscientist/Apollo-Hospitals-health-insurance-premium-prediction/blob/8149b2d7dea402e5ff4a7c0c16a0b444b272e836/conclusion)


## Project Structure

- **main.py**: Contains the Streamlit application code.   
- **prediction_helper.py**:: Contains preprocessing, scaling, and prediction helper functions.
- **artifacts**: Contains pre-trained models and scalers (model_young.joblib, model_rest.joblib, scaler_young.joblib, scaler_rest.joblib).
- **requirements.txt**: Lists the required Python packages.
- **image.png**: Background image used in the Streamlit app.
- **README.md**: Provides an overview and setup instructions for the project.

# Delivered

- Collected a labeled dataset of 50,000 records with 14 features from a third-party vendor.
- Performed data cleaning, handled missing values, and removed outliers to improve data quality.
- Conducted exploratory data analysis (EDA) to identify key patterns and correlations.
- Engineered new features, including a normalized risk score based on medical history.
- Encoded categorical variables and scaled numerical features for model readiness.
- Trained and evaluated multiple machine learning models to predict insurance premiums.
- Performed error analysis to understand prediction errors and refine model performance.
- Tuned hyperparameters to achieve high model accuracy and minimize prediction error.
- Selected and packaged the best-performing model for deployment.
- Built a user-friendly Streamlit application to allow real-time premium predictions.
- Documented the project, including setup instructions, usage guidelines, and model details.


## 📘 Documentation

For more detailed information about the system architecture and design, please refer to the [LLD Document](LLD.pdf).

# Conclusion
This project offers a user-friendly tool for predicting health insurance premiums based on user details and medical history. It aims to assist users in estimating costs and supports personalized insurance planning.


# 👨‍💻 Author & Internship Info
## 👤 Author: B. Balaji
- 🏢 Internship Organization: Centre for Digital Health and Precision Medicine (CDHPM)
- 🗓️ Duration: Summer 2025
- 💻 Domain: Machine Learning 
- 📧 Contact: balajiscientist@gmail.com
