
# Configuración de la sincronización

Configurar la conexión a otro dominio para traer la venta y sincronizar los maestros.


## Estadística de venta (modelo Leondis-Reycer)

 * D1 genera albarán o factura directa (una venta)
 * D2 recibe las ventas y genera documento estadístico

Documento estadístico no será asignable en preparación cargas para su reparto.
El caso de uso es D1 vende el producto de un proveedor a sus clientes
pero D2 tiene que transmitir esta información al proveedor.

En D2 el documento se generará como estadístico y no será asignable a
cargas pero si transmisible a proveedores.

D1 - SyncModoVentas=Ninguno

D2 - SyncModoVentas=Estadistica


## Venta externa (modelo Provea-Discamt)

 * D1 hace una venta pero genera documento estadístico
 * D2 recibe las ventas, genera albarán o factura directa para la entrega
 * D1 recibe las ventas modificadas y actualiza el documento original

El caso de uso es una empresa que vende los productos de otra pero no los reparte ni los factura.

El documento de venta cuando baja de la PDA se integra en Winfra como
documento estadístico que no se asigna a cargas ni se transmite a proveedores. Para eso todos los clientes tienen
que tener la condición de la venta del proveedor enlazado indicando **Albarán individual** y
**Documento de entrega = Documento estadístico**

D1 recibe y actualiza los documentos por si se han modificado en el reparto para tener información correcta para
comisiones de los vendedores.

D1 - SyncModoVentas=VentaExternaLiquidacion

D2 - SyncModoVentas=VentaExterna


## Reparto (modelo Sedinte-Dispegra)

 * D1 crea un pedido (o lo recibe desde el fabricante como Pepsi, Schweppes)
 * D2 recibe el pedido y genera **albaran de intermediacion de D1**
 * D1 recibe las ventas modificadas en el proceso de reparto y actualiza el documento original (convierte pedido a albarán/factura directa)

En el proveedor D1 y D2 sincronizamos la forma de pago a contado, el resto de formas de pago se integraran
como la forma de pago credito establecida en el proveedor D2.

D1 - SyncModoVentas=RepartoLiquidacion

D2 - SyncModoVentas=Reparto



## Intermediacion (modelo Blasco-Il-lusions)

 * D1 hace la venta y reparto, genera **albaranes de intermediación de D2**
 * D2 recibe la venta (bloqueada, liquidación cerrada) y genera albaranes y operación de cobro
 * D1 recibe la venta generada y crea albarán resumen de intermediaciones

En el proveedor D1 y D2 sincronizamos la forma de pago a contado, el resto de formas de pago se integraran
como la forma de pago credito establecida en el proveedor D2.

D1 - SyncModoVentas=IntermediacionLiquidacion

D2 - SyncModoVentas=Intermediacion



# Configuración de los proveedores

En **RepartoLiquidacion** y **Intermediacion** podemos generar la operación de cobro para documentos
con la forma de pago a contado:

 * indicar en los dos proveedores, local y externo las formas de pago de contado y crédito
 * en la sincronización de venta los documentos con forma de pago a contado del proveedor externo
indicamos forma de pago a contado del proveedor local
 * documentos a contado se añaden a una operación de tesorería como cobro



