Category: Winfra3 Windows

# Monitor de auditoría

Permite configurar los filtros y envía avisos por email cuando ocurran eventos en la auditoría de winfra.

## Configuración de los envíos

 * Configurar cuenta de correo en la pantalla de las [c]cuentas|views/Winfra3.Gestion.Views.Maestros.MailConfigs.MailConfigMainView.txt[c]
 * Indica la cuenta de correo que quiere utilizar en datos generales **Configuración de correo para envío de los avisos del monitor auditoria**
 * Configura el proceso de **Monitor de auditoría** en el programador de las tareas.

## Configuración de los filtros

 * **Habilitado** - permite habilitar/deshabilitar el aviso
 * **Operación** - filtrar nombre de la operación
 * **Descripción** - filtrar por descripción
 * **Datos** - filtrar por datos
 * **Usuario** - filtrar por usuario

El aviso se envía si el registro cumple con todos los filtros indicados. Si el filtro esta vacío no opera.
Puede utilizar \* como comodín.

Tiene que indicar por lo menos un filtro.

 * **Email** - indica el email al que hay que enviar el informe. Puede indicar varios separados por punto-coma.
