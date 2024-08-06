import tkinter as tk
import serial
import threading

# Configuration for serial port
SERIAL_PORT = '/dev/tty.usbmodem1101'  # Update this with your actual serial port
BAUD_RATE = 115200

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sensor Dashboard")
        self.geometry("400x300")
        
        self.pressure_label = tk.Label(self, text="Pressure: N/A")
        self.pressure_label.pack()
        
        self.temperature_label = tk.Label(self, text="Temperature: N/A")
        self.temperature_label.pack()
        
        self.accel_label = tk.Label(self, text="Accel: ax:N/A ay:N/A az:N/A")
        self.accel_label.pack()
        
        self.gyro_label = tk.Label(self, text="Gyro: gx:N/A gy:N/A gz:N/A")
        self.gyro_label.pack()
        
        # Start a thread to read from the serial port
        self.serial_thread = threading.Thread(target=self.read_serial)
        self.serial_thread.daemon = True
        self.serial_thread.start()

    def read_serial(self):
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            while True:
                if ser.in_waiting:
                    line = ser.readline().decode('utf-8').strip()
                    self.update_labels(line)
    
    def update_labels(self, data):
        parts = data.split(',')
        data_dict = {part.split(':')[0]: part.split(':')[1] for part in parts}
        
        # Update labels with data from the sensor
        self.pressure_label.config(text=f"Pressure: {data_dict.get('P', 'N/A')} hPa")
        self.temperature_label.config(text=f"Temperature: {data_dict.get('T', 'N/A')} C")
        self.accel_label.config(text=f"Accel: ax:{data_dict.get('ax', 'N/A')} ay:{data_dict.get('ay', 'N/A')} az:{data_dict.get('az', 'N/A')}")
        self.gyro_label.config(text=f"Gyro: gx:{data_dict.get('gx', 'N/A')} gy:{data_dict.get('gy', 'N/A')} gz:{data_dict.get('gz', 'N/A')}")
        
if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
