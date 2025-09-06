# Trabajo Práctico N°2

**Nombres**  
- Callovi, Lautaro
- Galoppo, José María
- Moreyra, Julián
- Rivera, Luis Mariano

**Nombre del grupo**: pingFloyd

**Nombre del centro educativo**: FCEFYN - UNC

**Nombre de la materia**: Comunicaciones de Datos

**Profesores**
- Solinas, Miguel A.
- Henn, Santiago M.
- Oliva Cuneo, Facundo N.

**Fecha**: 8 de septiembre de 2025

---
### Información de los autores
 
**Información de contacto**:
- jose.maria.galoppo@mi.unc.edu.ar (Galoppo, José María)
- luismarianorivera.25@mi.unc.edu.ar (Rivera, Luis Mariano)
- julian.moreyra@mi.unc.edu.ar (Moreyra, Julián)
- lautaro.callovi@mi.unc.edu.ar (Callovi, Lautaro Nicolás)
---

## Resumen

## Introducción

## Actividad 1

## Actividad 2

## Actividad 3

## Actividad 4
A partir de los resultados obtenidos, del trabajo aquí realizado e información obtenida de diferentes medios de Internet, podemos llegar a elaborar algunas conclusiones:

- *Privacidad de un dispositivo en la red*

    Podríamos decir que la privacidad dentro de una red no es una característica que viene por defecto, la privacidad hace referencia a que tan protegida esta la información que nosotros como usuarios manejamos y enviamos al estar conectados a una red ya que esta puede ser vulnerable a ataques. Por ejemplo: en una red LAN (de Wi-Fi sin contraseña), uno como usuario puede simplemente confiar que no hay nadie espiando el tráfico de datos pero al ser abierta cualquiera puede usar algún tipo de sniffer para capturar el tráfico que no está cifrado. 
    Al conectarnos a una red podemos exponer información como direcciones IP, MAC del dispositivo, Metadatos, etc. Aunque nosotros tomemos buenas medidas de seguridad siempre podemos estar expuestos a ataques, lo mejor sería combinar tanto la tecnología como cifrado y protocolos junto a la consciencia del usuario a la hora de conectarse a la red.

- *Trazabilidad de la dirección MAC*

   Como nombramos anteriormente la dirección MAC del dispositivo puede estar expuesta a la hora de conectarnos a una red. La dirección MAC es un identificador único integrado en el dispositivo, es una cadena única de números y letras que identifican y pertenecen al hardware del dispositivo utilizado, se codifica en la tarjeta de interfaz de red, NIC. Esta sirve para que los dispositivos se reconozcan en una red. Aunque en redes más grandes esta no viaja más allá del router, dentro de una empresa o campus (LAN) puede ocurrir que esta, al ser única de un dispositivo, pueda ser falsificada por atacantes (spoofing). Para evitar esto algunos sistemas operativos modernos llevan a cabo la aleatorización de la misma, es decir, generar direcciones MAC aleatorias para cada red que se conecte el dispositivo.

- *Similitud de IMEI con MAC*

   El IMEI, International Mobile Equipment Identity (Identidad Internacional de Equipo Móvil), es un número único de 15 dígitos que identifica a cada telefono móvil o dispositivo con módem celular, está grabado en el hardware del equipo y no se repite, es único. Sirve para poder identificar un dispositivo en la red celular y diferenciarlo de la línea o chip SIM. 
   Podríamos decir que tanto el IMEI como la dirección MAC funcionan como "huellas digitales" de hardware que lo provee el fabricante de cada dispositivo. El IMEI opera en redes celulares e identifica al equipo físico, mientras que la MAC opera en redes locales e identifica a la interfaz de red. 
   Una diferencia es que el IMEI es mucho mas difícil de cambiar o alterar que la MAC de un dispositivo.

- *¿Una VPN oculta la dirección MAC del dispositivo?*

   Una VPN cifra todo el tráfico entre un dispositivo y el servidor VPN, oculta la dirección IP pública y evita que el proveedor de Internet vea el contenido del tráfico. Ahora, esto no oculta ni modifica la dirección MAC del dispositivo dentro de la red local, por lo que otros dispositivos que esten conectados a la misma red local o LAN son capaces y podrían ver mi dirección MAC, incluso utilizando una VPN.

Tanto la dirección MAC del dispositivo y el IMEI funcionan como identificadores únicos del hardware, uno en redes locales y el otro en redes celulares respectivamente, aunque estas facilitan la trazabilidad y la gestión, de la misma manera pueden suponer un riesgo si no tomamos las medidas necesarias.
De esta manera forma podemos afirmar que siempre debemos actuar con cautela a la hora de conectarnos a una red, la seguridad de la misma nunca está asegurada.