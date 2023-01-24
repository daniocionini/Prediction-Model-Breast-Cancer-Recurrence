# --------------------------------------
# import the dataset
data = open("./breast-cancer.data")
feat = open("./breast-cancer.names")
data = data.read()
feat = feat.read()

data = data.replace('?','')

import pandas as pd
from io import StringIO

data = StringIO(data)
data = pd.read_csv(data, sep=",")

data.columns = ['class', 'age', 'menopause', 'tumour_size', 'inv_nodes', 'node_caps', 'deg_malig', 'breast', 'breast_quad', 'irrad']
# --------------------------------------



# Import libraries
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


# Create the Dash app
app = Dash(external_stylesheets=[dbc.themes.DARKLY])




# Set up the app layout
geo_dropdown = dcc.Dropdown(options=data['class'].unique(),
                            value='no-recurrence-events',
                            style={"background-color":"#999999", "color": "black"})




app.layout = html.Div(children=[
html.Div(children=[
    html.H1(children='Breast Cancer Dashboard'),
    geo_dropdown,
    dcc.Graph(id='price-graph', style={"margin-left":"350px", "margin-right":"350px"})
]),
html.Div(children=[
    html.H1(children=''),
    dcc.Graph(id='second-graph', style={"margin-left":"350px", "margin-right":"350px"})
]),
html.Div(children=[
    html.H1(children=''),
    dcc.Graph(id='third-graph', style={"margin-left":"350px", "margin-right":"350px"})
])
])



# Set up the callback function
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = data[data['class'] == selected_geography]
    line_fig = px.density_contour(filtered_avocado,
                       x='deg_malig', y='deg_malig',
                       color='node_caps',
                       labels={
                        "deg_malig": "Degree of Malignancy",
                        "node_caps": "Lymph Node Capsules Perforated"
                       },
                       title=f'based on {selected_geography}')
    line_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white')
    return line_fig



# Set up the callback function
@app.callback(
    Output(component_id='second-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = data[data['class'] == selected_geography]
    line_fig = px.funnel(filtered_avocado,
                       x='deg_malig', y='deg_malig',
                       color='breast_quad',
                       labels={
                        "deg_malig": "Degree of Malignancy",
                        "breast_quad": "Breast Quadrant"
                       },
                       title=f'based on {selected_geography}')
    line_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white')
    return line_fig


# Set up the callback function
@app.callback(
    Output(component_id='third-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = data[data['class'] == selected_geography]
    line_fig = px.bar(filtered_avocado,
                       x='deg_malig', y='deg_malig',
                       color='irrad',
                       labels={
                        "deg_malig": "Degree of Malignancy",
                        "irrad": "Radiation Therapy"
                       },
                       title=f'based on {selected_geography}')
    line_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white')
    return line_fig



# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
