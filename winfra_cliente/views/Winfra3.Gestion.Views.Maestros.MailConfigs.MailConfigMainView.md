title: Winfra3.Gestion.Views.Maestros.MailConfigs.MailConfigMainView.md
=== Configuración de las cuentas de correo

La pantalla permite configurar las cuentas que se van a utilizar para enviar el correo electrónico desde winfra.
La configuración de la cuenta la proporciona el proveedor del servicio de correo ej.: google, hotmail, outlook etc.

Puede configurar varias cuentas para diferenciar por ejemplo el envío de las facturas del envío de aviso de transmisiones.

Que cuenta se va utilizar para que propósito esta configurado en los datos generales.

== Parámetros de la cuenta

 * **Descripción** - descripcion para identificar las cuentas
 * **Correo origen** - correo electrónico que aparece en el campo "Desde:"
 * **Servidor** - nombre de servidor, normalmente un servidor SMTP como por ejemplo smtp.gmail.com
 * **Puerto** - puerto del servicio de correo ej.: 25, 587 etc.
 * **Encriptacion** - indica la encriptación que utiliza el servidor
 * **Usuario** - usuario utilizado a autenticar, puede coincidir con el correo de origen
 * **Contraseña** - por razones de seguridad una vez guardadas las cuentas la contraseña aparece como []*****[]
 * **Tiempo de espera** - Indica el tiempo de espera o deja el valor **0** para utilizar un valor por defecto.
 * **Emails por minuto** - Indica numero máximo de correos que se pueden enviar por minuto o 0 para indicar que no existe un limite.

 ! Utiliza el botón de **Enviar prueba** para validar al configuración de la cuenta.
