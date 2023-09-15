import time
import serial
from wifi import Cell
import requests
import json

serial_port = '/dev/ttyACM0'
baud_rate = 9600
arduino_serial = serial.Serial(serial_port, baud_rate)
known_ssids=['Moto Edge 40','Vivo1901','POCOM3']

def main():
    while True:
        try:
            flag = 0
            data = arduino_serial.readline().decode('utf-8').strip()
            print(data)
            gas, imu = eval(data)[0], eval(data)[1]
            gas_value, accel, gyro, mag = gas[0], imu[0], imu[1], imu[2]
            if gas_value >= 100:
                flag =  1
            # store_imu_data(accel, gyro, mag)
            # store_wif_signal_strength()
            cells = list(Cell.all("wlan0"))
            cells.sort(key=lambda x: x.signal, reverse=True)

            wifi_data = [{'ssid': cell.ssid, 'mac_address': cell.address, 'signal_strength': cell.signal} for cell in cells]
            print(wifi_data)
            mac1,mac2,mac3=0,0,0
            for data in wifi_data:
                if data['ssid'] == 'Moto Edge 40':
                    mac1=data['signal_strength']
                if data['ssid'] == 'Vivo1901':
                    mac2=data['signal_strength']
                if data['ssid'] == 'POCOM3':
                    mac3=data['signal_strength']
            payload={
                'ax': accel[0],
                'ay': accel[1],
                'az': accel[2],
                'gx': gyro[0],
                'gy': gyro[1],
                'gz': gyro[2],
                'mx': mag[0],
                'my': mag[1],
                'mz': mag[2],
                'mac1':mac1,
                'mac2':mac2,
                'mac3':mac3,
                'gas': flag
            }
            url = "https://edp-backend-jfu8.onrender.com/sensor-reading" # replace with your API endpoint URL



            headers = {
                "Content-Type": "application/json"
            }

            response = requests.post(url, data=json.dumps(payload), headers=headers)

            if response.status_code == 200:
                print("Data sent successfully.")
            else:
                print(f"Failed to send data. Error code: {response.status_code}")
            time.sleep(3)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()