## 1.a) Clasificación de redes según su alcance

Las redes se clasifican comúnmente según su alcance geográfico de la siguiente manera:

* **PAN (Personal Area Network - Red de Área Personal):**
    * **Características:** Es la red de menor alcance, cubriendo el espacio de trabajo de un solo individuo (generalmente unos pocos metros). Se utiliza para conectar dispositivos personales como teclados, ratones, auriculares y smartphones.
    * **Ejemplo:** Bluetooth, Zigbee.

* **LAN (Local Area Network - Red de Área Local):**
    * **Características:** Cubre un área geográfica limitada como una oficina, un edificio, un hogar o un campus pequeño. Se caracteriza por altas velocidades de transmisión (desde 100 Mbps a 10 Gbps) y baja latencia, ya que la infraestructura es propiedad de la organización.
    * **Ejemplo:** Una red Ethernet cableada en una oficina o una red Wi-Fi (conocida como WLAN) en una casa.

* **MAN (Metropolitan Area Network - Red de Área Metropolitana):**
    * **Características:** Cubre un área más grande que una LAN, como una ciudad entera o un gran campus universitario. Suelen interconectar múltiples LANs.
    * **Ejemplo:** Redes de fibra óptica de proveedores de servicios de cable en una ciudad.

* **WAN (Wide Area Network - Red de Área Amplia):**
    * **Características:** Cubre una gran área geográfica (país, continente o el mundo entero). Interconecta múltiples LANs y MANs que no están geográficamente cercanas. Las velocidades son más variables y las latencias más altas que en las LANs, ya que a menudo dependen de enlaces de proveedores de servicios.
    * **Ejemplo:** Internet es el ejemplo más grande de una WAN.



## 1.b) Definición y clasificación de VLAN

### ¿Qué es una VLAN?

Una **VLAN (Virtual Local Area Network)** o Red de Área Local Virtual, es un método para crear redes lógicas independientes dentro de una misma infraestructura de red física.

Permite agrupar dispositivos en diferentes segmentos de red como si estuvieran en la misma red física, aunque estén conectados a diferentes switches. Su principal ventaja es que segmenta los dominios de broadcast, lo que mejora el rendimiento y la seguridad de la red. Los dispositivos en una VLAN no pueden comunicarse directamente con dispositivos en otra VLAN sin un dispositivo de Capa 3 (como un router).

### ¿Cómo se clasifican?

Las VLANs se pueden clasificar según el método utilizado para asignar la pertenencia de un dispositivo a una VLAN:

1.  **VLAN Estática (Basada en Puerto):** Es el método más común y el que se usa en este práctico. La pertenencia a la VLAN se configura manualmente asignando puertos específicos de un switch a una VLAN determinada. Cualquier dispositivo que se conecte a ese puerto pertenece automáticamente a esa VLAN. Es segura y fácil de configurar, pero menos flexible si un usuario se mueve mucho.

2.  **VLAN Dinámica (Basada en Dirección MAC):** La pertenencia se asigna dinámicamente según la dirección MAC del dispositivo que se conecta. Requiere un servidor central (llamado VMPS - VLAN Management Policy Server) que mantiene una base de datos de direcciones MAC y su VLAN correspondiente. Es más flexible, pero más compleja de administrar.

3.  **VLAN Basada en Protocolo:** La pertenencia se determina por el protocolo de Capa 3 que transporta el paquete (por ejemplo, IP o IPX). Es menos común en redes modernas.

---

## 1.c) Protocolo IEEE 802.1Q

**IEEE 802.1Q** es el estándar de la industria que define el método de etiquetado de tramas (frame tagging) para implementar VLANs sobre redes Ethernet.

**Relación con las VLANs:**
Su función principal es permitir que el tráfico de múltiples VLANs atraviese un único enlace físico (conocido como enlace troncal o trunk) entre switches, sin que se mezclen los dominios de broadcast.

Para lograr esto, el protocolo 802.1Q funciona insertando una etiqueta (tag) de 4 bytes en el encabezado de la trama Ethernet original, justo después de la dirección MAC de origen.


Esta etiqueta contiene:
* **TPID (Tag Protocol Identifier):** 2 bytes. Tiene un valor fijo de `0x8100` que identifica la trama como una trama 802.1Q.
* **TCI (Tag Control Information):** 2 bytes, que se subdividen en:
    * PCP (Priority Code Point): 3 bits para Calidad de Servicio (QoS).
    * DEI (Drop Eligible Indicator): 1 bit para indicar si la trama puede ser descartada bajo congestión.
    * VLAN ID (VLAN Identifier): 12 bits que especifican el número de la VLAN a la que pertenece la trama. Este campo es el corazón del protocolo, ya que permite identificar hasta 4094 VLANs utilizables (de 1 a 4094, ya que 0 y 4095 están reservados).

Cuando una trama de una VLAN debe cruzar un enlace troncal, el switch de origen le añade esta etiqueta. El switch receptor la lee, sabe a qué VLAN pertenece la trama y la reenvía solo a los puertos de esa VLAN.

---

## 1.d) Tagging (Etiquetado)

En el contexto de las VLANs y el protocolo 802.1Q, el "Tagging" (etiquetado) es el proceso de añadir la etiqueta 802.1Q de 4 bytes a una trama Ethernet.

Este proceso es fundamental para el funcionamiento de los enlaces troncales (trunk):

1.  Una trama llega a un switch desde un dispositivo final (PC) a través de un puerto de acceso (un puerto asignado a una sola VLAN, ej: VLAN 10). Esta trama original no tiene etiqueta.
2.  El switch determina que la trama debe ser enviada a otro switch a través de un puerto troncal.
3.  Antes de enviarla por el troncal, el switch añade (tagging) la etiqueta 802.1Q a la trama, especificando el VLAN ID (ej: 10).
4.  La trama "etiquetada" viaja por el enlace troncal.
5.  El switch receptor recibe la trama, lee la etiqueta, e identifica que pertenece a la VLAN 10.
6.  Cuando la trama va a salir por un puerto de acceso hacia el dispositivo final de destino (en la VLAN 10), el switch remueve la etiqueta (untagging) y entrega la trama Ethernet original.
