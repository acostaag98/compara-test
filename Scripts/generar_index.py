import os
import json

# Ruta base donde están las compañías (desde la raíz del repositorio)
base_path = "Schema"

# Inicializamos el índice
index = {}

# Recorremos las carpetas de compañías
for company in os.listdir(base_path):
    company_path = os.path.join(base_path, company)
    outputs_path = os.path.join(company_path, "outputs")

    if os.path.isdir(outputs_path):
        product_files = [
            f for f in os.listdir(outputs_path)
            if f.startswith("producto_") and f.endswith(".json")
        ]
        if product_files:
            index[company] = product_files

# Guardamos el index.json en la raíz del proyecto
index_path = "index.json"
with open(index_path, "w", encoding="utf-8") as f:
    json.dump(index, f, indent=4, ensure_ascii=False)

print("index.json generado correctamente.")
