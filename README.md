# 🌫️ Air Quality Prediction System  
**Machine Learning + Streamlit Web App**

This project predicts the **Air Quality Index (AQI)** based on seven major air pollutants using a **trained Machine Learning model**.  
The system allows users to enter pollutant levels manually through a Streamlit interface and returns:

- Predicted AQI value  
- AQI Category (Good, Moderate, Poor, Very Poor, Severe)  
- Color-coded warning indicator  

---

## 📌 Features
- 🧪 **Predicts AQI** from pollutant readings  
- 📊 **Uses Decision Tree Regression model** (`air_quality_model.pkl`)  
- 🎛️ **Interactive Streamlit UI** with sliders for pollutant input  
- 🧰 **Pretrained model** ready for deployment  
- 📁 **Clean folder structure + requirements file**  
- ⚡ Real-time prediction  
- 🖥️ Works locally or can be deployed online (Streamlit Cloud/Heroku)

---

## 🧬 Machine Learning Model

The following regression models were tested during development:
- Linear Regression  
- Lasso Regression  
- Ridge Regression  
- **Decision Tree Regressor** ✔️ *(Best performer, chosen for deployment)*

**Final Model Used:** `DecisionTreeRegressor`  
**Training Dataset:** `city_day.csv` (Air pollution dataset)

The final trained model is saved as:
