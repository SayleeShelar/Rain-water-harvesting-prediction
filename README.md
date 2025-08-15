
# Rainwater Harvesting Prediction Model

This repository contains a machine learning project that predicts the volume of rainwater that can be harvested. The model is trained on a synthetic dataset and deployed using a Streamlit web application.

## Project Goal

The primary objective of this project is to create a predictive model that helps users estimate the amount of rainwater they can capture based on key factors. This can be used to assess the feasibility and potential of installing a rainwater harvesting system.

## Key Features

- **Data Exploration:**  
  A Jupyter Notebook (`rainwater_harvesting.ipynb`) is used to perform a thorough exploratory data analysis (EDA) of the dataset (`rainwater_harvesting_dataset.csv`).

- **Linear Regression Model:**  
  A Linear Regression model from scikit-learn is trained to predict `Liters_Captured` based on input features.

- **Model Evaluation:**  
  The model's performance is evaluated using standard metrics such as R², Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

- **Model Persistence:**  
  The trained model is saved using `joblib` for easy re-use and deployment.

- **Interactive Web App:**  
  A Streamlit application (`app.py`) is provided for a user-friendly interface to make real-time predictions.

## Model Details

The final model uses the following features to make predictions:

- **Roof Area (m²):** The size of the roof.  
- **Average Annual Rainfall (mm):** The amount of rainfall in the area.  
- **Runoff Coefficient:** A value from 0.6 to 0.95 representing the proportion of water that runs off a surface.  
- **Tank Size (Liters):** The capacity of the water storage tank.  

## Files in this Repository

- `rainwater_harvesting.ipynb` - Jupyter Notebook containing data analysis, model training, and evaluation.  
- `rainwater_harvesting_dataset.csv` - Dataset used to train the model.  
- `app.py` - Python script for the Streamlit web application.  
- `rainwater_harvesting_model.pkl` - Trained machine learning model saved using joblib.  
- `README.md` - This file.  

## How to Run the Project

### 1. Clone the repository:

```bash
git clone https://github.com/SayleeShelar/Rain-water-harvesting-prediction.git
cd Rain-water-harvesting-prediction
````

### 2. Install dependencies:

The required libraries are `streamlit`, `pandas`, `joblib`, `numpy`, and `scikit-learn`.

```bash
pip install streamlit pandas joblib numpy scikit-learn
```

Alternatively, you can install them from a `requirements.txt` file if one is provided.

### 3. Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open automatically in your web browser. You can then enter different values for the input features and get a prediction of the captured water volume.

## Conclusion

This project demonstrates an end-to-end machine learning workflow, from data analysis and model training to deployment in an interactive web application. The Streamlit app provides a practical way for users to engage with the model and understand the factors influencing rainwater capture.

**Future Development:**
The model could be further refined by exploring more advanced algorithms or incorporating additional features such as geographic location data, which could improve predictive accuracy and utility.

```

```
