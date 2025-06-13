# Documentación Técnica – Cardinal Assistance

## 1. Coberturas Detectadas

Se detectaron las siguientes categorías principales de cobertura en los productos Cardinal:
- Asistencia médica: enfermedad, accidente, COVID-19, embarazo, preexistencias, odontología, internación, etc.
- Cobertura hospitalaria: repatriaciones, acompañamiento, hotel post-hospitalización.
- Equipaje: demora, pérdida, daño, localización.
- Cancelaciones: vuelo, interrupción, cambio de fecha.
- Accidentes personales.
- Asistencia legal y fondos.
- Otros servicios: Wallet Assistance, traducción, transmisión de mensajes, etc.

## 2. Estructura del Schema

El `schema_cardinal.json` fue construido considerando todos los campos presentes al menos en un voucher. 
Sigue una estructura jerárquica que agrupa coberturas relacionadas bajo claves comunes como `asistencia_medica`, `equipaje`, `hospitalario`, etc.

## 3. Diferencias CCGG vs Vouchers

- **CCGG**: Define exclusiones generales, límite de edad, condiciones del servicio.
- **Vouchers**: Especifican los montos y detalles particulares por plan (por ejemplo, USD 17.000 para Internacional 17).

## 4. Reutilización con otras compañías

Para aplicar este mismo proceso:
1. Reemplazar archivos PDF en las carpetas correspondientes.
2. Reutilizar el `prompt_base.txt`.
3. Ejecutar el flujo automático de extracción y estructuración con el nuevo contenido.