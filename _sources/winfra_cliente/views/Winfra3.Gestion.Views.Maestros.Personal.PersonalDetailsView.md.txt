title: Winfra3.Gestion.Views.Maestros.Personal.PersonalDetailsView.md
=== Configuración de la gestión de horarios

== Posibles acciones en función del tipo de personal para el que queramos calcular horarios

= Personal de administración (oficina)
    - Tipo de cálculo = Fijo
    - Se indican las horas de inicio y fin de cada turno.
    - Primer turno es por la mañana y segundo turno es por la tarde

= Personal comercial
    - Tipo de cálculo = Calcular sobre acción
    - Cálculo hora de inicio = Hora inicio tempómetro
    - Cálculo hora finalización = Hora finalización tempómetro
    - Posibles correcciones al tempómetro
        ○ Si indicamos Hora inicio jornada desde, se tendrá en cuenta el primer registro del tempómetro posterior a esta
        ○ Si indicamos Hora fin jornada desde, se tendrá en cuenta el último registro del tempómetro anterior a esta
        ○ Hora inicio jornada hasta y Hora fin jornada hasta, no se usan en este cálculo

= Personal de reparto
    - Tipo de cálculo = Calcular sobre acción
    - Cálculo hora inicio. Posibles valores
        ○ Hora inicio jornada = Hora inicio jornada desde que indiquemos
        ○ Hora inicio tempómetro de visitas = no se usa
        ○ Hora confirmación carga = Inicia cuando se confirma la hoja de carga
        ○ Hora inicio ruta = solo para reparto mecanizado, cuando ejecutan la acción de iniciar ruta
    - Cálculo hora finalización. Posibles valores
        ○ Hora retorno carga = hora en la que se hace el retorno de la hoja de carga
        ○ Hora liquidación tesorería = hora en que se asigna el operador de tesorería a la operación de tesorería
        ○ Hora liquidación reparto = hora en que se genera la liquidación de la hoja de entrada del reparto
        ○ Hora finalización tempómetro de visitas = no se usa
        ○ Hora finalización ruta = solo para reparto mecanizado, cuando ejecutan la acción de finalizar ruta
