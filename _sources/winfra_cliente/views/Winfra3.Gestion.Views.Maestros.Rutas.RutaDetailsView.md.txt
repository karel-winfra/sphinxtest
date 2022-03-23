
# Configuración de la ruta

## Cabecera de la ruta

Campos para tener en cuenta de la cabecera de la ruta:

 * **Tipo ruta** distingue entre las rutas de venta y las rutas de reparto.
La ruta de tipo *Pendiente* sirve para poder crear una nueva ruta que el sistema no tiene en cuenta
y poder activarla cambiando su tipo.

Un punto de venta solo puede estar en una ruta de reparto con el mismo almacén y organización de venta.

 * **Cargar en PDA** indica que la ruta esta incluida en las cargas de dispositivos móvil

 * **Tarifa** indica la tarifa que se va a utilizar **SIEMPRE** para esta ruta.
La tarifa indicada prevalece sobre la configuración del cliente.

 * **Proveedor integración** indica si la ruta ha sido creada desde la integración de datos con algún proveedor

 * **Almacén** indica el almacén del cual saldrá la mercancía cuando se realicen ventas a los puntos de venta incluidos en la ruta. Solo opera en rutas de tipo geográfica


Por ejemplo la ruta nocturna indica la tarifa nocturna.
Al incluir el cliente en la ruta nocturna le aplicamos automáticamente esta tarifa aunque el cliente mismo esta configurado
con la tarifa normal.

## Configurar los puntos de venta de la ruta

La pestaña de **Elementos de la ruta** contiene dos lista
 * los puntos de venta incluidos en la ruta (a la izquierda)
 * resultados de la búsqueda de puntos de venta (a la derecha). Si un punto de venta ya esta en la ruta esta marcado en los resultados.

### Frecuencia de visita

Indica una frecuencia de visita de los clientes.
 * **Semanal** - visita cliente cada semana
 * **Semanas pares, Semanas impares** - visita cliente cada dos semanas
 * **Mensual 1., 2., 3., 4. semana** - visita cliente cada 4 semanas

 ! La frecuencia no esta basada en el numero de semana en el año actual.
Utilizar el numero de semana según el calendario ISO rompería la continuación al cambiar el año.
Un año con 53 semanas (2015, 2020) tiene la ultima impar y la siguiente es numero 1, también impar.

### Añadir y quitar los puntos de venta

Utiliza flechas situadas entre las dos listas para incluir y excluir los puntos de venta.

Utiliza botón **Quitar puntos de venta** para eliminar puntos de venta de la ruta pero seleccionando los entre los resultados de la búsqueda.
Esto permite, por ejemplo, quitar puntos de venta de una población filtrando por su dirección.

 * Abra la ruta de la que hay que quitar los puntos de venta
 * Busca la población ej. por código postal. Si ademas filtra la misma ruta solo verá los puntos de venta a quitar.

 ! rv:Ruta 2 Lunes d:46680

 * Los resultados incluidos están marcados
 * Selecciona los puntos de venta, puede seleccionar todos, los no incluidos en la ruta no se tienen en cuenta
 * Pincha botón **Quitar puntos de venta**


### Mover puntos de venta entre rutas

Mover los puntos de venta quita puntos de una ruta y los agrega a otra ruta.
Esto es especialmente útil para rutas de reparto que no permiten que cliente este en dos a la vez.

 * Abre la ruta de origen
 * Seleccione los puntos de venta
 * Pinchar botón **Traspasar**
 * Selecciona ruta de destino en el dialogo y pincha **Aceptar**

### Incluir puntos de venta de otra ruta

Copia los clientes a nueva ruta pero los mantiene en la original

 * Abre la ruta de destino
 * En el búsqueda busca los clientes de ruta de origen. Utiliza el parámetro de ruta (rv, rr, rp)

 ! rv:Ruta 2 Lunes

 * Los resultados de la búsqueda son ordenados por orden de ruta
 * Selecciona los puntos de venta y pincha la flecha para incluir

### Mantener orden de la ruta

Tiene varia alternativas para ordenar la ruta

 * Utilice botones **Mover arriba** y **Mover abajo**
 * Indica el orden en la columna **Orden**
 * Pincha botón **Reordenar** para aplicar el orden y recalcular la numeración
