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

## Introducción

## Desarrollo

## Actividad 1

## Actividad 2

## Actividad 3

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


