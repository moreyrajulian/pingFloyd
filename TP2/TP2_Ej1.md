## Resumen

El presente informe analiza el **efecto Doppler en las telecomunicaciones** [y aca los otros temas que tocaron]
Se explican los casos más relevantes afectados por el efecto Doppler, desde comunicaciones celulares y satelitales hasta transmisiones por cable, y se ejemplifica la influencia de la frecuencia en la magnitud del efecto Doppler.
## Introducción

El efecto Doppler es un fenómeno físico que afecta a las ondas cuando existe **movimiento relativo entre el emisor y el receptor**. Su estudio es fundamental en telecomunicaciones, ya que puede alterar la frecuencia percibida de las señales, especialmente en sistemas inalámbricos y de alta frecuencia.  
En este informe se describe cómo se manifiesta el efecto Doppler en diferentes tipos de comunicaciones, se analizan los sistemas más susceptibles y los menos afectados, y se aclara la diferencia entre este efecto y otros fenómenos, como las interferencias en dispositivos electrónicos.


.
.
.

.
.
.


# Desarrollo

### Actividad N°1

### Efecto Doppler en las telecomunicaciones

En la imagen se puede observar cómo una señal, mientras viaja por un medio, va variando su frecuencia.  
Una de las posibles causas de esta variación es el **efecto Doppler**, que afecta directamente a las telecomunicaciones, especialmente a las comunicaciones inalámbricas entre fuentes emisoras y receptoras en movimiento.  

El efecto es poco perceptible en la comunicación entre una antena y teléfonos celulares en superficie, pero resulta muy importante tenerlo en cuenta cuando se establece comunicación con satélites.  

El efecto Doppler se caracteriza por lo siguiente:  

- Cuando las fuentes (emisora y receptora) se **acercan**, el frente de onda aumenta su frecuencia percibida.  
- Cuando las fuentes se **alejan**, el frente de onda disminuye su frecuencia percibida.  

Es importante aclarar que, si las fuentes se mueven con **velocidad constante**, el efecto Doppler existe, pero la frecuencia percibida se mantiene constante durante el desplazamiento. En cambio, si las fuentes presentan **aceleración**, la frecuencia sí varía a lo largo del tiempo.

---

### Las comunicaciones con altas frecuencias vs el efecto doppler

La frecuencia percibida $f'$ se calcula mediante la fórmula general del efecto Doppler:

$$
f' = f \cdot \frac{c \pm v_r}{c \pm v_s}
$$

donde:

- $f$ = frecuencia emitida  
- $f'$ = frecuencia percibida  
- $c$ = velocidad de propagación de la onda (≈ velocidad de la luz en telecomunicaciones)  
- $v_r$ = velocidad del receptor (signo positivo si se acerca, negativo si se aleja)  
- $v_s$ = velocidad de la fuente (signo positivo si se aleja, negativo si se acerca)  

Se puede observar que la frecuencia de la señal emitida es directamente proporcional a la frecuencia percibida. Por lo tanto, las **comunicaciones con señales de alta frecuencia son más susceptibles al efecto Doppler**, ya que incluso velocidades moderadas pueden generar corrimientos significativos de frecuencia.

### Ejemplos de transmisiones según su susceptibilidad al Doppler

- **Alta frecuencia (UHF y SHF, 300 MHz – 30 GHz):**  
  - Bandas utilizadas en 4G/LTE, 5G sub-6 GHz y mmWave.  
  - Doppler moderado a alto, requiere corrección en la modulación y sincronización.  

- **Frecuencia extremadamente alta (EHF, 30–300 GHz):**  
  - Enlaces satelitales (banda Ka), WiFi mmWave, enlaces punto a punto de alta capacidad.  
  - Doppler muy significativo incluso a velocidades moderadas; se necesita compensación activa.  

- **Frecuencias bajas (MF, VHF, HF, 0.5–300 MHz):**  
  - Radio AM/FM, TV terrestre, radioaficionados.  
  - Doppler despreciable; la variación en Hz es mínima en comparación con la frecuencia de la señal.  

### Comunicaciones menos afectadas

- **Comunicaciones por cable:** fibra óptica, cable coaxial, DSL.  
  - No se ven afectadas por movimiento relativo entre transmisor y receptor.  

- **Enlaces terrestres de baja frecuencia:** radio AM/FM, VHF, HF.  

- **Redes inalámbricas estacionarias o de corta distancia:** WiFi convencional en interiores, dispositivos IoT fijos.  

---

### Teléfonos celulares en aviones

Actualmente, gracias a los avances tecnológicos, **encender los celulares dentro de un avión no representa riesgos significativos**.  

Sin embargo, esto no siempre fue así. Hace algunos años, los teléfonos celulares podían operar en **las mismas bandas de frecuencia que algunos instrumentos del avión**, lo que **podía generar interferencias**.  

Es importante aclarar que esto **no tiene relación con el efecto Doppler**. La interferencia es un fenómeno distinto, que ocurre cuando señales electromagnéticas de frecuencias similares se superponen y afectan el funcionamiento de los equipos.

.
.
.

.
.
.


## Conclusiones

El efecto Doppler es un fenómeno fundamental en las telecomunicaciones, cuya importancia aumenta con la frecuencia de la señal y la velocidad relativa entre emisor y receptor. 
En comunicaciones inalámbricas de alta frecuencia, como 5G mmWave o enlaces satelitales, el corrimiento Doppler puede ser significativo y requiere compensación activa para mantener la integridad de la señal.
