# SQl Reader
lee cualquier archivo SQL que reciba, si contiene instrucciones para crear tablas, las analiza y las muestra en un HTML, además de mostrar las relaciones existentes entre estas.

## Estructura del archivo
está es la estructura que debe tener al definir una tabla y lo que tomará en cuenta, puede evitar los espacios en blanco entonces no es tan importante eso.
``` sql
create table Tabla1(
    PrimaryKey int primary key, // puede detectar cual es la PK
    nombre varchar(40)
)
```

y así puedes seguir añadiendo el numero de tablas que desees. Esta tabla será mostrada en el HTML así:
| PrimaryKey (PK) | nombre |
| ---------- | ------ |
| int        | varchar(40) |

