import paho.mqtt.client as mqtt
import time

# --- Configuración Local ---
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPICO_PUBLICACION = "lan/broadcast/all" # <-- Tópico específico

# --- Callbacks (API V1) ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[Central] ¡Conectado al broker en {BROKER_HOST}!")
    else:
        print(f"[Central] Fallo al conectar, código: {rc}")

# --- Script Principal ---
print("[Cliente Central] Iniciando...")

# Forzamos la API V1
client_central = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client_central.on_connect = on_connect

client_central.connect(BROKER_HOST, BROKER_PORT, 60)
client_central.loop_start()
time.sleep(1)

mensaje = "¡MENSAJE DE BROADCAST A TODA LA RED!"
client_central.publish(TOPICO_PUBLICACION, mensaje)
print(f"[Central] MENSAJE ENVIADO: Tópico={TOPICO_PUBLICACION} | Mensaje={mensaje}")

time.sleep(1) # Damos tiempo a que se envíe
client_central.loop_stop()
print("[Central] Mensaje enviado. Cerrando.")