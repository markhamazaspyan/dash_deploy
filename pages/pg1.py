import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.express as px
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Home',  # name of page, commonly used as name of link
                   title='Stocks',  # title that appears on browser's tab
)

# page 1 data

layout = dbc.Container([
        dbc.Row([
            dbc.Col([html.Img(src='assets/stocks-and-indices.png',style={'height':'80%', 'width':'80%'})])

        ])
])