# Stockprice-Pnomaly-Detector
# Dataset Preprocessing – Steps:
Data Collection ,   
Missing Value Handling ,   
Date Parsing and Indexing ,   
Feature Selection (e.g., Close price) ,   
Reshaping and Scaling (for LSTM) ,   
Train-Test Split (for LSTM forecasting) 

# Model Selection and Rationale:
# Isolation Forest:
Best suited for unsupervised anomaly detection in financial data.
No labels required and efficient on large datasets.
Identifies abnormal spikes/dips by isolating data points.
# LSTM (Long Short-Term Memory):
Powerful for time-series forecasting.
Captures sequential dependencies in closing prices.
Helps predict future price trends and compare with actuals to detect anomalies post-prediction.

# Challenges Faced and Solutions:
While building this financial time-series anomaly detection and forecasting tool, several beginner-level challenges were faced.
One of the major difficulties was understanding how to prepare time-series data properly for different models like Isolation Forest and LSTM. It was tricky to reshape the data in the format that LSTM accepts, especially with no background in deep learning.
Another challenge was interpreting the model outputs — the LSTM predictions were coming in the form of graphs, and it wasn’t clear how to extract meaningful values like future closing prices in number form. With time and experimentation, these results were visualized better to understand the trends.
Also, deploying the app on Hugging Face was new and challenging. Facing errors like "network error", "invalid syntax", and dependency issues made deployment frustrating. These problems were solved by carefully creating a requirements.txt file and uploading only the necessary files (app.py, requirements.txt, and model-related files).
Overall, the key to solving all challenges was breaking the problem into small parts, learning each part slowly, and testing everything in Jupyter Notebook before moving to Streamlit and then deployment.

# Isolation forest anomalies visualization:
![image](https://github.com/user-attachments/assets/3e370036-ea30-466d-afde-3b92e2176a7a)

# LSTM prediction vs actual values visualization:
![image](https://github.com/user-attachments/assets/eefab38e-3ecb-4b65-b93c-ca050d1e1c3d)


