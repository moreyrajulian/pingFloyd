## Resumen punto 3


---
## Introducción punto 3


---
# Desarrollo 
## Actividad 3

### Objetivo

### Topologia
![Topo](topo.png)

### Diseño y Esquema de Direccionamiento IP
| NOMBRE | VLAN | RED IP | GATEWAY |
|-------|--------------|---------------------|---------------------------|
| Turista | 10 | 10.10.10.0/24 | 10.10.10.1 |
| Business | 20 | 10.10.20.0/24 | 10.10.20.1 |
| Servidor | 50 | 10.10.50.0/24 | 10.10.50.1 |
| Admin | 99 | 10.10.99.0/24 | 10.10.99.1 |

### Configuración de Nivel 2: Segmentación (Switch)

![Brief](brief.png)

![Trunk](trunk.png)


### Configuración de Nivel 3: Enrutamiento y Servicios (Router)

![BriefRouter](briefRouter.png)

![dhcp](dchp.png)

![PCAdmin](pcAdmin.png)

![Celu](celu.png)


### Implementación de Políticas de Seguridad (ACL y NAT)

![ACL](ACL.png)
![ACL y NAT](ACL_Y_NAT.png)



### Pruebas

**Caso 1: Host Turista (VLAN 10)**

![HostTurista](celu1.png)

**Caso 2: Host Business (VLAN 20)**
![HostBusiness](celu2.png)

**Caso 3: Host Admin (VLAN 99)**

![HostAdmin](admin.png)



---
## Conclusiones punto 3
