import serial
import csv
import time

# Configura el puerto serial
# Cambia 'COM3' (Windows) o '/dev/ttyUSB0' (Linux) al puerto correspondiente
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Nombre del archivo CSV
filename = "sensor_data.csv"

# Abre el archivo CSV en modo escritura
with open(filename, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Escribe encabezados (opcional)
    csv_writer.writerow(['Datos del sensor'])

    print("Recibiendo datos del puerto serial y guardando en", filename)
    
    while True:
        # Leer línea desde el puerto serial
        line = ser.readline().decode('utf-8').strip()
        
        if line:
            print("Datos recibidos:", line)
            
            # Guardar la línea recibida en el archivo CSV
            csv_writer.writerow([line])
            
        # Agrega una pequeña pausa para evitar una sobrecarga
        time.sleep(0.1)
