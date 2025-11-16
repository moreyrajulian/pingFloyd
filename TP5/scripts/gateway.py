import paho.mqtt.client as mqtt
import datetime
import os # Para verificar si el archivo existe

# --- Configuración Local ---
BROKER_HOST = "localhost"
BROKER_PORT = 1883
# Tópico con comodines para todas las salas y sensores
TOPICO_SUSCRIPCION = "lan/+/sensor/+" 
ARCHIVO_CSV = "datos_sensores.csv"

# --- Callbacks (API V1) ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[Gateway] ¡Conectado al broker!")
        client.subscribe(TOPICO_SUSCRIPCION)
        print(f"[Gateway] Suscrito a: {TOPICO_SUSCRIPCION}")
    else:
        print(f"[Gateway] Fallo al conectar, código: {rc}")

def on_message(client, userdata, msg):
    try:
        mensaje = msg.payload.decode('utf-8')
        tópico = msg.topic
        timestamp = datetime.datetime.now().isoformat()
        
        print(f"[Gateway] DATO RECIBIDO: Tópico={tópico} | Mensaje={mensaje}")
        
        # Guardamos en el CSV
        with open(ARCHIVO_CSV, 'a', encoding='utf-8') as f:
            # 'a' significa "append" (agregar al final)
            f.write(f"{timestamp};{tópico};{mensaje}\n")
            
    except Exception as e:
        print(f"[Gateway] Error al procesar mensaje: {e}")

# --- Script Principal ---
print("[Gateway] Iniciando...")

# Escribimos el encabezado del CSV si el archivo no existe
if not os.path.exists(ARCHIVO_CSV):
    with open(ARCHIVO_CSV, 'w', encoding='utf-8') as f:
        # 'w' significa "write" (sobrescribir)
        f.write("Timestamp;Topico;Valor\n")

# Forzamos la API V1 (la que nos funcionó)
client_gw = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client_gw.on_connect = on_connect
client_gw.on_message = on_message

client_gw.connect(BROKER_HOST, BROKER_PORT, 60)
client_gw.loop_forever() # El gateway solo escucha, así que va con loop_forever