
# Claves de las incidencias de la venta

La pantalla permite codificar las incidencias relacionadas con el documento de la venta.

Algunas incidencias se producen como consecuencia de otros procesos como **Rechazo** o **Anulación**.
Las incidencias tipo **Genérica** se pueden agregar manualmente en el documento de venta.

En todos los procesos el usuario puede hacer un comentario ademas de indicar la clave.

## Campos de las claves para tener en cuenta

 * **Referencia del fabricante** es una codificación de la incidencia para el proveedor/fabricante.
Esto se utiliza para indicar razones de anulación en las transmisiones de proveedores.
Hay que indicar el proveedor.
 * **Proveedor** indica que la incidencia se aplica a los documentos de intermediación.
Si no se ha indicado ningún proveedor la clave se aplica para todos los documentos sin intermediación
e intermediaciones de los proveedores que no tengan definidas las claves.
 * **Tipo** indica el proceso en cual se utiliza la incidencia.
Solo debería existir una clave de tipo **Rechazo**. Tiene que existir al menos una clave de **Anulación**.
 * **Acción** se aplica después de anulación.

### Acciones

Las acciones se aplican después de la anulación del documento.

 * **Ninguna** es la opción por defecto. El documento queda anulado.
 * **Duplicar** creara un nuevo documento con el mismo contenido.
 * **Repetir** marca la repetición del documento para la transmisión por el portal CCIP.
Esta opción solo hay que utilizarla junto con el proveedor CocaCola
