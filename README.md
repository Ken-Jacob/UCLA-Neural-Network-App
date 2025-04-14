# 🎓 UCLA Admission Predictor

A machine learning project using a Neural Network to predict a student’s chance of admission to UCLA based on their GRE, TOEFL, CGPA, SOP, LOR, and Research experience. The project is built with Streamlit for interactive visualization and deployed using Streamlit Cloud.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Ken-Jacob/UCLA-Neural-Network-App.git
cd Neural-Network-Solution
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🧠 Model Info

- Algorithm: `MLPRegressor (Neural Network)`
- Preprocessing: `StandardScaler`, train-test split
- Features:
  - GRE Score
  - TOEFL Score
  - University Rating
  - SOP
  - LOR
  - CGPA
  - Research
- Target: Admit Chance (0 to 1)

---

## ☁️ Deployment
**You can deploy this app on https://ken-jacob-ucla-neural-network-app-app-ybvcgs.streamlit.app/
**---

## 🧑‍💻 Author

**Ken Biju Jacob**  
Business Intelligence System Infrastructure  
Algonquin College 
