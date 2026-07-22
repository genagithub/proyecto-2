### 📉 Optimización de Presupuesto Publicitario (Marketing Mix Modeling)

#### 🎯 El Contexto del Problema 
Los sectores de marketing y finanzas invierten grandes sumas de dinero en publicidad en múltiples canales (TV, Radio y Social Media) sin saber con certeza si cada dólar invertido está generando el máximo retorno posible. El objetivo es descubrir si existe una redistribución óptima del presupuesto que maximice las ventas sin aumentar el gasto total.

--- 

#### 💡 Hallazgos Clave de la Investigación (Frontera de Eficiencia)
El Análisis Exploratorio de Datos (EDA) y el estudio de la frontera de eficiencia revelaron ineficiencias críticas en la estrategia actual:
- **Rendimientos Volátiles en TV:** La televisión garantiza un gran volumen de masa de clientes, pero el gasto actual superó el punto de equilibrio óptimo. Invertir más dinero en TV ya no genera más la misma seguridad.
- **Gasto Ineficiente:** El análisis histórico demostró que se lograron niveles de ingresos idénticos usando presupuestos significativamente menores. La empresa está gastando de más.
- **El Potencial Oculto:** La Radio (~15% de retorno) y los canales de Social Media presentan un costo marginal mucho menor y una mayor agilidad de retorno por cada dólar invertido.

---

#### 🛠️ Enfoque Técnico y Modelado
En lugar de entrenar una regresión lineal tradicional que promedie el desempeño general (lo cual arrastraría los errores del gasto ineficiente), se aplicó un enfoque avanzado:
- **Filtrado por Frontera de Eficiencia:** Se aisló el cuantil superior (top 12%) de los datos históricos con mejor rendimiento de ROI.
- **Regresión Lineal Segmentada:** El algoritmo se entrenó exclusivamente sobre estos escenarios ideales para aprender a replicar los éxitos de negocio del pasado.
- **Validación de Supuestos:** Se realizaron pruebas estadísticas rigurosas para asegurar la normalidad en los residuos, control de outliers y correlación de variables, garantizando que el modelo es estadísticamente confiable.

---

#### 🚀 Solución Analítica: Simulador Estratégico
El resultado final es una herramienta interactiva diseñada para la asignación eficiente de recursos, transformando los datos históricos de pauta publicitaria en un entorno seguro de simulación financiera que opera bajo tres capacidades clave:
- **Auditoría de Inversión:** Analiza de forma previa la distribución actual de los canales, midiendo con precisión su proporción en los costos totales para detectar oportunidades de retorno marginal desaprovechadas.
- **Simulación de Presupuesto:** Permite mover palancas de inversión de forma específica para los canales TV y Radio específicamente, evaluando diferentes escenarios de distribución.
- **Rebalanceo Seguro del Mix de Medios:** Faculta al equipo a redistribuir el presupuesto estratégico bajo la frontera de eficiencia, visualizando el impacto en los ingresos antes de ejecutar la inversión real en el mercado.

---

#### 🎯 Recomendación Estratégica
No se debe aumentar el presupuesto total de marketing. La solución consiste **en quitar una fracción de la inversión estancada en TV y redirigirla de forma estratégica hacia la Radio y canales digitales** para maximizar el margen neto y acelerar la velocidad del retorno.
