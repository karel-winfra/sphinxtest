
# Integración con SAP

La pantalla permite ejecutar y revisar la integración de la contabilidad con los servicio web
del SAP BO.

## Procesos

 * Pre-validar las ventas, compras, facturas globales y el resto de contabilidad para generar
registros que enlazaran el documento de winfra con el documento de SAP
 * Revisar posibles errores de la pre-validación y volver a pre-validar
 * Enviar a SAP

## Estados de los registros

 * **Pendiente** - el registro ha sido pre-validado y esta pendiente de de enviar
 * **PendienteAviso** - pre-validado con algún aviso (no hay que hacer nada) - ej.: se va a dar de alta el cliente
 * **PendienteError** - pre-validado pero hay algún problema que hay que solucionar - ej.: hay que de alta el proveedor
 * **Correcto** - esta integrado en SAP correctamente
 * **Revisar** - esta integrado en SAP, pero hay algún problema ej.: no coinciden los totales
 * **Error** - la integración en SAP ha fallado

Ademas de los estados el registro puede bloquear el envío (indica una cerradura).

## Notas

El proceso de envió solo envía registros pre-validados **Pendiente** y **PendienteAviso**
en el orden de serie/numero y finaliza en el primer registro **PendienteError** o **Error** o en un registro bloqueado.
No continua después de error para no crear huecos en las series de SAP.

El bloqueo de envío aparece si existen huecos en la numeración de los documentos pendientes. Ej. Si el ultimo documento
enviado es de viernes y a continuación pre-validamos el lunes, el primer documento de lunes estará bloqueado si hay también
venta en sábado. Hay que pre-validar sábado para desbloquear el envío.

En caso de **PendienteError** hay que arreglar el error (ej. dar de alta el proveedor) y volver a pre-validar los registros.
Si el problema esta en Winfra y hay que modificar cliente/venta etc.
Hay que eliminar el registro primero (esta protegido para evitar modificación) y luego volver a pre-validar.

Los errores es posible tirar atrás y volver a enviar con el botón **Marcar pendiente**.

Los registros **Revisar** es posible pasar a **Correcto** con el botón **Marcar correcto**

Los registros **Correcto** no salen por defecto en la pantalla. Para verlos hay que filtrar todos los estados e:\*
