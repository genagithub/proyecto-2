### 📉 Optimización de Presupuesto Publicitario (Marketing Mix Modeling)

#### 🎯 El Problema de Negocio
Invierte grandes sumas de dinero en publicidad en múltiples canales (TV, Radio y Social Media) sin saber con certeza si cada dólar invertido está generando el máximo retorno posible. El objetivo es descubrir si existe una redistribución óptima del presupuesto que maximice las ventas sin aumentar el gasto total.

--- 

#### 💡 Hallazgos Clave de la Investigación (Frontera de Eficiencia)
El Análisis Exploratorio de Datos (EDA) y el estudio de la frontera de eficiencia revelaron ineficiencias críticas en la estrategia actual:
- **Rendimientos Decrecientes en TV:** La televisión garantiza un gran volumen de masa de clientes, pero el gasto actual superó el punto de equilibrio óptimo. Invertir más dinero en TV ya no genera más ventas proporcionales.
- **Gasto Ineficiente:** El análisis histórico demostró que se lograron niveles de ingresos idénticos usando presupuestos significativamente menores. La empresa está gastando de más.
- **El Potencial Oculto:** La Radio (~15% de retorno) y los canales de Social Media presentan un costo marginal mucho menor y una mayor agilidad de retorno por cada dólar invertido.

---

#### 🛠️ Enfoque Técnico y Modelado
En lugar de entrenar una regresión lineal tradicional que promedie el desempeño general (lo cual arrastraría los errores del gasto ineficiente), se aplicó un enfoque avanzado:
- **Filtrado por Frontera de Eficiencia:** Se aisló el cuantil superior (top 12%) de los datos históricos con mejor rendimiento de ROI.
- **Regresión Lineal Segmentada:** El algoritmo se entrenó exclusivamente sobre estos escenarios ideales para aprender a replicar los éxitos de negocio del pasado.
- **Validación de Supuestos:** Se realizaron pruebas estadísticas rigurosas para asegurar la normalidad en los residuos, control de outliers y correlación de variables, garantizando que el modelo es estadísticamente confiable.

---

#### 🚀 El Data Product: Simulador Estratégico
El resultado final es un Dashboard Interactivo para el equipo de Marketing y Finanzas. La herramienta permite:
1- Mover palancas de presupuesto para TV, Radio y Redes Sociales.
2- Visualizar de inmediato la estimación de ingresos optimizada bajo la frontera de eficiencia.
3- Rebalancear el mix de medios de forma segura antes de ejecutar la inversión real.

---

### 🎯 Recomendación de Negocio
No se debe aumentar el presupuesto total de marketing. La solución consiste **en quitar una fracción de la inversión estancada en TV y redirigirla de forma estratégica hacia la Radio y canales digitales** para maximizar el margen neto y acelerar la velocidad del retorno.
