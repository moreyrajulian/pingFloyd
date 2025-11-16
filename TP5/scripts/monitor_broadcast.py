import paho.mqtt.client as mqtt

# --- Configuración Local ---
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPICO_SUSCRIPCION = "lan/broadcast/#"  # <-- El comodín (wildcard)

# --- Callbacks (API V1) ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[Monitor] ¡Conectado al broker en {BROKER_HOST}!")
        client.subscribe(TOPICO_SUSCRIPCION)
        print(f"[Monitor] Suscrito al tópico general: {TOPICO_SUSCRIPCION}")
    else:
        print(f"[Monitor] Fallo al conectar, código: {rc}")

def on_message(client, userdata, msg):
    mensaje = msg.payload.decode('utf-8')
    print(f"[Monitor] MENSAJE RECIBIDO: Tópico={msg.topic} | Mensaje={mensaje}")

# --- Script Principal ---
print("[Monitor Broadcast] Iniciando...")

# Forzamos la API V1
client_monitor = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client_monitor.on_connect = on_connect
client_monitor.on_message = on_message

client_monitor.connect(BROKER_HOST, BROKER_PORT, 60)
client_monitor.loop_forever()