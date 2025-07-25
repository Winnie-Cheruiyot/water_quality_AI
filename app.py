import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Water Quality AI", layout="wide")
st.title("💧 AI Water Quality Checker")
st.markdown("Predict whether drinking water is **safe or unsafe** using chemical test results.")

# Tabs: Manual | CSV Upload | Info
tab1, tab2, tab3 = st.tabs(["🔎 Manual Input", "📂 Upload CSV", "📊 Threshold Charts"])

# --- Tab 1: Manual Input ---
with tab1:
    st.sidebar.header("Manual Input")

    def user_input_features():
        ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0)
        hardness = st.sidebar.slider("Hardness (mg/L)", 0.0, 500.0, 150.0)
        solids = st.sidebar.slider("Solids (ppm)", 500.0, 50000.0, 10000.0)
        chloramines = st.sidebar.slider("Chloramines (mg/L)", 0.0, 15.0, 6.0)
        sulfate = st.sidebar.slider("Sulfate (mg/L)", 100.0, 500.0, 250.0)
        conductivity = st.sidebar.slider("Conductivity (μS/cm)", 100.0, 1000.0, 400.0)
        organic_carbon = st.sidebar.slider("Organic Carbon (mg/L)", 0.0, 30.0, 10.0)
        trihalomethanes = st.sidebar.slider("Trihalomethanes (µg/L)", 0.0, 120.0, 60.0)
        turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 4.0)

        data = {
            "ph": ph,
            "Hardness": hardness,
            "Solids": solids,
            "Chloramines": chloramines,
            "Sulfate": sulfate,
            "Conductivity": conductivity,
            "Organic_carbon": organic_carbon,
            "Trihalomethanes": trihalomethanes,
            "Turbidity": turbidity
        }
        return pd.DataFrame([data])

    input_df = user_input_features()

    st.write("### Sample Input")
    st.write(input_df)

    if st.button("🔍 Predict Potability"):
        result = model.predict(input_df)[0]
        prediction = "✅ Safe to Drink" if result == 1 else "❌ Unsafe to Drink"
        st.success(f"**Prediction:** {prediction}")

# --- Tab 2: Bulk Prediction via CSV ---
with tab2:
    st.subheader("📂 Upload CSV File")
    uploaded_file = st.file_uploader("Upload CSV with water features", type=["csv"])

    if uploaded_file:
        df_uploaded = pd.read_csv(uploaded_file)
        st.write("📋 Preview of Uploaded Data")
        st.dataframe(df_uploaded.head())

        # Predict
        try:
            predictions = model.predict(df_uploaded)
            df_uploaded["Prediction"] = ["Safe" if pred == 1 else "Unsafe" for pred in predictions]
            st.success("✅ Predictions completed.")
            st.dataframe(df_uploaded)

            # Download link
            csv = df_uploaded.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Results", data=csv, file_name="predicted_water_quality.csv", mime="text/csv")
        except Exception as e:
            st.error("Check your CSV format. It must match model input features.")

# --- Tab 3: Threshold Charts & Info ---
with tab3:
    st.subheader("📊 Water Quality Guidelines")
    thresholds = {
        "pH": (6.5, 8.5),
        "Hardness (mg/L)": (60, 180),
        "Solids (ppm)": (0, 500),
        "Chloramines (mg/L)": (0, 4),
        "Sulfate (mg/L)": (0, 250),
        "Conductivity (μS/cm)": (50, 500),
        "Organic Carbon (mg/L)": (0, 10),
        "Trihalomethanes (µg/L)": (0, 80),
        "Turbidity (NTU)": (0, 5)
    }

    for feature, (low, high) in thresholds.items():
        st.write(f"**{feature}**: Acceptable range is **{low} to {high}**")
        fig, ax = plt.subplots()
        ax.axvspan(low, high, color='green', alpha=0.3, label="Safe Range")
        ax.axvline(low, color='orange', linestyle='--')
        ax.axvline(high, color='orange', linestyle='--')
        ax.set_title(f"{feature} Threshold Range")
        ax.set_xlabel(feature)
        ax.set_yticks([])
        st.pyplot(fig)
