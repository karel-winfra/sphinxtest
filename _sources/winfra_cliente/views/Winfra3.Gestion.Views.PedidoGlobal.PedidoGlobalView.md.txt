title: Winfra3.Gestion.Views.PedidoGlobal.PedidoGlobalView.md
=== Pedido global

Pedido global representa un pedido que se va a servir en varias entregas,
posiblemente a varias direcciones y se va a facturar en una o varias facturas
posiblemente a diferentes clientes.

Pedido global permite controlar el total del pedido, cantidades entregadas y
facturadas y posibles discrepancias.

== Configuración del pedido global

La configuración se aplica al generar las entregas y las facturas. Si los documentos ya estan generados
hay que modificarlos manualmente.

Los valores por defecto de la configuración se pueden configurar en *Datos de tipo documento*,
apartado de *Pedido global*.

= Tipo

Existen dos tipos de pedido global:
 * **Pedido** - las entregas hay que generarlas manualmente desde la pantalla de
pedido global
 * **Contrato** - las entregas se generan automaticamente desde las descargas de
venta móvil hasta agotar la cantidad pedida. Es posible generar la entrega manualmente
igual como en caso de pedido.

= Gestión de envases

Existen tres modos de gestionar los envases:
 * **No cargar envase** - el envase no se carga ni en la factura ni en la entrega
 * **Facturar envases, no cargar en la entrega** - los envases se cargar en la factura
y no se incluyen en las entregas. Las devoluciones hay que abonarlas en otro documento.
 * **Cargar entrega en documento aparte, no facturar** - no se carga el envase en la factura.
Junto con cada entrega se genera un documento valorado de envases. Las devoluciones hay que
abonarlas en el mismo documento.

 !! Si el cliente seleccionado tiene marcado **No se cargan los envase** la gestión de envases cambia
automaticamente a **No cargar envase**.

= Entregas valoradas

Si la opción esta marcada los albaranes de entrega se imprimirán valorados.
Al desmarcar la opción la impresión solo incluye el artículo y la cantidad.
 ! La opción solo es aplicable al tipo pedido, las entregas de contratos no se valoran.

== Detalles

Indica los artículos y cantidades pedidas. La campaña y el valor del descuento es opcional.
El valor de descuento se corresponde al tipo de calculo de la campaña. Si la campaña es de tipo
**Porcentaje** el valor tiene que ser el porcentaje aplicado etc.

El descuento se aplican a las lineas de las entregas y de las facturas. Si no se ha indicado ningún descuento
aplicamos las condiciones vigentes del cliente.

El uso de la campaña de tipo regalo o promoción tiene varias limitaciones:
 * En caso de pedido solo se pueden generar la factura una vez se han generado todas las entregas.
 * Las notas de entregas no reflejan el regalo (en el caso que se imprimen valoradas).

== Entregas

Las entregas se generan en dos pasos:
 * Entrega del pedido global - indica la dirección de entrega, artículos y cantidades entregadas
 * Nota de entrega - un albarán de tipo **Nota de entrega** asociado a la entrega de pedido global
que se genera automaticamente apartir de su cabecera y líneas.

En el caso de generar las entregas de un pedido de tipo **Contrato** en el proceso automático de la descarga de las
ventas móvil generamos los dos documentos a la vez.

= Agregar entrega directa

La operación genera una entrega del pedido global con el destinatario igual al cliente del pedido.
La cantidad entregada es lo que queda por entregar.

= Agregar entrega manual

La operación crea un nueva entrega vacía. Hay que indicar el destinatario y las cantidades manualmente.

 ! Para generar la **nota de entrega** utiliza la operación **Generar albarán** de la pantalla de la entrega
o de la pantalla **Entregas globales**

== Facturas

Generación de las facturas crea un documento de venta de tipo **factura directa global** asociado con el pedido global.

= Facturar

La operación genera la factura con la fecha y cliente indicado. Las cantidades facturadas varían según el tipo de pedido
global.
 * En caso de pedido facturamos todos los artículos entregados que no estén facturados.
Para contar como entregado no hace falta generar la **nota de entrega** (albarán)
 * En caso de contrato facturamos todos los artículos pedidos que no estén facturados.

= Factura vacía

La operación genera una factura vacía enlazada con el pedido global con el fin de poder indicar manualmente las cantidades.
Por ejemplo en caso de las devoluciones.
