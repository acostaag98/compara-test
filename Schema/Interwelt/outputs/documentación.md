# Documentación Técnica – Interwelt

## Productos Procesados:
- Aventura 17
- Estelar Europa
- Y otros 6 vouchers más.

## Campos detectados en el schema
- Asistencia médica: enfermedad, accidente, COVID-19, embarazo, preexistencias, internación, medicamentos, odontología, etc.
- Hospitalización: traslados, repatriaciones, acompañamiento, hotel post alta.
- Equipaje: demora, pérdida, localización.
- Cancelación de viaje: COVID, eventos, interrupción.
- Accidentes personales: muerte accidental, invalidez.
- Asistencia legal: fianza, abogados.
- Otros: transmisión de mensajes, consultas, límites de edad y días.

## Diferencias entre CCGG y vouchers
- El CCGG define cláusulas generales, territorios y exclusiones.
- Los vouchers especifican montos aplicables por plan y destino.

## Cómo usar este flujo con otras compañías
1. Cargar PDF de CCGG + vouchers.
2. Extraer texto, construir `schema` base.
3. Crear ejemplos estructurados de productos.
4. Documentar y generar prompt base reutilizable.