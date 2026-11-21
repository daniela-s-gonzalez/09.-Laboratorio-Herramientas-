# 📚 Material Avanzado - Laboratorio (Herramientas)

## 🎯 Propósito

Material avanzado complementario para profundizar temas del curso principal de **Laboratorio (Herramientas)** en la **Licenciatura en Analítica de Negocios** de la Universidad del Aconcagua.

Este contenido está diseñado para:
- 🚀 Estudiantes que quieren ir más allá del programa base
- 💡 Profundizar conceptos de ML y optimización
- 🛠️ Aprender herramientas modernas de la industria
- 📊 Aplicar técnicas avanzadas con el dataset de la panadería

---

## 🏗️ Estructura

Cada módulo incluye:
- **📖 Notebook de Teoría**: Fundamentos conceptuales, comparaciones, mejores prácticas
- **💻 Notebook Práctico**: Ejercicios hands-on con datasets reales del curso
- **🎓 Integración**: Conexión con contenido del curso principal (features H3, pipeline Medallion)

---

## ✅ Módulos Completos

### 01. Optimización de Hiperparámetros con Optuna

**📊 Estadísticas**: 2 notebooks, 31 celdas, ~4 horas de material

**Teoría** (`Teoría - Optimización de Hiperparámetros con Optuna.ipynb`):
- ¿Qué son los hiperparámetros? Diferencia con parámetros
- Métodos tradicionales: Grid Search vs Random Search
- Introducción a Optuna (búsqueda bayesiana con TPE)
- Visualizaciones interactivas (historia, importancia, slice plots)
- Técnicas avanzadas: Pruning automático, paralelización, persistencia
- Mejores prácticas y cuándo usar cada método

**Práctica** (`Práctica - Optimización con Optuna.ipynb`):
- **Ejercicio 1**: Optimizar Gradient Boosting Regressor
  - Configuración de hiperparámetros
  - Validación cruzada
  - Comparación con Random Forest
  
- **Ejercicio 2**: Optimización multi-objetivo
  - Trade-off entre precisión (MAE) y velocidad
  - Pareto front
  - Selección según prioridades de negocio

- **Ejercicio 3**: Persistencia en base de datos
  - Storage con SQLite
  - Reanudar optimizaciones interrumpidas
  - Compartir estudios entre equipos

- **Ejercicio 4**: Features geoespaciales H3
  - Agregar features espaciales (dist_sucursal_min, densidad_zona, facturacion_zona)
  - Re-optimizar modelo con features ampliadas
  - Feature importance de variables espaciales

**🎯 Objetivos de Aprendizaje**:
- ✅ Entender diferencia entre parámetros e hiperparámetros
- ✅ Optimizar modelos de forma eficiente vs. Grid/Random Search
- ✅ Aplicar pruning para ahorrar tiempo de cómputo
- ✅ Visualizar proceso de optimización
- ✅ Integrar features espaciales H3 en workflows de ML

**📦 Librerías Requeridas**:
```python
optuna==3.5.0
h3==4.0.0b5
scikit-learn
pandas
numpy
plotly
```

**🔗 Conexión con el Curso**:
- Relacionado con **Unidad 3 (Modelado de Datos)** - Feature Engineering
- Usa datasets de la panadería del curso principal
- Integra features geoespaciales H3 de TP04-TP08

---

## ✅ Módulos Completos

### 02. Validación Cruzada Avanzada

**📊 Estadísticas**: 2 notebooks, ~4 horas de material

**Teoría** (`Teoría - Validación Cruzada Avanzada.ipynb`):
- K-Fold, Stratified K-Fold, Group K-Fold, Leave-One-Out CV
- Time Series Cross-Validation (sin data leakage temporal)
- Validación espacial con H3 (bloqueo geográfico)
- Comparación de estrategias y cuándo usar cada una

**Práctica** (`Práctica - Validación Cruzada Avanzada.ipynb`):
- Aplicar CV estratificada y temporal sobre dataset de panadería
- Comparar resultados entre estrategias
- Validación espacial usando H3

**🔗 Conexión con el Curso**: Unidad 3 (Modelado de Datos) - Evaluación de Modelos

---

### 03. Selección de Características

**📊 Estadísticas**: 2 notebooks, ~3 horas de material

**Teoría** (`Teoría - Selección de Características.ipynb`):
- Filter methods (correlación, chi-cuadrado, mutual information)
- Wrapper methods (RFE, forward/backward selection)
- Embedded methods (Lasso, Ridge, tree-based importance)
- SHAP para selección de features
- Selección de features espaciales (H3)

**Práctica** (`Práctica - Selección de Características.ipynb`):
- Aplicar Filter/Wrapper/Embedded sobre dataset de panadería
- Comparar subsets de features seleccionados
- Integrar features espaciales H3 en la selección

**🔗 Conexión con el Curso**: Unidad 3 (Modelado de Datos) - Feature Engineering

---

### 04. Interpretabilidad de Modelos

**📊 Estadísticas**: 2 notebooks, ~4 horas de material

**Teoría** (`Teoria - Interpretabilidad de Modelos.ipynb`):
- SHAP (SHapley Additive exPlanations): global y local
- LIME (Local Interpretable Model-agnostic Explanations)
- Partial Dependence Plots (PDP) e Individual Conditional Expectation (ICE)
- Permutation Feature Importance
- Interpretabilidad espacial con H3

**Práctica** (`Practica - Interpretabilidad de Modelos.ipynb`):
- Explicar predicciones de modelos con SHAP
- Visualizar importancia global y local
- Analizar impacto de features espaciales

**🔗 Conexión con el Curso**: Unidad 4 (Proyectos Integradores)

---

### 05. AutoML y Feature Store

**📊 Estadísticas**: 2 notebooks, ~4 horas de material

**Teoría** (`Teoría - AutoML y Feature Store.ipynb`):
- AutoML: H2O.ai, PyCaret, comparación de enfoques
- Databricks Feature Store: concepto y arquitectura
- Integración Feature Store + MLflow
- Feature Engineering automatizado

**Práctica** (`Práctica - AutoML y Feature Store.ipynb`):
- Aplicar AutoML para benchmarking rápido
- Configurar Feature Store con features del dataset
- Integrar con MLflow para tracking

**🔗 Conexión con el Curso**: Unidad 3-4 (Modelado y Pipelines)

---

### 06. MLflow Tracking y Model Registry

**📊 Estadísticas**: 2 notebooks, ~4 horas de material

**Teoría** (`Teoría - MLflow Tracking.ipynb`):
- Logging de parámetros, métricas y artefactos
- Comparación de runs y experimentos
- Model Registry: versionamiento y stages (Staging/Production/Archived)
- Deployment y serving de modelos
- A/B testing de modelos en producción

**Práctica** (`Práctica - MLflow Tracking.ipynb`):
- Trackear experimentos de modelos de panadería
- Registrar y versionar modelos en Model Registry
- Comparar métricas entre runs
- Configurar stages de deployment

**🔗 Conexión con el Curso**: Unidad 4 (Proyectos Integradores) - Pipelines de Producción

---

## 🚀 Cómo Usar Este Material

### Requisitos Previos
- ✅ Completar **Unidad 1 y 2** del curso principal
- ✅ Familiaridad con Python, Pandas y scikit-learn
- ✅ Haber trabajado con el dataset de la panadería

### Orden Sugerido
1. **Después de Unidad 3**: Módulos 01, 02, 03
2. **Después de TP07-TP08**: Módulos 04, 05, 06

### Recomendaciones
- 📖 **Leer teoría primero** antes de ejercicios prácticos
- 💻 **Ejecutar todas las celdas** para ver resultados
- 🔬 **Experimentar** modificando hiperparámetros
- 📊 **Analizar visualizaciones** para entender procesos
- 🎯 **Completar ejercicios** propuestos en cada notebook

---

## 🎓 Objetivos Generales del Material Complementario

Al completar estos módulos, los estudiantes serán capaces de:

✅ **Optimización Avanzada**:
- Configurar búsquedas de hiperparámetros eficientes
- Aplicar técnicas modernas (Optuna, AutoML)
- Balancear precisión, velocidad y recursos

✅ **Validación Robusta**:
- Seleccionar métodos de validación apropiados
- Evitar data leakage
- Validar modelos temporales y espaciales

✅ **Feature Engineering Inteligente**:
- Seleccionar features automáticamente
- Evaluar importancia de variables
- Incorporar información espacial/temporal

✅ **Interpretabilidad**:
- Explicar predicciones de modelos complejos
- Comunicar resultados a stakeholders no técnicos
- Cumplir requisitos de transparencia

✅ **MLOps y Producción**:
- Tracking de experimentos con MLflow
- Versionamiento de modelos
- Deployment y monitoreo

---

## 📊 Dataset

Este material complementario usa los **mismos datasets** del curso principal:
- `ventas.csv`: Transacciones de panadería (55,986 registros)
- `clientes.csv`: Información de clientes con H3 geoespacial (500 clientes)
- `productos.csv`: Catálogo de productos (45 productos)
- `sucursales.csv`: Ubicaciones con H3 (3 sucursales)
- `detalles_ventas.csv`: Ítems de cada transacción (113,523 líneas)

**Ubicación archivos CSV**: `/Workspace/Users/cortega@uda.edu.ar/Laboratorio/05 - Datasets/`

**Tablas en Unity Catalog**: `workspace.panaderia` (productos, clientes, sucursales, ventas, detalles_ventas)

---

## 🛠️ Tecnologías Adicionales

Además de las herramientas del curso base, este material introduce:

| Herramienta | Uso | Módulo |
|-------------|-----|--------|
| **Optuna** | Optimización de hiperparámetros | 01 |
| **SHAP** | Interpretabilidad de modelos | 03, 04 |
| **LIME** | Explicaciones locales | 04 |
| **H2O.ai** | AutoML | 05 |
| **PyCaret** | AutoML low-code | 05 |
| **MLflow** | Tracking y registry | 06 |

---

## 📖 Orden de Estudio Recomendado

### Track 1: Machine Learning Avanzado
1. **Módulo 01**: Optimización de Hiperparámetros ← ✅ **EMPEZAR AQUÍ**
2. **Módulo 02**: Validación Cruzada Avanzada
3. **Módulo 03**: Selección de Características
4. **Módulo 05**: AutoML y Feature Store

### Track 2: Interpretabilidad y MLOps
1. **Módulo 04**: Interpretabilidad de Modelos
2. **Módulo 06**: MLflow Tracking y Model Registry

### Track Completo (Recomendado)
Seguir el orden numérico de los módulos (01 → 02 → 03 → 04 → 05 → 06)

---

## 🎯 Conexiones con el Curso Principal

| Módulo Complementario | Unidad del Curso | Tema Relacionado |
|----------------------|------------------|------------------|
| 01 - Optuna | Unidad 3 | Feature Engineering y Modelado |
| 02 - Validación CV | Unidad 3 | Evaluación de Modelos |
| 03 - Selección Features | Unidad 3 | Feature Engineering |
| 04 - Interpretabilidad | Unidad 4 | Proyectos Integradores |
| 05 - AutoML | Unidad 3-4 | Modelado y Pipelines |
| 06 - MLflow | Unidad 4 | Pipelines de Producción |

---

## ✅ Criterios de Éxito

Has completado exitosamente este material complementario cuando puedas:

- [ ] Optimizar hiperparámetros con Optuna en <5 minutos
- [ ] Explicar diferencias entre Grid Search, Random Search y Optuna
- [ ] Aplicar validación cruzada apropiada según tipo de datos
- [ ] Seleccionar features automáticamente con métodos justificados
- [ ] Interpretar predicciones de modelos usando SHAP/LIME
- [ ] Configurar AutoML para benchmarking rápido
- [ ] Trackear experimentos con MLflow
- [ ] Versionar y deployar modelos en producción

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Optuna](https://optuna.readthedocs.io/)
- [SHAP](https://shap.readthedocs.io/)
- [H2O.ai](https://docs.h2o.ai/)
- [PyCaret](https://pycaret.gitbook.io/)
- [MLflow](https://mlflow.org/docs/latest/)

### Papers y Referencias
- "Optuna: A Next-generation Hyperparameter Optimization Framework" (2019)
- "A Unified Approach to Interpreting Model Predictions" (SHAP paper)
- Kaggle competitions best practices

### Cursos Relacionados
- Databricks Academy: Machine Learning
- Fast.ai: Practical Deep Learning
- Coursera: MLOps Specialization

---

## 💡 Contribuciones

Si tienes ideas para nuevos módulos o mejoras:
1. Contactar a: cortega@uda.edu.ar
2. Proponer temas relacionados con las unidades del curso
3. Sugerir ejercicios prácticos con el dataset de la panadería

---

## 📧 Contacto

**Profesor**: Cristian Dario Ortega Yubro  
**Email**: cortega@uda.edu.ar  
**Universidad**: Universidad del Aconcagua  
**Ubicación**: Mendoza, Argentina  
**GitHub**: [@cristiandarioortegayubro](https://github.com/cristiandarioortegayubro)

---

**🌟 Este material complementario sigue en desarrollo. Nuevos módulos serán agregados periódicamente.**

**Universidad del Aconcagua - Facultad de Ciencias Económicas y Jurídicas**  
**Licenciatura en Analítica de Negocios**  
**Mendoza, Argentina 🇦🇷**
