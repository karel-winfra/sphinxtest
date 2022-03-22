title: Ribera2.Printing.Views.MailSenderView.md
=== Envío de documentos por correo electrónico

La pantalla permite enviar por correo electrónico los documentos que se han impreso a una cola de winfra.
Cada documento esta adjunto al mensaje de correo como un fichero PDF. Es posible enviar todo tipo
de documentos ya sean albaranes, facturas o informes.

== Parámetros de la pantalla:

 * **Cola de impresión** - indica la cola de la que se van enviar los documentos
 * **Destinatario** - si esta marcada la opción de utilizar dirección indicada en el documento se envía a su dirección.
La impresión de los albaranes y de las facturas incluye la dirección de cliente indicada en **Mail facturación**.
Si desmarca la opción tiene que indicar la dirección y todos los documentos sean enviados a la dirección indicada.
Puede indicar mas que una dirección separadas por coma o punto-coma.

 * **Asunto** - si esta marcada la opción de utilizar el asunto indicado en el documento el envío utiliza la descripción
del documento como asunto del mensaje. Si desmarca la opción tiene que indicar un asunto.

 * **Mensaje** - el texto del mensaje
 * **Pie del mensaje** - pie del mensaje esta incluido al final del mensaje. A diferencia del mensaje el pie se guarda al lanzar
el envío.

== Configuración del servidor de correo

El envío necesita la configuración del servidor de correo. La configuración esta en los **Datos generales** en el apartado
**Envío documentos por correo electrónico**.
Contacta con su proveedor de correo si desconoce la configuración de su servidor.

== Control de los errores

Una vez el documento esta enviado se elimina de la cola. Si ocurre un error durante del envío el documento
se queda en la cola indicando el error. Es posible revisar los errores en la pantalla de trabajos de impresión.
Si el error es intermitente, por ejemplo un fallo de conexión a internet, es posible reiniciar el estado del
trabajo y luego volver a iniciar el envío.

Si el error esta en el propio documento, por ejemplo la dirección de correo de cliente no es válida, tendrá modificar
el correo y volver a imprimir.

 ! La pantalla de impresión masiva de albaranes y facturas permite filtrar los documentos enviados.

== Colas para el envío

Es posible utilizar cualquier colo de impresión para el envío de correo, pero es posible lanzar solo un envío por cada cola.
Si necesita que varios usuarios envíen correos a la vez hay que crear una cola para cada uno.

 !! En el caso de impresión de documentos de venta el perfil utilizado tiene que tener el **Tamaño de lote** igual a **1**.
