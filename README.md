# Gyro Pressure Dynamic SAT-1 Anomaly Detection using ML

## Project Overview

The "Gyro Pressure Dynamic SAT-1 Anomaly Detection using ML" project demonstrates the application of Machine Learning for anomaly detection in sensor data. This simulation mimics a satellite-like system using pressure and gyroscopic sensors to collect, process, and visualize data in real-time with Streamlit.

While this project does not involve an actual satellite, it utilizes sensors commonly found in satellite systems:

- **BMP280** (Pressure Sensor)
- **MPU6050** (Gyroscopic Sensor)

## Sensor Integration in Satellite Systems

### BMP280 Pressure Sensor

#### Role in Satellite Systems:
- **Altitude Measurement**: Measures atmospheric pressure to estimate altitude, crucial for determining satellite position relative to Earth or other reference points.
- **Environmental Monitoring**: Monitors internal environmental conditions within satellite compartments to ensure systems operate within safe pressure ranges.

#### Applications in Satellite Systems:
- **Altitude Control**: Accurate altitude measurements assist in maintaining the desired orbit and performing maneuvers for satellites in low Earth orbit (LEO).
- **Thermal Control Systems**: Pressure readings help regulate thermal control systems by monitoring and adjusting internal conditions.

### MPU6050 Gyroscopic Sensor

#### Role in Satellite Systems:
- **Orientation and Stabilization**: Measures angular velocity and acceleration to provide data on the satellite's orientation and movement, essential for stabilization and control.
- **Attitude Determination**: Integral to attitude determination systems, ensuring the satellite is correctly oriented for communication and observation tasks.

#### Applications in Satellite Systems:
- **Attitude Control Systems (ACS)**: Fine-tunes satellite orientation and maintains alignment with Earth or space targets.
- **Navigational Adjustments**: Allows for precise adjustments in trajectory and orientation.

## Project Components

1. **Sensor Simulation**: Mimics the BMP280 and MPU6050 sensors to collect data similar to that used in satellite systems.
2. **Real-Time Data Processing**: Uses Machine Learning algorithms to detect anomalies in the sensor data.
3. **Visualization**: Implements Streamlit to visualize the processed data and detected anomalies.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/gyro-pressure-dynamic-sat1.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- BMP280 and MPU6050 sensor documentation
- Streamlit for data visualization
- Machine Learning libraries for anomaly detection

For more details or questions, feel free to open an issue or contact the project maintainer.

