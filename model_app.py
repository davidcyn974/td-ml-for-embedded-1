"""3. Create a model_app.py file and import streamlit and joblib

4. In model_app.py, using the joblib library, load the model from the "regression.joblib "file

5. Using the st.number_input function, create three form fields for size, number of bedrooms and whether a house has a garden

6. Retrieve the information and pass it to the model via the predict function. Display the result in the streamlit

Use st.write to display the prediction result"""

import streamlit as st
import joblib

model = joblib.load("regression.joblib")

def main():
    st.title("House Price Prediction App")
    size = st.number_input("Size")
    nb_rooms = st.number_input("Number of rooms")
    garden = st.number_input("Garden")
    if st.button("Predict"):
        result = model.predict([[size, nb_rooms, garden]])[0]
        st.write(f"The predicted price is {result}")

if __name__ == "__main__":
    main()