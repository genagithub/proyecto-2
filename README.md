### 📉 Optimización de Presupuesto Publicitario (Marketing Mix Modeling)

#### 🎯 Contexto del Problema de Negocio 
El área de Finanzas delega en el equipo de Marketing la distribución del presupuesto publicitario, esta asignación de la inversión inicial se define mediante un acuerdo mutuo entre ambas áreas para co-diseñar la estrategia de pauta, debido a la dinámica comercial del negocio el retorno de esta inversión no es inmediato: los ingresos generados por las campañas se calculan, consolidan y recolectan formalmente tras un periodo de maduración de dos meses. Históricamente la empresa opera bajo una distribución jerárquica (tradicional), donde el canal de TV absorbe la gran mayoría del presupuesto por una amplia diferencia sin considerar su elasticidad respecto a las ventas. 

El objetivo es mediante un histórico de campañas consolidadas en los últimos 5 años, modelar y cuantificar el retorno de inversión. A partir de este modelado estadístico automatizar una redistribución óptima del presupuesto que maximice el ingreso, reduciendo la saturación financiera en canales de alto volumen y eliminando ineficiencias en el gasto.

--- 

#### 💡 Hallazgos Clave (Insights): Frontera de Eficiencia
El Análisis Exploratorio de Datos y el estudio de la frontera de eficiencia revelaron una estructura estable pero también ineficiencias críticas en la estrategia actual:
- **Rendimientos Volátiles en TV:** El canal de Televisión garantiza un gran volumen de masa de clientes pero el gasto actual superó el punto de equilibrio óptimo, es decir, invertir más dinero ya no genera más la misma seguridad.
- **Gasto Ineficiente:** El análisis histórico demostró que se lograron niveles de ingresos idénticos usando presupuestos significativamente menores, lo que lleva al siguiente insight: hay un gasto excesivo cuando la posibilidad de generar lo mismo con menos existe.
- **El Potencial Oculto:** El canal de Radio (~15% de retorno) presenta un costo marginal mucho menor y una mayor agilidad de retorno por cada dólar invertido.

---

#### 🛠️ Enfoque Técnico y Modelado
Previo a implementar cualquier rebalanceo de presupuesto, se probó la precisión en un modelado lineal basado en costos (X) e ingresos (Y). En lugar de entrenar una regresión lineal tradicional que promedie el desempeño general (lo cual arrastraría los errores del gasto ineficiente), se aplicó un enfoque avanzado:
- **Validación de Supuestos de Gauss-Markov:** Se realizaron pruebas estadísticas como test de ANOVA para la variable cualitativa, control de homocedasticidad, detección de outliers y correlación de variables, garantizando que el modelo es estadísticamente confiable.
- **Modelado de Elasticidad (Relación Porcentual):** Se implementó una transformación de Log-Log tanto en la variable X como en la variable Y, permitiendo capturar la elasticidad publicitaria, donde los esfuerzos de marketing impactan de forma proporcional y no lineal, y estabilizando la varianza de ingresos en los períodos de alta inversión.
- **Regresión Lineal Sesgada en Eficiencia:** El algoritmo se entrenó exclusivamente sobre estos escenarios ideales y de forma específica para la variable de inversión en el canal de TV, considerándola como la mayor asociada linealmente con la variable objetivo. 
.

---

#### 🚀 Solución Analítica: Simulador Estratégico de Rebalanceo
El resultado final es una herramienta interactiva diseñada para la asignación eficiente de recursos, transformando los datos históricos de pauta publicitaria en un entorno seguro de simulación financiera que opera bajo tres capacidades clave:
- **Auditoría de Inversión:** Analiza de forma previa la distribución actual de los canales, midiendo con precisión su proporción en los costos totales para detectar oportunidades de retorno marginal desaprovechadas.
- **Simulación de Presupuesto:** Permite mover palancas de inversión de forma específica para los canales TV y Radio específicamente, evaluando diferentes escenarios de distribución.
- **Rebalanceo Seguro del Mix de Medios:** Faculta al equipo a redistribuir el presupuesto histórico bajo la frontera de eficiencia, visualizando el impacto estratégico en los ingresos antes de ejecutar la inversión real en el mercado.

---

#### 🎯 Propósito: Impacto Directo (Discovery)
**Reingeniería de la cartera de inversión:** A través de auditoría analítica propone optimizar el capital existente mediante la desinversión parcial en medios tradicionales de Televisión —cuyo rendimiento ha entrado en una fase de estancamiento— y ejecutar una reasignación táctica de esos recursos principalmente hacia la Radio, actuando como un motor de recomendación estratégica para la toma de decisiones ejecutivas. Esta diversificación inteligente no solo maximizará el margen neto por campaña, sino que también acelerará el retorno de inversión (ROI), dinamizando el flujo de caja operativo.
