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
class_dropdown = dcc.Dropdown(options=data['class'].unique(),
                            value='recurrence-events',
                            style={"background-color":"#999999", "color": "black"})





app.layout = dbc.Row([
    dbc.Col([
        html.Div(children=[
            html.Div(children=[
                class_dropdown,
                html.H5(children='Recurrence Event by Age group and Menopause state of the Patient'),
                dcc.Graph(id='first-graph')
            ]),
            html.Div(children=[
                html.H5(children='Recurrence Event by Nb. of Invaded Lymph Nodes and Lymph Nodes with Pierced Capsule'),
                dcc.Graph(id='sixth-graph')
            ])
        ])
    ], width=5),
    dbc.Col([
        html.Div(children=[
            html.Div(children=[
                html.H6(children='Recurrence Event by Degree of Malignancy and Size of the Tumour'),
                dcc.Graph(id='second-graph')
            ]),
            html.Div(children=[
                html.H6(children='Recurrence Event by Radiation Therapy and Degree of Malignancy fo the Tumor'),
                dcc.Graph(id='third-graph')
            ])
        ])
    ], width=3),
    dbc.Col([
        html.Div(children=[
            html.Div(children=[
                html.H6(children='Recurrence Event by Breast Location and Tumour Size'),
                dcc.Graph(id='fourth-graph')
            ]),
            html.Div(children=[
                html.H6(children='Recurrence Event by Radiation Therapy and Nb. of Invaded Lymph Nodes'),
                dcc.Graph(id='fifth-graph')
            ])
        ])
    ], width=3)
], justify='center')
















@app.callback(
    Output(component_id='first-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='age',
                       color='menopause',
                       nbins=6,
                       labels={
                        "age": "Age Group of the Patient",
                        "menopause": "Menopause State of the Patient"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig









@app.callback(
    Output(component_id='second-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='deg_malig',
                       color='tumour_size',
                       nbins=6,
                       labels={
                        "deg_malig": "Degree of Malignancy",
                        "tumour_size": "Size of the Tumour (mm)"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig









@app.callback(
    Output(component_id='third-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='deg_malig',
                       color='irrad',
                       nbins=6,
                       labels={
                        "deg_malig": "Degree of Malignancy",
                        "irrad": "Radiation as a Therapy"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig








@app.callback(
    Output(component_id='fourth-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='tumour_size',
                       color='breast',
                       nbins=6,
                       labels={
                        "tumour_size": "Size of the Tumour (mm)",
                        "breast": "Location of the Breast"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig








@app.callback(
    Output(component_id='fifth-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='inv_nodes',
                       color='irrad',
                       nbins=6,
                       labels={
                        "irrad": "Radiation as a Therapy",
                        "inv_nodes": "Nb. of Invaded Lymph Nodes"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig







@app.callback(
    Output(component_id='sixth-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='inv_nodes',
                       color='node_caps',
                       nbins=6,
                       labels={
                        "inv_nodes": "Nb. of Invaded Lymph Nodes",
                        "node_caps": "Lymph Node Capsules Perforated"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig














# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)

