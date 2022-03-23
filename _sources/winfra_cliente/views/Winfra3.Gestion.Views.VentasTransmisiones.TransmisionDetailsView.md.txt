
# Perfil de transmisión

Permite configurar el envío y recepción de los datos a los proveedores

 * **Tipo** identifica el modulo de comunicación
 * **Proveedor** indica el proveedor

## Datos generales

Datos de configuración del modulo de transmisión. Los datos dependen del tipo de transmisión seleccionada.

## Datos control

 * **Transmisión automática** marca la opción para enviar los datos en una transmisión automática por la noche
```{warning}
No todos los proveedores tienen la opción de envío automático.
```
 * **Días de la semana** indica los días en las que se va ejecutar el envío automático
 * **Días del mes** indica días del mes en los que se va ejecutar el envío automático.
 Acepta varios días separados por coma ej.: 10, 20, 31. Si el mes no tiene día 31 se ejecutara el último día del mes.

```{note}
Si no indica ningún día de la semana ni del mes se va transmitir todos los días.
```

 * **Control estados venta** - Controlaremos si hay ventas en el periodo que se queden fuera por el estado del documento.
 Si esta marcado avisa si hay, por ejemplo, un documento en el estado de carga entre las fechas que hay que transmitir.
