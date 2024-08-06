import tkinter as tk
import serial
import threading

# Serial port configuration
SERIAL_PORT = '/dev/tty.usbmodem1101'  # Replace with your actual serial port
BAUD_RATE = 115200

# Set up the serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# Create the GUI
class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sensor Dashboard")
        self.geometry("400x300")

        # Create labels
        self.pressure_label = tk.Label(self, text="Pressure: ", font=("Helvetica", 12))
        self.pressure_label.pack(pady=10)

        self.temperature_label = tk.Label(self, text="Temperature: ", font=("Helvetica", 12))
        self.temperature_label.pack(pady=10)

        self.accel_label = tk.Label(self, text="Accel: ", font=("Helvetica", 12))
        self.accel_label.pack(pady=10)

        self.gyro_label = tk.Label(self, text="Gyro: ", font=("Helvetica", 12))
        self.gyro_label.pack(pady=10)

        # Start data reading thread
        self.data_thread = threading.Thread(target=self.read_data)
        self.data_thread.daemon = True
        self.data_thread.start()

    def read_data(self):
        while True:
            try:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        # Parse the data
                        data = {item.split(':')[0]: item.split(':')[1] for item in line.split(',')}
                        self.update_labels(data)
            except serial.SerialException as e:
                print(f"Error reading from serial port: {e}")
                break
    def update_labels(self, pressure, temperature, ax, ay, az, gx, gy, gz):
        self.pressure_label.config(text=f"Pressure: {pressure:.2f} hPa")
        self.temperature_label.config(text=f"Temperature: {temperature:.2f} C")
        self.accel_label.config(text=f"Accel: ax:{ax:.2f} ay:{ay:.2f} az:{az:.2f}")
        self.gyro_label.config(text=f"Gyro: gx:{gx:.2f} gy:{gy:.2f} gz:{gz:.2f}")




    '''def update_labels(self, data):
        self.pressure_label.config(text=f"Pressure: {data.get('P', 'N/A')} hPa")
        self.temperature_label.config(text=f"Temperature: {data.get('T', 'N/A')} C")
        self.accel_label.config(text=f"Accel: ax:{data.get('ax', 'N/A')} ay:{data.get('ay', 'N/A')} az:{data.get('az', 'N/A')}")
        self.gyro_label.config(text=f"Gyro: gx:{data.get('gx', 'N/A')} gy:{data.get('gy', 'N/A')} gz:{data.get('gz', 'N/A')}")'''

# Run the GUI
if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
