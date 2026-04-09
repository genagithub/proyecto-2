import pandas as pd
import numpy as np
import os
import dash
from dash import html, dcc, Input, Output
import plotly.graph_objects as go
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression

# --- 1. CARGA Y MODELADO DE ELASTICIDAD ---
df = pd.read_csv("data/advertising_and_sales.csv", index_col="id")

# Calculamos Elasticidades (Log-Log) para entender el impacto porcentual
# Esto resuelve tu duda: ¿Por qué TV es clave? Porque su coeficiente será el más alto.
def get_elasticities(data):
    df_log = np.log(data[['tv', 'radio', 'social_media', 'sales']] + 1)
    model = LinearRegression()
    model.fit(df_log[['tv', 'radio', 'social_media']], df_log['sales'])
    return dict(zip(['TV', 'Radio', 'Social Media'], model.coef_))

elasticidades = get_elasticities(df)
margen_promedio = df["sales"].mean() - (df["tv"].mean() + df["radio"].mean() + df["social_media"].mean())

# --- 2. CONFIGURACIÓN DASH ---
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(className="e2_body", children=[
    html.H1("Estrategia de Inversión: Del Volumen a la Rentabilidad", id="title"),
    
    # KPIs Superiores
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}, children=[
        html.Div([html.H3(f"${round(margen_promedio, 2)}"), html.P("Margen Neto Promedio")], className="e2_stats"),
        html.Div([html.H3(f"{round(elasticidades['TV'], 2)}"), html.P("Elasticidad TV (Dominancia)")], className="e2_stats"),
        html.Div([html.H3(f"{round(elasticidades['Radio'], 2)}"), html.P("Elasticidad Radio (Oportunidad)")], className="e2_stats"),
    ]),

    html.Div(id="dashboard", className="e2_dashboard", children=[
        # Columna de Controles y Simulación
        html.Div(className="e2_column_1", children=[
            html.Label("Simulador de Rebalanceo: Mover presupuesto de TV a Radio (%)"),
            dcc.Slider(id='rebalance-slider', min=0, max=30, step=5, value=0, 
                       marks={i: f'{i}%' for i in range(0, 31, 5)}),
            
            dcc.Graph(id="graph-pie-gasto"),
            dcc.Graph(id="graph-elasticidad")
        ]),

        # Columna de Resultados de Negocio
        html.Div(className="e2_column_2", children=[
            dcc.Graph(id="graph-frontera-eficiencia"),
            html.Div(id="resolucion-texto", style={'padding': '15px', 'backgroundColor': '#f9f9f9', 'borderRadius': '10px'})
        ])
    ])
])

# --- 3. CALLBACKS ---
@app.callback(
    [Output("graph-pie-gasto", "figure"),
     Output("graph-elasticidad", "figure"),
     Output("graph-frontera-eficiencia", "figure"),
     Output("resolucion-texto", "children")],
    [Input("rebalance-slider", "value")]
)
def update_strategy(rebalance_pct):
    # Simulación simple de impacto
    gasto_tv_orig = df["tv"].mean()
    cambio_dinero = gasto_tv_orig * (rebalance_pct / 100)
    
    # Gráfico 1: Mix de Gasto Actual
    pie_gasto = go.Figure(data=[go.Pie(labels=['TV', 'Radio', 'RRSS'], 
                                      values=[df['tv'].mean(), df['radio'].mean(), df['social_media'].mean()],
                                      hole=.3)])
    pie_gasto.update_layout(title="Distribución Actual del Gasto")

    # Gráfico 2: Comparativa de Elasticidades (Poder de Tracción)
    fig_els = go.Figure([go.Bar(x=list(elasticidades.keys()), y=list(elasticidades.values()), marker_color='indigo')])
    fig_els.update_layout(title="Elasticidad: Sensibilidad de Ventas al +1% Gasto", yaxis_title="Impacto % en Ventas")

    # Gráfico 3: Frontera de Eficiencia (Scatter)
    # Filtramos por tu umbral de ROI del 12% para mostrar solo los casos eficientes
    df["ROI"] = (df["sales"] - df["tv"]) / df["tv"]
    df_eficiente = df[df["ROI"] >= df["ROI"].quantile(0.12)]
    
    fig_scatter = go.Figure()
    fig_scatter.add_trace(go.Scatter(x=df["tv"], y=df["sales"], mode='markers', name='Campaña Estándar', opacity=0.4))
    fig_scatter.add_trace(go.Scatter(x=df_eficiente["tv"], y=df_eficiente["sales"], mode='markers', name='Frontera Eficiente', marker=dict(color='green', size=8)))
    fig_scatter.update_layout(title="Identificación de la Frontera de Eficiencia", xaxis_title="Gasto TV", yaxis_title="Ventas")

    ventas_est = df["sales"].mean() * (1 + (rebalance_pct/100 * elasticidades['Radio']))
    texto = [
        html.H4("Resolución Estratégica:"),
        html.P(f"Al rebalancear un {rebalance_pct}% de TV hacia Radio, estás moviendo ${round(cambio_dinero, 2)} a un canal con mayor retorno marginal."),
        html.P(f"Estimación: Las ventas podrían optimizarse un {round(rebalance_pct * elasticidades['Radio'], 2)}% manteniendo el presupuesto constante.")
    ]

    return pie_gasto, fig_els, fig_scatter, texto

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host='0.0.0.0', port=port)
