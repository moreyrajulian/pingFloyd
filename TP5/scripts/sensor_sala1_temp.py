import paho.mqtt.client as mqtt
import time
import random

# --- Configuración Local ---
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPICO_PUBLICACION = "lan/sala1/sensor/temp" # <-- Tópico de ESTE sensor
TOPICO_COMANDOS = "lan/comandos/broadcast"   # <-- Tópico que TODOS escuchan

# Variable global para saber si debemos simular
simulacion_activa = False

# --- Callbacks (API V1) ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[Sensor {TOPICO_PUBLICACION}] Conectado al broker")
        # El sensor se suscribe al tópico de comandos
        client.subscribe(TOPICO_COMANDOS)
        print(f"[Sensor {TOPICO_PUBLICACION}] Suscrito a comandos en: {TOPICO_COMANDOS}")
    else:
        print(f"[Sensor {TOPICO_PUBLICACION}] Fallo al conectar: {rc}")

def on_message(client, userdata, msg):
    global simulacion_activa # Para modificar la variable global
    
    comando = msg.payload.decode('utf-8')
    print(f"[Sensor {TOPICO_PUBLICACION}] COMANDO RECIBIDO: {comando}")
    
    if comando == "START":
        simulacion_activa = True
    elif comando == "STOP":
        simulacion_activa = False

# --- Script Principal ---
print(f"[Sensor {TOPICO_PUBLICACION}] Iniciando...")

client_sensor = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client_sensor.on_connect = on_connect
client_sensor.on_message = on_message

client_sensor.connect(BROKER_HOST, BROKER_PORT, 60)

# ¡¡LA CLAVE!!
# loop_start() inicia un hilo en segundo plano que maneja 
# la conexión y los callbacks (como on_message).
client_sensor.loop_start() 

print(f"[Sensor {TOPICO_PUBLICACION}] Esperando comando 'START'...")

try:
    while True:
        # El hilo principal se queda en este bucle
        if simulacion_activa:
            # Generamos un dato aleatorio (simulando > 500ms)
            temperatura = round(random.uniform(20.0, 25.0), 2)
            
            client_sensor.publish(TOPICO_PUBLICACION, str(temperatura))
            print(f"[Sensor {TOPICO_PUBLICACION}] Publicado: {temperatura}")
            
            time.sleep(random.randint(1, 3)) # Espera entre 1 y 3 seg
        else:
            # Si no está activa, solo esperamos
            time.sleep(1)

except KeyboardInterrupt:
    print(f"\n[Sensor {TOPICO_PUBLICACION}] Deteniendo...")
    client_sensor.loop_stop() # Detenemos el hilo de red