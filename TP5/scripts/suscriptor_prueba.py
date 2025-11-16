import paho.mqtt.client as mqtt

# --- Configuración ---
BROKER_HOST = "4d53cd59228d4a4fafd36b91899525b7.s1.eu.hivemq.cloud"
BROKER_PORT = 8883 
TOPICO_PRUEBA = "probando TP5"
TU_USUARIO = "julianmoreyra"
TU_PASSWORD = "Moreyrajulian1"

# --- CAMBIO 1: Quitamos 'properties' ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"¡Conectado exitosamente al broker en {BROKER_HOST}!")
        client.subscribe(TOPICO_PRUEBA)
        print(f"Suscrito al tópico: {TOPICO_PRUEBA}")
    else:
        print(f"Fallo al conectar, código de retorno: {rc}")

# --- CAMBIO 2: Quitamos 'properties' ---
def on_message(client, userdata, msg):
    print(f"MENSAJE RECIBIDO: Tópico = {msg.topic} | Mensaje = {msg.payload.decode('utf-8')}")

# --- Script Principal ---
print("Intentando conectar al broker de HiveMQ Cloud...")

# --- CAMBIO 3: Forzamos la API V1 ---
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)

# Asignamos las funciones "callback"
client.on_connect = on_connect
client.on_message = on_message

# 1. Establecemos el usuario y contraseña
client.username_pw_set(TU_USUARIO, TU_PASSWORD)
# 2. Le decimos que use una conexión segura (TLS/SSL)
client.tls_set()

# Nos conectamos al broker
client.connect(BROKER_HOST, BROKER_PORT, 60)

# Bucle
client.loop_forever()