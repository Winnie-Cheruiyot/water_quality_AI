# 💧 Water Quality Monitoring AI System

A Streamlit-based AI dashboard for analyzing, predicting, and visualizing water quality across multiple boreholes in Turkana and other arid regions.

## 🌍 Problem Statement

Millions of people rely on borehole water without knowing if it's safe to drink. Manual testing is slow, costly, and inconsistent. This tool empowers communities and organizations to:

- Upload water quality test data (CSV)
- Get instant potability predictions using AI
- View trends, contaminants, and borehole health over time
- Export water reports and monitor location-based data

## 🚀 Features

✅ CSV upload for water test results  
✅ AI-based prediction using RandomForest  
✅ Borehole management (name, location, readings)  
✅ Role-based login (Admin/User)  
✅ Visualizations: Line charts, bar graphs, and heatmaps  
✅ Export water reports to PDF  
✅ Map view for borehole distribution  
✅ IoT-ready for future real-time sensor integration

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, Pandas, scikit-learn
- **Model:** RandomForestClassifier
- **Data:** `water_potability.csv`
- **Auth:** Simple login system (expandable)
- **Optional:** Hugging Face / Render deployment

## 📦 Installation

```bash
## Clone the repo
git clone https://github.com/Winnie-Cheruiyot/water_quality_AI.git
cd water_quality_AI

## (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## ▶️ Run the App
streamlit run app.py

## 🧪 Sample Data Columns
- pH

- Hardness

- Solids

- Chloramines

- Sulfate

- Conductivity

- Organic_carbon

- Trihalomethanes

- Turbidity

- Potability (target: 0 = not safe, 1 = safe)

## 📈 Model Info

- Algorithm: RandomForestClassifier

- Training Accuracy: ~98%

- Input: 9 water quality indicators

- Output: Binary prediction (Potable / Not Potable)

## 👩‍💻 Future Improvements
- Real-time IoT data streaming

- SMS alerts and automated reporting

- User role management and analytics dashboard

- Geo-location map view (Leaflet/Folium)
## 🏆 Credits
Created by Winnie Cheruiyot for AI for Good / SDG 6 project:
"Safe Water for Turkana using AI"

## 🌐 License
- MIT License
