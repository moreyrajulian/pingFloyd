import paho.mqtt.client as mqtt
import time
import random

# --- Configuración Local ---
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPICO_PUBLICACION = "lan/deviceA/status"

# --- Callbacks (API V1) ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[Dispositivo A] ¡Conectado al broker en {BROKER_HOST}!")
    else:
        print(f"[Dispositivo A] Fallo al conectar, código: {rc}")

# --- Script Principal ---
print("[Dispositivo A] Iniciando...")

# Forzamos la API V1
client_a = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client_a.on_connect = on_connect

client_a.connect(BROKER_HOST, BROKER_PORT, 60)

# Damos un segundo para que se conecte antes de empezar el bucle
client_a.loop_start() # Inicia un hilo en segundo plano
time.sleep(1)

contador = 0
try:
    while True:
        contador += 1
        mensaje = f"Reporte de estado Nro: {contador}"
        
        # Publicamos el mensaje
        client_a.publish(TOPICO_PUBLICACION, mensaje)
        print(f"[Dispositivo A] MENSAJE ENVIADO: Tópico={TOPICO_PUBLICACION} | Mensaje={mensaje}")
        
        time.sleep(3) # Esperamos 3 segundos

except KeyboardInterrupt:
    print("\n[Dispositivo A] Deteniendo...")
    client_a.loop_stop()