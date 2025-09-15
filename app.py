import streamlit as st #type:ignore
import numpy as np
import joblib

model = joblib.load('./model/model.pkl')

st.title("Insurance Charge Predictor")

age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ['male', 'female'])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.slider("Number of Children", 0, 5, 1)
smoker = st.selectbox("Smoker", ['yes', 'no'])
region = st.selectbox("Region", ['southeast', 'southwest', 'northeast', 'northwest'])




sex_encoded = 1 if sex == 'male' else 0
smoker_encoded = 1 if smoker == 'yes' else 0
region_map = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}
region_encoded = region_map[region]

input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])


if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Insurance Charge: ${prediction:,.2f}")
