# Trabajo Práctico N°3

**Integrantes**  
- Callovi, Lautaro
- Galoppo, José María
- Moreyra, Julián
- Rivera, Luis Mariano

**Grupo**: pingFloyd

**Centro educativo**: FCEFYN - UNC

**Asignatura**: Comunicaciones de Datos

**Profesores**
- Solinas, Miguel A.
- Henn, Santiago M.
- Oliva Cuneo, Facundo N.

**Fecha**: 22 de septiembre de 2025

---
### Información de los autores
- jose.maria.galoppo@mi.unc.edu.ar (Galoppo, José María)
- luismarianorivera.25@mi.unc.edu.ar (Rivera, Luis Mariano)
- julian.moreyra@mi.unc.edu.ar (Moreyra, Julián)
- lautaro.callovi@mi.unc.edu.ar (Callovi, Lautaro Nicolás)
---


## Resumen
Se presenta parte de la evolución de los estándares IEEE 802.3 e IEEE 802.11. Se comenta la relación entre los protocolos y los niveles de seguridad. Se realiza una prueba práctica para determinar los estándares de red utilizados en la facultad.

Asimismo, se comparan diferentes versiones de Wi-Fi en cuanto a velocidad, modulación, bandas de frecuencia y mecanismos de seguridad, destacando las mejoras que aportan Wi-Fi 6 y Wi-Fi 7 frente a generaciones anteriores. También se analiza el papel de la fibra óptica (monomodo y multimodo), su fundamento físico mediante la Ley de Snell y su relación con las comunicaciones inalámbricas.

Por otra parte, se estudian diversos protocolos de comunicación para IoT (como ZigBee, LoRa, NB-IoT y Bluetooth), comparando sus alcances, tasas de transmisión y ámbitos de aplicación. Finalmente, se revisan las tecnologías que permiten la conectividad a Internet en un avión, como enlaces satelitales y aire-tierra, diferenciando entre el tráfico interno y el acceso a Internet.

## Introducción
Los estándares IEEE 802.3 e IEEE 802.11 son fundamentales para el buen funcionamiento de las redes hoy en día, ya sean cableadas (802.3) o inalámbricas (802.11). A medida que la tecnología fue avanzando, estos estándares se fueron modificando para ofrecer mejores prestaciones. Temas como velocidad, modulaciones e incluso aspectos normativos y de seguridad fueron cambiando con el paso de los años.

En este trabajo se aborda tanto la evolución de dichos estándares como su aplicación práctica, mediante la identificación de protocolos en uso dentro de la facultad y el análisis de las características de compatibilidad entre dispositivos. También se estudian los mecanismos de seguridad que acompañaron a cada versión, desde los vulnerables WEP hasta el actual WPA3.

Además, se incluye el estudio de medios de transmisión alternativos como la fibra óptica y su fundamento físico, así como la comparación con otras tecnologías de comunicación de corto y largo alcance utilizadas en IoT. Finalmente, se presentan aplicaciones reales de estas tecnologías, como la conectividad en aviones, que combina distintos tipos de enlaces para ofrecer servicios a bordo.

## Desarrollo

## Actividad 1

### Estándares 802.3 y 802.11

**IEEE 802.3**

El estándar IEEE 802.3 se remonta a 1983 y fue el primer intento de estandarizar redes Ethernet, que previamente utilizaban otros formatos como Ethernet II. Este estándar buscaba normalizar las velocidades de transmisión y los medios físicos, que en ese momento eran principalmente cables coaxiales.

Al inicio, existía una pequeña diferencia entre las cabeceras definidas por Ethernet y las de 802.3, particularmente en el campo ubicado después de las direcciones de destino y origen dentro del header.

Desde entonces, el estándar ha tenido varias ampliaciones, abarcando aspectos como velocidades, redes virtuales (VLANs), hubs, switches y distintos tipos de medios. Una de las últimas modificaciones importantes fue IEEE 802.3df‑2024, publicada el 15 de marzo de 2024, en la que se establecieron nuevos parámetros MAC y PHY, así como nuevas cláusulas técnicas y anexos relacionados con el funcionamiento de Ethernet a altas velocidades.

**IEEE 802.11**

El estándar IEEE 802.11 se remonta a 1997 y tiene como objetivo estandarizar las redes inalámbricas. La primera versión incluía redes que utilizaban infrarrojo, tecnología que hoy en día ya no se usa, aunque aún forma parte del estándar.

La versión IEEE 802.11b fue la primera en ser ampliamente aceptada, ya que ofrecía velocidades competitivas frente a Ethernet y los dispositivos que implementaban este estándar eran más económicos. Además, IEEE 802.11 implementa el protocolo CSMA/CA (Carrier Sense Multiple Access / Collision Avoidance) para gestionar el acceso al medio inalámbrico y evitar colisiones.

Uno de los últimos cambios importantes al estándar fue IEEE 802.11be‑2024 (“Wi‑Fi 7”), publicado el 22 de julio de 2025. Esta versión introduce mejoras de rendimiento extremo (Extremely High Throughput, EHT), alcanzando velocidades de hasta 30 Gbps a nivel MAC, en bandas de frecuencia entre 1 GHz y 7.25 GHz. Además, incluye mejoras en latencia (worst case latency) y jitter, aumentando la confiabilidad de la conexión incluso en condiciones adversas.

### Experimento: Determinar versión del protocolo 802.11 de una red de la facultad
![cmd](codigocmd.png)

Ejecutando el comando **netsh** en una notebook conectada a la red wifi, se pudo observar la versión del protocolo 802.11 de la red FCEFyN. Siendo la 802.11n.

### Redes y dispositivos incompatibles
Si un dispositivo tiene una NIC que no soporta el estándar de la red (por ejemplo, Wi‑Fi), no podrá establecer conexión. La red puede no aparecer en la lista de redes disponibles, o bien, en algunos casos, la conexión se logra pero funciona muy lentamente y puede sufrir interrupciones frecuentes constantemente.

### Protocolos y seguridad

A medida que los estándares Wi‑Fi fueron evolucionando, también mejoraron los mecanismos de seguridad, incluyendo métodos de cifrado y algoritmos de autenticación, con el objetivo de proteger las conexiones frente a accesos no autorizados.

Una de las primeras formas de seguridad fue WEP (Wired Equivalent Privacy), que aunque permitía cifrar la información, resultó ser muy vulnerable a ataques y podía ser fácilmente vulnerada por terceros. Posteriormente, se introdujo WPA (Wi‑Fi Protected Access), seguido de WPA2, que incorporó cifrado AES y mejoras en la gestión de claves, proporcionando una protección mucho más robusta.

Actualmente, el estándar WPA3 es uno de los más recientes y seguros, ofreciendo autenticación avanzada, cifrado individualizado y protección frente a ataques modernos, como el “key reinstallation attack” (KRACK).

Cada nueva versión del estándar Wi‑Fi corrige vulnerabilidades de versiones anteriores, asegurando conexiones más confiables y seguras para los usuarios.

### Experimento: Seguridad de una red de la facultad
Se puede observar en la imagen:
![cmd](codigocmd.png)

Que al ser una red abierta no utiliza Wi‑Fi Protected Access y además no contiene cifrado. Por lo que la seguridad es nula.
La version 802.11g (anterior a 802.11n) soporta hasta WPA2.

### Versiones WIFI y sus características


| -                       | WIFI 5                         | WIFI 6                         | WIFI 7                         |
|-------------------------|--------------------------------|--------------------------------|--------------------------------|
| Versión IEEE            | IEEE 802.11ac                  | IEEE 802.11ax                  | IEEE 802.11be                  |
| Tasa de datos máxima    | Hasta 3.5 Gbps                 | Hasta 9.6 Gbps                 | Hasta 46 Gbps                  |
| Banda(s)                | 5 GHz (también 2.4 GHz)        | 5 GHz (también 2.4 GHz)        |6 GHz (también 2.4 GHz y 5 GHz) |
| Ancho de Banda          | Entre 80 y 160 MHz por canal   | Entre 80 y 160 MHz por canal   | Entre 80 y 320 MHz por canal   |
| Modulación              | 256-QAM                        | 1024-QAM                       |4096-QAM                        |
| Sistema de Seguridad    | Hasta WPA2                     | Hasta WPA3                     |Hasta WPA3                      |

## Actividad 2

a) La imagen nos ilustra dos tipos de transmision con fibra optica. En la izquierda se representa la **fibra monomodo**, en la cual un haz de luz viaja por un unico trayecto dentro del nucleo. Este tipo nos ofrece caracteristicas tales como:
+ Mayor ancho de banda
+ Baja atenuacion
+ Minima dispersion

Esto resulta ideal para la transmision en largas distancias en altas velocidades. Sin embargo, tiene un costo elevado de implementacion debido a la presicion que requiere tanto la fibra como los emisores (laseres). 


En la parte de la derecha de la imagen se representa la **fibra multimodo**, donde la luz se propagada a traves de varios caminos o modos. Este tipo de fibra es mas economica y sencilla de instalar, ya que suele utilizar LEDs como fuente de luz, pero representa dispersion modal, lo que la limita en distancia y velocidad de transmision.

b) La **Ley de Snell** establece la relación entre los ángulos de incidencia y refracción de un rayo de luz al pasar de un medio a otro con diferente índice de refracción:
$$
n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)
$$
En la fibra óptica esta ley explica el fenómeno de reflexión interna total, que es el principio de funcionamiento básico de estas transmisiones. Si el ángulo de incidencia supera un valor crítico, la luz no atraviesa el revestimiento sino que se refleja completamente dentro del núcleo, permitiendo así su propagación a lo largo de la fibra. En el caso de la fibra monomodo, la luz viaja en una unica trayectoria, mientras que en la fibra multimodo son posibles múltiples de estas, todas regidas por la misma ley física.

c) La relación entre las conexiones inalámbricas y la fibra óptica radica en que ambas transmiten información mediante ondas electromagnéticas, aunque en diferentes rangos del espectro. Las conexiones inalámbricas utilizan ondas de radio o microondas que viajan por el aire, mientras que la fibra óptica emplea luz en frecuencias mucho más altas, confinada dentro de la fibra.

## Actividad 3

# Protocolos de Comunicación Inalámbrica e IoT

a) Protocolos y Estándares

| Protocolo | ¿Está estandarizado? | Estándar / Última versión |
|-----------|----------------------|---------------------------|
| Wi-Fi     | Sí                   | IEEE 802.11 (última: 802.11be - Wi-Fi 7) |
| Bluetooth | Sí                   | IEEE 802.15.1 / Bluetooth 5.4 |
| ZigBee    | Sí                   | IEEE 802.15.4 |
| NFC       | Sí                   | ISO/IEC 18092, ECMA-340 |
| LTE       | Sí                   | 3GPP Release 8 (evoluciones hasta Release 14 LTE-Advanced Pro) |
| GSM       | Sí                   | 3GPP TS 45.x / ETSI (GSM Release 1990+) |
| 5G (3GPP) | Sí                   | 3GPP Release 15–18 (NR - New Radio) |
| LoRa      | Parcial (LoRa propietario, LoRaWAN estandarizado) | LoRaWAN por LoRa Alliance (v1.0.4, 2021) |
| NB-IoT    | Sí                   | 3GPP Release 13 en adelante |
| SigFox    | No completamente (propietario) | Especificación propietaria de SigFox |
| Z-Wave    | Sí (desde 2012 en ITU-T) | ITU-T G.9959 |

---

b) Gráfico de Alcance vs Tasa de Datos

Ubicación aproximada de los protocolos en el gráfico (Data rate vs Distance):

- **Wi-Fi** → ~100 m, hasta varios Gbps.  
- **Bluetooth** → ~10 m, hasta 2–3 Mbps (Bluetooth 5.4 puede llegar a 100 m en modos especiales).  
- **ZigBee** → ~10–100 m, hasta 250 kbps.  
- **NFC** → <10 cm, hasta 424 kbps.  
- **LTE** → ~10 km, hasta 300 Mbps.  
- **GSM** → ~35 km (máx. celda), hasta 200 kbps (EDGE).  
- **5G** → ~1–10 km, hasta 10 Gbps.  
- **LoRa** → ~2–15 km, hasta 50 kbps.  
- **NB-IoT** → ~10 km, hasta 250 kbps.  
- **SigFox** → ~10–50 km, hasta 100 bps.  
- **Z-Wave** → ~100 m, hasta 100 kbps.  

![Grafica de tasa de datos y distancias](image.png)

---

c) Comparación de Medios de Transmisión

| Característica | UTP | Fibra Óptica | Wi-Fi 802.11be (Wi-Fi 7) | Bluetooth 5.4 | 5G |
|----------------|-----|--------------|---------------------------|---------------|----|
| **Ancho de banda** | Hasta 10 Gbps (Cat6a/7), 40 Gbps en Cat8 | >1 Tbps (en laboratorio), típicamente 100 Gbps comercial | Hasta 46 Gbps | ~2 Mbps (modo clásico), hasta 2 Mbps LE; alcance extendido <1 Mbps | >10 Gbps (teórico, con anchos de banda de 400 MHz) |
| **Distancias** | 100 m máx. | Varios km (decenas con repetidores) | ~100 m | 10–100 m | 1–10 km |
| **Inmunidad a EMI/RFI** | Baja | Muy alta | Media (puede afectarse) | Media | Media-alta |
| **Costos de medios/conectores/dispositivos** | Bajo | Alto | Medio | Bajo | Alto |
| **¿Disponible en Packet Tracer?** | Sí | Sí | Sí (802.11ac/ax según versión) | No | No |

---


## Actividad 4

a) Al hablar de conectividad a Internet en un avión en vuelo surgen algunas tecnologías que pueden hacerlo posible. Aquí se encontrarán detalladas con sus características y limitaciones:

### Tecnología Satelital o Satellite Communications (SATCOM)
Esta tecnología permite a los aviones conectarse con satélites en órbita, entre ellos tenemos a:
+ Satélites Geoestacionarios (GEO) que se encuentran a unos 36000 km de altitud, incluyendo una amplia cobertura hasta para rutas transoceánicas pero puede incluir cierta latencia por la gran distancia.
+ Satélites de Órbita Media (MEO) a una altitud de 2000 a 20000 km, suelen ofrecer una menor latencia que los GEO pero se necesita de una red de múltiples satélites y antenas para el avión que permitan cambiar de conexión entre satélites.
+ Satélites de Órbita baja (LEO) a una altitud de 500 a 2000 km, un ejemplo es Starlink, estos ofrecen una muy baja latencia y velocidades mas altas que las demás, ideal para videollamadas, streaming y juegos. Su limitación es que se requiere de una gran constelación de miles de satélites para poder ofrecer una cobertura continua y decente.

Estas tecnologías se usan mucho para vuelos transoceánicos o donde no existe una cobertura terrestre.

### Tecnologías Aire-Tierra (ATG Air-to-Ground)
Esta tecnología permite a los aviones conectarse a una red de torres de telefonía móvil que se encuentran instaladas en tierra (como las 4G/5G) mediante una antena ubicada en la parte inferior del avión. 
Estas generalmente son más lentas que las conexiones satelitales ya que depende de que existan las antenas en tierra, además en áreas rurales o zonas donde no se encuentren instaladas muchas torres la conexión puede ser intermitente.

Se suele usar para vuelos sobre tierra firme.

b) 

[1] G. Fontanesi et al., "Artificial Intelligence for Satellite Communication: A Survey," in IEEE Communications Surveys & Tutorials, doi: 10.1109/COMST.2025.3534617.
URL: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10886927&isnumber=5451756




[2] S. L. Barbera et al., "SATCOM for Air Traffic Management: Benefits and Technological Roadmap of the FOC Space Segment Solution," 2025 Integrated Communications, Navigation and Surveillance Conference (ICNS), Brussels, Belgium, 2025, pp. 1-10, doi: 10.1109/ICNS65417.2025.10976806. URL: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10976806&isnumber=10976746

c) Podríamos pensarlo como dos redes separadas, una interna, donde todo queda dentro de la red del avión sin afectar a la conexión de Internet, con un servidor local gratis e ilimitado para los pasajeros que permite ver películas, series o jugar juegos. El tráfico nunca sale del avión, el pasajero se conecta a la red Wi-Fi del avión y el tráfico viaja desde el servidor al dispositivo dentro de la misma red de área local (LAN).

Luego, el tráfico de Internet como correos, redes sociales, navegar páginas web, etc. Si necesita de una conexión satelital o vía antenas en tierra, necesita "salir" del avión mediante una conexión satelital o ATG. Este es el tráfico que consume ancho de banda del servicio de internet pago, que a su vez es costoso y compartido entre los pasajeros del avión.


