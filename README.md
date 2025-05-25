# sistema-vigilancia-mayores
sistema de vigilancia para adultos mayores y personas con alzheimer
#autores: Kevin, Daniel y David
#tabla de eventos
| ID                  | Nombre                 | Criterios principales                         | Prioridad |
| ------------------- | ---------------------- | --------------------------------------------- | --------- |
| `caida_suelo`       | Caída al suelo         | Cambio bbox vertical→horizontal + suelo ≥ 3 s | Alta      |
| `salida_casa`       | Salida no autorizada   | Cruce zona puerta > 2 s fuera de 08:00–20:00  | Media     |
| `inactividad_larga` | Inactividad prolongada | Sin movimiento > 300 s                        | Media     |

