import numpy as np
import pandas as pd
import altair as alt

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pathlib

from ..utils import Header, make_dash_table




#------------------
# imort data

wine = pd.read_csv("src/data/wine_quality.csv")
#---------------------

def create_layout(app):

    return dbc.Container(
        [Header(app),
             # first plot (Luka)
             dbc.Row([
                dbc.Col([
                    html.H2('Luka'),
                    html.Iframe(
                        id='first_plot',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                    dcc.Dropdown(
                        id='xcol-widget',
                        value='pH',  # REQUIRED to show the plot on the first page load
                        options=[{'label': col, 'value': col} for col in wine.columns])
                ]),
                #second plot ( Yuxuan )
                dbc.Col([
                    html.H2('Yuxuan'),
                    html.Iframe(
                        id='histgram',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                    dcc.Dropdown(
                        id='xcol-widget_2',
                        value='pH',  # REQUIRED to show the plot on the first page load
                        options=[{'label': col, 'value': col} for col in wine.columns]),
                 ])
                 
             ]),
            dbc.Row([
                    # third plot (Eric
                    dbc.Col([
                        html.H2('Eric'),
                        html.Iframe(
                            id='third_plot',
                            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                    dcc.Dropdown(
                            id='xcol-widget_3',
                            value='pH',  # REQUIRED to show the plot on the first page load
                            options=[{'label': col, 'value': col} for col in wine.columns]),
                    dcc.Dropdown(
                            id='ycol-widget',
                            value='pH',  # REQUIRED to show the plot on the first page load
                            options=[{'label': col, 'value': col} for col in wine.columns])
                    ]),
                    # fourth plot (Rain)
                    dbc.Col([
                        html.H2('Rain'),
                        html.Iframe(
                            id='fourth_plot',
                            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                        dcc.Dropdown(
                            id='xcol-widget_4',
                            value='pH',  # REQUIRED to show the plot on the first page load
                            options=[{'label': col, 'value': col} for col in wine.columns]),
                        dcc.Dropdown(
                            id='ycol-widget_4',
                            value='pH',  # REQUIRED to show the plot on the first page load
                            options=[{'label': col, 'value': col} for col in wine.columns])
                        ])  
              ])
    ]
)