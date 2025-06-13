# Documentación Técnica – Assist Card

## Resumen del Análisis

Se analizaron las Condiciones Generales (CCGG) y 7 vouchers de productos específicos emitidos por Assist Card.

### Productos procesados:
- AC 1 MILLON
- AC 35 Especial
- AC 60 (en sus variantes: Especial, Multiviaje, Larga Estadía, Receptivo)
- AC 150 Larga Estadía

---

## Estructura del Schema

El schema detectado agrupa las coberturas en las siguientes categorías:

- **Asistencia médica**: accidentes, enfermedades, COVID-19, preexistencias, embarazo, odontología, medicamentos.
- **Hospitalario**: traslados, repatriación, acompañamiento, estancia de familiar, gastos de hotel post hospitalización.
- **Equipaje**: demora y pérdida.
- **Cancelación de viaje**: por fuerza mayor, COVID-19, penalidad de regreso, safe passport.
- **Accidentes personales**: muerte accidental, invalidez, límites globales.
- **Asistencia legal**: reclamos, adelanto de fianzas.
- **Otros**: localización de equipaje, documentos, regreso anticipado, validez territorial, edad, días consecutivos.

---

## Diferencias entre CCGG y Vouchers

- **CCGG**: contiene definiciones generales, exclusiones y cláusulas legales.
- **Vouchers**: especifican los montos aplicables para cada producto, incluyendo detalles de cobertura particulares.

---

## Uso con otras compañías

Este mismo flujo puede repetirse de la siguiente forma:

1. Extraer texto de CCGG y vouchers.
2. Identificar coberturas por categoría.
3. Estandarizar los datos bajo el mismo schema.
4. Crear ejemplos completos.
5. Documentar diferencias clave y generar un prompt base.