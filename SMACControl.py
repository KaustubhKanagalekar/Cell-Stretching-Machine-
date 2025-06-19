import pyserial
import time

try:
    smac = pyserial.Serial('/dev/tty.PL2303G-USBtoUART10', 9600)
except pyserial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

#print("Enter 'a' for topleft, 'd' for topright, 'w' for bottomleft, 's' for bottomright. Enter 'q' to quit.")

while True:
    key = input("Enter command: ")  # Waits for user input                                                                                                                          
    smac.write(key.encode())  # Send input as bytes
    if key == 'q':
        print("Exiting...")
        break                                                                                                                          

smac.close()

