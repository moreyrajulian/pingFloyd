import paho.mqtt.client as mqtt
import time

# --- Configuración Local ---
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPICO_COMANDOS = "lan/comandos/broadcast"

print("[Control Remoto] Iniciando...")

# Pedimos al usuario qué comando enviar
comando = input("¿Qué comando querés enviar? (START / STOP): ").upper()

if comando not in ["START", "STOP"]:
    print("Comando no válido. Saliendo.")
else:
    client_control = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    client_control.connect(BROKER_HOST, BROKER_PORT, 60)
    
    # Damos tiempo a que se conecte
    client_control.loop_start()
    time.sleep(1)
    
    # Publicamos el comando
    client_control.publish(TOPICO_COMANDOS, comando)
    print(f"¡Comando '{comando}' enviado a {TOPICO_COMANDOS}!")
    
    client_control.loop_stop()
    print("[Control Remoto] Cerrando.")