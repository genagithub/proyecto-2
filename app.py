import pandas as pd
import numpy as np
import dash
from dash import html, dcc, Input, Output
import plotly.graph_objects as go
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/advertising_and_sales.csv", index_col="id")

def get_elasticities(data):
    df_log = np.log(data[["tv", "radio", "social_media", "sales"]] + 1)
    model = LinearRegression()
    model.fit(df_log[["tv", "radio", "social_media"]], df_log["sales"])
    return dict(zip(["TV", "Radio", "Social Media"], model.coef_))

elasticities = get_elasticities(df)
mean_margin = df["sales"].mean() - (df["tv"].mean() + df["radio"].mean() + df["social_media"].mean())

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(id="body", className="e2_body", children=[
    html.A(href="https://github.com/genagithub/proyecto-2/edit/main/optimizaci%C3%B3n_de_inversi%C3%B3n_publicitaria.ipynb", children=[html.H1("Estrategia de Inversión: del volumen a la rentabilidad", className="e2_title")]),
    
    html.Div(className="e2_div_stats", children=[
        html.Div([html.H3("Margen Neto Promedio:"), html.B(f"${round(mean_margin, 2)}",style={"font-weight":"bold","font-size":"1em"})], className="e2_stats"),
        html.Div([html.H3("Elasticidad TV (dominancia):"), html.B(f"{round(elasticities["TV"], 2)}",style={"font-weight":"bold","font-size":"1em"})], className="e2_stats"),
        html.Div([html.H3("Elasticidad Radio (oportunidad):"), html.B(f"{round(elasticities["Radio"], 2)}",style={"font-weight":"bold","font-size":"1em"})], className="e2_stats"),
    ]),

    html.Div(id="dashboard", className="e2_dashboard", children=[
        html.Div(className="e2_column_1", children=[
            html.Div(className="e2_div_graphs", children=[
                dcc.Graph(id="graph-pie", className="e2_graphs", figure={}),
                dcc.Graph(id="graph-bar", className="e2_graphs", figure={})
        ]),
        
        html.Div(className="e2_div_slider", children=[
               html.Label("Simulador de Rebalanceo: Mover presupuesto de TV a Radio (%)", className="e2_label"),
               dcc.Slider(
                   id="rebalance-slider", 
                   min=0, max=30, step=5, value=0, 
                   marks={i: {"label": f"{i}%", "style": {"color": "white"}} for i in range(0, 31, 5)}
               ),
            ])
        ]),

        html.Div(className="e2_column_2", children=[
            dcc.Graph(id="graph-scatter", figure={}),
            html.Div(id="text-resolution", classsName="e2_text_resolution")
        ])
    ])
])

@app.callback(
    [Output("graph-pie", "figure"),
     Output("graph-bar", "figure"),
     Output("graph-scatter", "figure"),
     Output("text-resolution", "children")],
    [Input("rebalance-slider", "value")]
)

def update_strategy(rebalance_pct):
    cost_tv_orig = df["tv"].mean()
    money_change = cost_tv_orig * (rebalance_pct / 100)
    
    piechart = go.Figure(data=[go.Pie(labels=["TV", "Radio", "RRSS"], 
                                      values=[df["tv"].mean(), df["radio"].mean(), df["social_media"].mean()],
                                      hole=.3)])
    piechart.update_layout(title="Distribución Actual del Gasto")

    barchart = go.Figure([go.Bar(x=list(elasticities.keys()), y=list(elasticities.values()), marker_color="indigo")])
    barchart.update_layout(title="Elasticidad: Sensibilidad de Ventas al +1% Gasto", yaxis_title="Impacto % en Ventas")

    df["ROI"] = (df["sales"] - df["tv"]) / df["tv"]
    df_efficient = df[df["ROI"] >= df["ROI"].quantile(0.12)]
    
    scatter = go.Figure()
    scatter.add_trace(go.Scatter(x=df["tv"], y=df["sales"], mode="markers", name="Campaña Estándar", opacity=0.4))
    scatter.add_trace(go.Scatter(x=df_efficient["tv"], y=df_efficient["sales"], mode="markers", name="Frontera de Eficiencia", marker=dict(color="green", size=8)))
    scatter.update_layout(title="Identificación de la Frontera de Eficiencia", xaxis_title="Gasto TV", yaxis_title="Ventas")

    sales_est = df["sales"].mean() * (1 + (rebalance_pct/100 * elasticities["Radio"]))
    text = [
        html.H4("Resolución Estratégica:"),
        html.P(f"Al rebalancear un {rebalance_pct}% de TV hacia Radio, estás moviendo ${round(money_change, 2)} a un canal con mayor retorno marginal."),
        html.P(f"Estimación: Las ventas podrían optimizarse un {round(rebalance_pct * elasticities["Radio"], 2)}% manteniendo el presupuesto constante.")
    ]

    return piechart, barchart, scatter, text

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host='0.0.0.0', port=port)
