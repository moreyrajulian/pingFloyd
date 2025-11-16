import paho.mqtt.client as mqtt

# --- Configuración Local ---
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPICO_SUSCRIPCION = "lan/deviceA/status"

# --- Callbacks (API V1) ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[Dispositivo B] ¡Conectado al broker en {BROKER_HOST}!")
        client.subscribe(TOPICO_SUSCRIPCION)
        print(f"[Dispositivo B] Suscrito a: {TOPICO_SUSCRIPCION}")
    else:
        print(f"[Dispositivo B] Fallo al conectar, código: {rc}")

def on_message(client, userdata, msg):
    mensaje = msg.payload.decode('utf-8')
    print(f"[Dispositivo B] MENSAJE RECIBIDO: Tópico={msg.topic} | Mensaje={mensaje}")

# --- Script Principal ---
print("[Dispositivo B] Iniciando...")

# Forzamos la API V1 (la que nos funcionó)
client_b = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client_b.on_connect = on_connect
client_b.on_message = on_message

client_b.connect(BROKER_HOST, BROKER_PORT, 60)
client_b.loop_forever()