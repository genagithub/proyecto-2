import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from scipy.stats import pearsonr, zscore, kurtosis, norm, kstest
from sklearn.linear_model import LinearRegression


df = pd.read_csv("data/advertising_and_sales.csv")
df.set_index("id", inplace=True)

corr, _ = pearsonr(df["radio"], df["sales"])

df_zscore = df.loc[:,["tv","sales"]]

df_zscore["tv_zscore"] = np.abs(zscore(df["tv"]))
df_zscore["sales_zscore"] = np.abs(zscore(df["sales"]))

outliers = df_zscore.loc[(df_zscore["tv_zscore"] > 3) | (df_zscore["sales_zscore"] > 3),:]

curtosis_x = kurtosis(df["tv"])
curtosis_y = kurtosis(df["sales"])

_, p_value_var_x = kstest(df["tv"].values, "norm")
_, p_value_var_y = kstest(df["sales"].values, "norm")

df["ROI"] = (df["sales"] - df["tv"]) / df["tv"]

umbral_roi = df["ROI"].quantile(0.2)
df_model = df[df["ROI"] >= umbral_roi].copy()

var_x = df_model["tv"].values.reshape((-1,1))
var_y = df_model["sales"]

linear_regression = LinearRegression()
linear_regression.fit(var_x, var_y)

objects = df[["tv","sales"]].sample(n=25)
predicts = linear_regression.predict(objects["tv"].values.reshape((-1,1)))

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(id="body",className="e2_body",children=[
    html.A(href="https://github.com/genagithub/proyecto-2/blob/main/optimizaci%C3%B3n_de_inversi%C3%B3n_publicitaria.ipynb",target="_blank",children=[html.H1("EDA y Modelado lineal sobre costos e ingresos",id="title",className="e2_title")]),
    html.Div(id="dashboard",className="e2_dashboard",children=[
        html.Div(id="column-1",className="e2_column_1",children=[
            dcc.Dropdown(id="dropdown",className="e2_dropdown",
                        options=[
                            {"label":"Costos en promoción (TV)","value":"tv"},
                            {"label":"Ingresos por ventas","value":"sales"}
                        ],
                        value="tv",
                        multi=False,
                        clearable=False),
            html.Div(className="e2_div_graphs",children=[
                dcc.Graph(id="graph-1",className="e2_graphs",figure={}), 
                dcc.Graph(id="graph-2",className="e2_graphs",figure={})
            ])
        ]),
        html.Div(id="column-2",className="e2_column_2",children=[
            html.Div(id="p_values",className="e2_stats_div",children=[
                html.Div(id="p_value_var_x",className="e2_stats",children=[html.P(f"Kolgomorov (X): P = {round(p_value_var_x, 1)}",style={"font-size":"1em"})]),
                html.Div(id="p_value_var_y",className="e2_stats",children=[html.P(f"Kolgomorov (Y): P = {round(p_value_var_y, 1)}",style={"font-size":"0.98em"})])
            ]),
            html.Div(f"Correlación de Pearson: {round(corr,2)}",className="e2_corr",id="corr"),
            dcc.Graph(id="graph-3",className="e2_graph_3",figure={})
        ])
    ])
])

@app.callback(
    [Output(component_id="graph-1",component_property="figure"),
    Output(component_id="graph-2",component_property="figure"),
    Output(component_id="graph-3",component_property="figure")],
    [Input(component_id="dropdown",component_property="value")]
)

def update_dash(slct_var):
    
    mean = df[slct_var].mean()
    median = df[slct_var].median()
    
    var_title = "Campaña Publicitaria en TV ($)"
    
    if slct_var == "sales":
        var_title = "Ventas Históricas ($)"
    else:
        var_title = var_title
        
    scatter_radio = go.Figure()
    scatter_radio.add_trace(go.Scatter(x=df[slct_var], y=df["radio"], mode="markers", marker_color="blue"))
    scatter_radio.update_layout(title="Correlación con el canal Radio", xaxis_title=var_title, yaxis_title="Campaña Publicitaria en Radio ($)")
    
    histplot = go.Figure(go.Histogram(x=df[slct_var], name="Distribución"))
    histplot.add_trace(go.Scatter(x=[mean,mean], y=[0,100], mode="lines+markers", marker_color="red", name="Media"))
    histplot.add_trace(go.Scatter(x=[median,median], y=[0,100], mode="lines+markers", marker_color="green", name="Mediana"))
    histplot.update_layout(title="Histograma", xaxis_title=var_title, yaxis_title=" ")
    
    linear_regression = go.Figure()
    linear_regression.add_trace(go.Scatter(x=df["tv"], y=df["sales"], mode="markers", marker_color="blue", name="Ventas históricas"))
    linear_regression.add_trace(go.Scatter(x=objects["tv"], y=predicts, mode="lines+markers", marker_color="red", name="Ventas estimadas"))
    linear_regression.add_trace(go.Scatter(x=objects["tv"], y=objects["sales"], mode="markers", marker_color="green", name="Ventas reales"))
    linear_regression.update_layout(title="Frontera de Eficiencia de Inversión Publicitaria", xaxis_title="Campaña Publicitaria en TV ($)", yaxis_title=" ")

    return scatter_radio, histplot, linear_regression

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050)) 
    app.run_server(host='0.0.0.0', port=port)
