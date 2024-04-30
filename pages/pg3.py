import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.express as px
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go

dash.register_page(__name__,
                   path='/compare',  # represents the url text
                   name='Comparision',  # name of page, commonly used as name of link
                   title='multistocks'  # epresents the title of browser's tab
)

# page 2 data
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 12, 3)
df = web.DataReader(['AMZN','GOOGL','META','MSFT','NVDA'],
                    'stooq', start=start, end=end,)

# make multicolumn df to one column
df.columns=["_".join(x) for x in df.columns.values]

df.reset_index(inplace=True)
df.rename(columns={'index': 'Date'}, inplace=True)


stocks = ['AMZN','GOOGL','META','MSFT','NVDA']

layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(id="multi_stock_selector", options=[{"label":x,"value":x} for x in stocks], multi=True, value=stocks[0:2]),
                dcc.Graph(id="multi_stock_selector_graph", figure={})])
            ]
                    
                ),
])


@callback(
    Output('multi_stock_selector_graph', 'figure'),
    Input('multi_stock_selector', 'value')
)
def update_graph2(stocks):
    if isinstance(stocks,str):
        stocks=[stocks]
    cols= ["Close_"+x for x in  list(stocks)]
    
    fig = go.Figure(px.line(df, x="Date", y=cols,labels={"variable": "Stocks","value":"Close price"},))
    # fig.update_layout(margin=dict(l=0,r=0,b=0,t=0))


    return fig