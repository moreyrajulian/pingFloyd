## Trabajo práctico N°1

### Actividad 1:

### Breve introducción
Una onda electromagnética es una **perturbación que se propaga en el campo electromagnético**.
Está compuesta por un campo eléctrico y un campo magnético que oscilan perpendicularmente entre sí y a la dirección de propagación.
Curiosamente, según las ecuaciones de Maxwell, una variación de un campo eléctrico genera un campo magnético y viceversa, por lo que no pueden existir de forma independiente en una onda propagándose en el vacío.
Estas ondas transportan energía, momento y pueden interactuar con la materia.
Además, no necesitan de un medio físico para propagarse como si lo necesitan las ondas mecánicas.

Las ondas están caracterizadas por:
- Longitud de onda
- Frecuencia
- Amplitud
- Fase

Estas ondas pueden manipularse para transmitir información. Las técnicas para esto son la modulación y la demodulación.
La modulación es el proceso de alterar las características de una onda electromagnética portadora (como su amplitud, frecuencia o fase) para que pueda transportar información, mientras que la demodulación es el proceso inverso, donde se extrae la información original de la señal modulada.

De ahora en más, se hablará de **señales** y de **ondas** indistintamente.  

Las señales se pueden clasificar en dos grupos según cómo se analice su comportamiento en el **tiempo**: **continuas** y **discretas**.  

### Señales continuas
Son aquellas definidas para **todos los instantes de tiempo** dentro de un intervalo determinado. Su representación es una función continua $x(t)$, y pueden variar suavemente (variación continua y diferenciable) sin interrupciones.  

### Señales discretas
Son aquellas definidas únicamente en **instantes específicos de tiempo**. Se representan como secuencias $x[n]$, donde $n$ es un número entero que indica el índice temporal. Estas señales son más comunes en sistemas digitales.


### Análisis de la onda
(acá va la URL de la imagen local en github)

En la imagen se observa una onda senoidal cuya amplitud disminuye con la distancia. Es decir, se observa un efecto de **atenuación**. La frecuencia de la onda se mantiene constante.

La frecuencia $f$ de la onda se puede calcular usando la relación:

$$
\Large f = \frac{v}{\lambda}
$$

donde:
- $v$ es la velocidad de propagación de la onda
- $\lambda$ es la longitud de onda.

De la imagen se extrae que $\lambda = 60\ \text{mm} = 0.06\ \text{m}$.  
Suponiendo que la onda se propaga en el vacío a velocidad $v = 3\times10^8 \ \text{m/s}$, se obtiene:

$$
\Large f = \frac{3\times10^8}{0.06} = 5 \ \text{GHz}
$$

### Bandas del espectro según la ITU y su relación con la onda analizada

| Banda | Abreviatura | Rango de Frecuencia | Rango de Longitud de Onda |
|-------|--------------|---------------------|---------------------------|
| Muy Baja Frecuencia | VLF | 3 a 30 kHz | 10 a 100 km |
| Baja Frecuencia | LF | 30 a 300 kHz | 1 a 10 km |
| Media Frecuencia | MF | 300 a 3000 kHz | 100 a 1000 m |
| Alta Frecuencia | HF | 3 a 30 MHz | 10 a 100 m |
| Muy Alta Frecuencia | VHF | 30 a 300 MHz | 1 a 10 m |
| Ultra Alta Frecuencia | UHF | 300 a 3000 MHz | 10 a 100 cm |
| Super Alta Frecuencia | SHF | 3 a 30 GHz | 1 a 10 cm |
| Ultra Alta Frecuencia Extrema | EHF | 30 a 300 GHz | 1 a 10 mm |
| Terahercios | THF | 300 a 3000 GHz | 0.1 a 1 mm |

Por lo que la señal se considera SHF (banda 9).

### Ejemplo de dispositivo que opera en esta banda
Un ejemplo de dispositivo que opera en estas bandas son los routers Wi-Fi, que utilizan frecuencias de 2,4 GHz (UHF) y 5 GHz (SHF) para la transmisión de datos inalámbrica.

### Análisis de la atenuación
La línea roja en la imagen representa como la **amplitud de la señal** se **atenúa exponencialmente** con la distancia. Visto solo en dos dimensiones.  

Esta atenuación influye sobre los dispositivos que utilizan **señales electromagnéticas para transmitir datos**. Un caso muy común son los routers Wi-Fi: por ejemplo, la comunicación entre un celular y el router puede disminuir significativamente a medida que ambos se alejan.

La atenuación de la señal afecta a transmisiones por telefonía celular, cable coaxial y fibra óptica, pero de distintas formas.

Se debe tener en cuenta que, cualquiera que sea el medio que atraviesa la señal, esta se verá afectada por su naturaleza. En comunicaciones digitales, esta situación se modela mediante filtros.

Si bien podemos suponer que la energía total de la onda electromagnética se mantiene constante, al expandirse en todas las direcciones, su intensidad en una sola dirección o eje disminuye. Lo que se percibe como atenuación.

**Analizando cada caso:**

1. La telefonía celular se comunica de forma inalámbrica, lo que significa que las ondas electromagnéticas viajan libres en el espacio sin un medio físico que las confine.
Esto permite que la onda se expanda en todas direcciones desde la antena emisora, lo que provoca que la potencia se distribuya sobre un área cada vez mayor conforme aumenta la distancia, siguiendo la ley del cuadrado inverso.
Además, durante su propagación, la onda puede sufrir absorción por la atmósfera, pérdidas por dispersión, reflexión y difracción al encontrarse con obstáculos como edificios, árboles o el terreno.

2. Los cables coaxiales están formados por distintas capas: un conductor central, un dieléctrico que lo separa de un conductor externo (blindaje) y una cubierta protectora.
El blindaje y la geometría coaxial permiten que la onda electromagnética viaje en el interior del cable, minimizando la radiación y aislándola del ruido electromagnético externo.
Lo que medimos en los extremos del cable no es la “onda” directamente, sino la señal eléctrica (tensión y corriente) asociada a esa onda electromagnética.
Tanto el conductor interno como el externo tienen una resistencia finita, por lo que parte de la energía de la onda se pierde como calor debido al efecto Joule.
Aunque el coaxial es muy eficiente en contener la energía, existen pérdidas adicionales por el dieléctrico y pequeñas fugas de radiación, lo que provoca una atenuación mínima pero inevitable de la señal a lo largo del cable.

3. La transmisión por fibra óptica es actualmente una de las más eficientes. Ya que guía pulsos de luz (fotones) a través de un núcleo de vidrio o plástico con mínimas pérdidas. Sin embargo, la atenuación sigue existiendo.
A medida que el haz de luz avanza y se refleja internamente en las paredes del núcleo por reflexión total, una pequeñísima fracción de la energía se pierde en cada rebote debido a absorción en el material y a imperfecciones microscópicas.
Además, el material de la fibra no es perfectamente transparente. Ciertos átomos y enlaces químicos absorben parte de la energía de los fotones y las impurezas o irregularidades dispersan la luz en otras direcciones.
Estos procesos hacen que la potencia óptica disminuya gradualmente con la distancia, aunque a un ritmo mucho menor que en cables eléctricos o en enlaces inalámbricos.

