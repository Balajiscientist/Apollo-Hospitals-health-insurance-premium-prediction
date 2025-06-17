# Apollo Health Insurance Premium Prediction Project

This project is an Apollo Health Insurance Premium Prediction system that provides a user-friendly. Streamlit frontend and uses machine learning models to estimate health insurance premiums based on user input and medical history. This project was developed at the Centre for Digital Health and Precision Medicine (CDHPM) during an internship.


## Project Structure

- **main.py/**: Contains the Streamlit application code.   
- **prediction_helper.py/**:: Contains preprocessing, scaling, and prediction helper functions.
- **artifacts/**: Contains pre-trained models and scalers (model_young.joblib, model_rest.joblib, scaler_young.joblib, scaler_rest.joblib).
- **requirements.txt/**: Lists the required Python packages.
- **image.png/**: Background image used in the Streamlit app.
- **README.md/**: Provides an overview and setup instructions for the project.
## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Balajiscientist/Apollo-Hospitals-health-insurance-premium-prediction.git
   cd Apollo-Hospitals-health-insurance-premium-prediction
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```

1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run main.py
   ```
