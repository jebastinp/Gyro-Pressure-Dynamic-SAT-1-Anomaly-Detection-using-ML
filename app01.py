import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import serial
import time
import joblib
import io

# Load the pre-trained Isolation Forest model
model_filename = 'isolation_forest_model.joblib'
model = joblib.load(model_filename)

# Initialize the serial port
ser = serial.Serial('/dev/tty.usbmodem1101', 115200)  # Replace with your actual port

# Initialize DataFrame to store data
columns = ['Time', 'Pressure', 'Temperature', 'Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz']
incoming_data = pd.DataFrame(columns=columns)

# Function to parse sensor data
def parse_sensor_data(data_line):
    try:
        # Split the line by comma
        parts = data_line.split(',')
        
        # Check if we have the right number of parts
        if len(parts) != len(columns):
            st.write(f"Unexpected number of values: {len(parts)}. Expected: {len(columns)}")
            return None
        
        # Parse each part, assuming the format 'key:value'
        parsed_data = [float(part.split(':')[1]) for part in parts]
        
        return parsed_data
    except Exception as e:
        st.write(f"Error parsing data: {e}")
        return None

# Function to detect anomalies in the data using the pre-trained model
def detect_anomalies(data_point):
    # Convert the data point into a DataFrame for consistency
    data_point_df = pd.DataFrame([data_point], columns=columns)
    
    # Normalize the data
    scaler = StandardScaler()
    data_normalized = scaler.fit_transform(data_point_df)
    
    # Predict anomalies using the pre-trained model
    anomaly_prediction = model.predict(data_normalized)
    anomaly_prediction = 1 if anomaly_prediction[0] == -1 else 0
    
    return anomaly_prediction

# Function to convert DataFrame to CSV
def convert_df_to_csv(df):
    """Convert DataFrame to CSV"""
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()

# Streamlit UI
st.set_page_config(page_title="Anomaly Detection Dashboard", layout="wide")
st.title("Gyro Pressure Dynamic SAT-1 Anomaly Detection using ML")

# Streamlit placeholders
data_placeholder = st.empty()
pressure_plot_placeholder = st.empty()
temperature_plot_placeholder = st.empty()
report_placeholder = st.empty()
download_placeholder = st.empty()

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            parsed_data = parse_sensor_data(line)
            if parsed_data and len(parsed_data) == len(columns):
                # Add new data to the DataFrame
                new_data = pd.DataFrame([parsed_data], columns=columns)
                new_data['Time'] = new_data['Time'] + time.time()  # Adjust the time for plotting
                
                # Detect anomalies in the new data point
                anomaly = detect_anomalies(parsed_data)
                new_data['anomaly'] = anomaly

                # Append the new data to the incoming_data DataFrame
                incoming_data = pd.concat([incoming_data, new_data], ignore_index=True)

                # Display the data with anomalies
                data_placeholder.write(incoming_data)

                # Plot Pressure vs Time with Anomalies
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(incoming_data['Time'], incoming_data['Pressure'], label='Pressure')
                ax.scatter(incoming_data['Time'][incoming_data['anomaly'] == 1], incoming_data['Pressure'][incoming_data['anomaly'] == 1], color='red', label='Anomaly')
                ax.set_xlabel('Time')
                ax.set_ylabel('Pressure')
                ax.legend()
                pressure_plot_placeholder.pyplot(fig)

                # Plot Temperature vs Time with Anomalies
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(incoming_data['Time'], incoming_data['Temperature'], label='Temperature', color='orange')
                ax.scatter(incoming_data['Time'][incoming_data['anomaly'] == 1], incoming_data['Temperature'][incoming_data['anomaly'] == 1], color='red', label='Anomaly')
                ax.set_xlabel('Time')
                ax.set_ylabel('Temperature')
                ax.legend()
                temperature_plot_placeholder.pyplot(fig)

                # Display classification report for Temperature anomaly detection
                true_labels = incoming_data['anomaly']
                if len(true_labels) > 1:  # Ensure there is enough data to create a classification report
                    report = classification_report(true_labels, true_labels, output_dict=True)
                    report_placeholder.write(report)

                    # Extract and display precision and recall
                    precision = report['1']['precision']
                    recall = report['1']['recall']
                    st.write(f"Temperature Anomaly Precision: {precision:.2f}")
                    st.write(f"Temperature Anomaly Recall: {recall:.2f}")

    except Exception as e:
        st.write(f"Error: {e}")
        continue

ser.close()

# Add download button outside the loop
csv_data = convert_df_to_csv(incoming_data)
download_placeholder.download_button(
    label="Download All Data as CSV",
    data=csv_data,
    file_name="sensor_data_full.csv",
    mime="text/csv"
)
