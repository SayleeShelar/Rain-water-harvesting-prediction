Rainwater Harvesting Prediction Model
This repository contains a machine learning project that predicts the volume of rainwater that can be harvested. The model is trained on a synthetic dataset and deployed using a Streamlit web application.

Project Goal
The primary objective of this project is to create a predictive model that helps users estimate the amount of rainwater they can capture based on key factors. This can be used to assess the feasibility and potential of installing a rainwater harvesting system.

Key Features
Data Exploration: A Jupyter Notebook (rainwater harvesting.ipynb) is used to perform a thorough exploratory data analysis (EDA) of the provided dataset (rainwater_harvesting_dataset.csv).

Linear Regression Model: A Linear Regression model from scikit-learn is trained to predict the Liters_Captured based on input features.

Model Evaluation: The model's performance is evaluated using standard metrics such as R 
2
 , Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

Model Persistence: The trained model is saved using joblib for easy re-use and deployment.

Interactive Web App: A Streamlit application (app.py) is provided for a user-friendly interface to make real-time predictions.

Model Details
The final model uses the following features to make predictions:

Roof Area (m 
2
 ): The size of the roof.

Average Annual Rainfall (mm): The amount of rainfall in the area.

Runoff Coefficient: A value from 0.6 to 0.95 that represents the proportion of water that runs off a surface.

Tank Size (Liters): The capacity of the water storage tank.

Files in this Repository
rainwater harvesting.ipynb: The Jupyter Notebook containing all the steps for data analysis, model training, and evaluation.

rainwater_harvesting_dataset.csv: The dataset used to train the model, containing features and the target variable.

app.py: The Python script for the Streamlit web application.

rainwater_harvesting_model.pkl: The trained machine learning model saved using joblib.

README.md: This file.

How to Run the Project
To run this project, you will need to have Python and a few libraries installed.

Clone the repository:

git clone https://github.com/SayleeShelar/Rain-water-harvesting-prediction.git
cd Rain-water-harvesting-prediction



Install dependencies:
The required libraries are streamlit, pandas, joblib, and numpy.

pip install streamlit pandas joblib numpy scikit-learn



Alternatively, you can install them from a requirements.txt file if one is provided in the repository.

Run the Streamlit app:
To start the web application, execute the following command in your terminal:

streamlit run app.py



The app will open automatically in your web browser. You can then enter different values for the input features and get a prediction of the captured water volume.
