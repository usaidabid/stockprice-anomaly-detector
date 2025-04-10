import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import plotly.graph_objects as go

st.title("📈 Excel-Based Stock Anomaly Detector")
st.write("Upload an Excel file with 'Close*' column and Date as index")

# File uploader
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Read Excel with index column (Date)
        df = pd.read_excel(uploaded_file, index_col=0)
        df.index = pd.to_datetime(df.index)  # ensure index is datetime
        st.success("✅ File uploaded successfully!")

        # Preview
        st.subheader("📊 Preview of Uploaded Data")
        st.write(df.head())

        # Check for 'Close*' column
        if 'Close*' in df.columns:
            # Isolation Forest
            model = IsolationForest(contamination=0.05)
            df['Anomaly'] = model.fit_predict(df[['Close*']])
            anomalies = df[df['Anomaly'] == -1]

            # Plot
            st.subheader("📉 Stock Close* with Anomalies")
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df.index, y=df['Close*'], name='Close* Price'))
            fig.add_trace(go.Scatter(x=anomalies.index, y=anomalies['Close*'], mode='markers',
                                     marker=dict(color='red', size=10), name='Anomalies'))
            st.plotly_chart(fig)

            # Show anomaly rows
            st.subheader("📌 Detected Anomalies")
            st.write(anomalies[['Close*']])
        else:
            st.error("❌ 'Close*' column missing in Excel file.")
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
