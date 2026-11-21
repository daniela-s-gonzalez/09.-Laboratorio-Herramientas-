# Databricks notebook source
# DBTITLE 1,Título y Descripción del Notebook
# MAGIC %md
# MAGIC # 🔧 Setup y Verificación de Entorno
# MAGIC ## Laboratorio (Herramientas) - Universidad del Aconcagua
# MAGIC
# MAGIC Este notebook verifica que el entorno de Databricks esté correctamente configurado para el curso. Ejecuta todas las celdas en orden antes de comenzar cualquier Trabajo Práctico.
# MAGIC
# MAGIC **Uso**: Ejecuta todas las celdas secuencialmente. Si todas las verificaciones muestran ✅, el entorno está listo.

# COMMAND ----------

# DBTITLE 1,Sección 1 - Librerías Base
# MAGIC %md
# MAGIC ## 📦 1. Verificación de Librerías Base
# MAGIC
# MAGIC Las siguientes librerías son necesarias para los Trabajos Prácticos del curso:

# COMMAND ----------

# DBTITLE 1,Verificar Librerías Base
import importlib
import sys

librerias_base = {
    "pandas": "Manipulación de datos",
    "numpy": "Computación numérica",
    "plotly": "Visualizaciones interactivas (Plotly Express)",
    "sklearn": "Machine Learning (Scikit-learn)",
}

print("=" * 60)
print("📦 VERIFICACIÓN DE LIBRERÍAS BASE")
print("=" * 60)

todas_ok = True
for lib, desc in librerias_base.items():
    try:
        mod = importlib.import_module(lib)
        version = getattr(mod, "__version__", "N/A")
        print(f"  ✅ {lib:<15} v{version:<10} - {desc}")
    except ImportError:
        print(f"  ❌ {lib:<15} NO INSTALADO    - {desc}")
        todas_ok = False

print(f"\n{'✅ Todas las librerías base están instaladas' if todas_ok else '⚠️ Faltan librerías base. Ejecuta: %pip install <lib>'} ")

# COMMAND ----------

# DBTITLE 1,Sección 2 - Librerías Avanzadas
# MAGIC %md
# MAGIC ## 🚀 2. Verificación de Librerías Avanzadas (Material Complementario)
# MAGIC
# MAGIC Estas librerías son necesarias solo para el material complementario y avanzado:

# COMMAND ----------

# DBTITLE 1,Verificar Librerías Avanzadas
librerias_avanzadas = {
    "optuna": "Optimización de hiperparámetros",
    "h3": "Análisis geoespacial (H3)",
    "folium": "Mapas interactivos",
    "tensorflow": "Redes neuronales (Keras)",
    "mlflow": "Tracking de experimentos",
    "shap": "Interpretabilidad de modelos",
}

print("=" * 60)
print("🚀 VERIFICACIÓN DE LIBRERÍAS AVANZADAS")
print("=" * 60)

avanzadas_ok = {}
for lib, desc in librerias_avanzadas.items():
    try:
        mod = importlib.import_module(lib)
        version = getattr(mod, "__version__", "N/A")
        print(f"  ✅ {lib:<15} v{version:<10} - {desc}")
        avanzadas_ok[lib] = True
    except ImportError:
        print(f"  ⚠️ {lib:<15} NO INSTALADO    - {desc}")
        avanzadas_ok[lib] = False

faltantes = [lib for lib, ok in avanzadas_ok.items() if not ok]
if faltantes:
    print(f"\n⚠️ Librerías faltantes: {', '.join(faltantes)}")
    print("   Instalar con: %pip install " + " ".join(faltantes))
    print("   Estas librerías son OPCIONALES para el curso base.")
else:
    print("\n✅ Todas las librerías avanzadas están instaladas.")

# COMMAND ----------

# DBTITLE 1,Sección 3 - Datasets CSV
# MAGIC %md
# MAGIC ## 📂 3. Verificación de Datasets CSV
# MAGIC
# MAGIC Verifica que los archivos CSV del curso estén accesibles:

# COMMAND ----------

# DBTITLE 1,Verificar Datasets CSV
import os

datasets_path = "/Workspace/Users/cortega@uda.edu.ar/Laboratorio/05 - Datasets"

datasets_esperados = {
    "productos.csv": (45, "productos de panadería"),
    "clientes.csv": (500, "clientes con geolocalización"),
    "sucursales.csv": (3, "sucursales"),
    "ventas.csv": (55986, "transacciones de ventas"),
    "detalles_ventas.csv": (113523, "líneas de detalle"),
}

print("=" * 60)
print("📂 VERIFICACIÓN DE DATASETS CSV")
print("=" * 60)

csv_ok = True
for archivo, (filas_esperadas, desc) in datasets_esperados.items():
    path = os.path.join(datasets_path, archivo)
    if os.path.exists(path):
        size_kb = os.path.getsize(path) / 1024
        # Contar líneas reales
        with open(path, 'r') as f:
            num_lineas = sum(1 for _ in f) - 1  # Restar header
        estado = "✅" if num_lineas == filas_esperadas else "⚠️"
        print(f"  {estado} {archivo:<25} {num_lineas:>7,} filas ({size_kb:>8.1f} KB) - {desc}")
        if num_lineas != filas_esperadas:
            print(f"     Esperadas: {filas_esperadas:,}, Encontradas: {num_lineas:,}")
    else:
        print(f"  ❌ {archivo:<25} NO ENCONTRADO")
        csv_ok = False

print(f"\n{'✅ Todos los datasets CSV están disponibles' if csv_ok else '❌ Faltan datasets. Ejecuta el notebook Generador de Datos.'} ")

# COMMAND ----------

# DBTITLE 1,Sección 4 - Unity Catalog
# MAGIC %md
# MAGIC ## 🗄️ 4. Verificación de Tablas en Unity Catalog
# MAGIC
# MAGIC Verifica que las tablas del curso estén disponibles en `workspace.panaderia`:

# COMMAND ----------

# DBTITLE 1,Verificar Tablas en Unity Catalog
print("=" * 60)
print("🗄️ VERIFICACIÓN DE TABLAS EN UNITY CATALOG")
print("=" * 60)

tablas_esperadas = {
    "productos": 45,
    "clientes": 500,
    "sucursales": 3,
    "ventas": 55986,
    "detalles_ventas": 113523,
}

uc_ok = True
for tabla, filas_esperadas in tablas_esperadas.items():
    try:
        resultado = spark.sql(f"SELECT COUNT(*) as cnt FROM workspace.panaderia.{tabla}").collect()
        filas_reales = resultado[0].cnt
        estado = "✅" if filas_reales == filas_esperadas else "⚠️"
        print(f"  {estado} workspace.panaderia.{tabla:<20} {filas_reales:>7,} filas")
    except Exception as e:
        print(f"  ❌ workspace.panaderia.{tabla:<20} NO DISPONIBLE")
        uc_ok = False

if uc_ok:
    print("\n✅ Todas las tablas de Unity Catalog están disponibles.")
    print("   Puedes usar consultas SQL directas: SELECT * FROM workspace.panaderia.ventas LIMIT 10")
else:
    print("\n⚠️ Las tablas de Unity Catalog no están disponibles.")
    print("   Carga los datasets ejecutando el notebook Generador de Datos o usa los CSVs directamente.")

# COMMAND ----------

# DBTITLE 1,Sección 5 - Spark y Compute
# MAGIC %md
# MAGIC ## ⚡ 5. Verificación de Spark y Compute

# COMMAND ----------

# DBTITLE 1,Verificar Spark y Compute
print("=" * 60)
print("⚡ VERIFICACIÓN DE SPARK Y COMPUTE")
print("=" * 60)

# Versión de Spark
print(f"  ✅ Spark versión: {spark.version}")

# Versión de Databricks Runtime
try:
    db_version = spark.sql("SELECT version()").collect()[0][0]
    print(f"  ✅ Databricks Runtime: {db_version}")
except:
    pass

# Información del cluster
print(f"  ✅ Modo compute: {'Serverless' if 'serverless' in str(spark.conf.getAll()).lower() else 'Cluster'}")

# Test de query simple
try:
    resultado = spark.sql("SELECT 1 as test").collect()
    print(f"  ✅ Query de prueba: OK")
except:
    print(f"  ❌ Query de prueba: FALLÓ")

# COMMAND ----------

# DBTITLE 1,Resumen Final
# MAGIC %md
# MAGIC ## 📋 6. Resumen Final
# MAGIC
# MAGIC Si todas las verificaciones muestran ✅, el entorno está listo para comenzar los Trabajos Prácticos.
# MAGIC
# MAGIC | Verificación | Estado |
# MAGIC |---|---|
# MAGIC | Librerías base | Revisar celda 3 |
# MAGIC | Librerías avanzadas | Revisar celda 5 |
# MAGIC | Datasets CSV | Revisar celda 7 |
# MAGIC | Tablas Unity Catalog | Revisar celda 9 |
# MAGIC | Spark y Compute | Revisar celda 11 |
# MAGIC
# MAGIC > **💡 Nota**: Las librerías avanzadas son opcionales para el curso base. Solo se necesitan para el material complementario y avanzado.

# COMMAND ----------

# DBTITLE 1,Resumen Automático del Entorno
print("=" * 60)
print("📋 RESUMEN FINAL DEL ENTORNO")
print("=" * 60)

print(f"""
  📦 Librerías base:     {'✅ OK' if todas_ok else '❌ Faltan librerías'}
  🚀 Librerías avanzadas: {sum(avanzadas_ok.values())}/6 instaladas
  📂 Datasets CSV:       {'✅ OK' if csv_ok else '❌ Faltan archivos'}
  🗄️ Unity Catalog:     {'✅ OK' if uc_ok else '⚠️ No disponible (usar CSVs)'}
  ⚡ Spark:              ✅ Funcionando
""")

if todas_ok and csv_ok:
    print("🎉 ¡Entorno listo! Puedes comenzar con TP01 - Configuración Cloud y Almacenamiento.")
else:
    print("⚠️ Revisa los elementos marcados con ❌ antes de continuar.")