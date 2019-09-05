import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_table
import dash_html_components as html
import dash_design_kit as ddk
from portfolio_table import portfolio_table
from theme import theme
import pandas as pd
from pprint import pprint

from components import Column, Header, Row

app = dash.Dash(
    __name__
)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

server = app.server  # Expose the server variable for deployments

def get_home():
    return ddk.Block([
        # ddk.Card(),
        portfolio_table(),
        dcc.Markdown(id='output')
        # ddk.Card([dcc.Tabs(
        #     id='portfolio-tabs',
        #     value='create-report',
        #     children=[
        #         dcc.Tab(value='historical', label='Historical View'),
        #         dcc.Tab(value='predicted', label='Predicted View'),
        #         # I need to figure out why I get a console error about this not being present in layout even though suppress callback exeptions is on.
        #         dcc.Tab(value='create-report', label='Create Report', children=html.Button(id='portfolio-create-report-button', n_clicks=0, style={'display': 'none'}))
        #     ]
        #     ),
        #     html.Div(id='portfolio-tabs-content')
        # ])
        ])

# Standard Dash app code below
app.layout = ddk.App(
    theme=theme,
    children=[
        get_home()
])

@app.callback(Output('output', 'children'),
              [Input('portfolio-table', 'data')])
def print_data(data):
    pprint(data)
    y = '''
    ```
    {}
    ```
    '''.format(data)
    return y


if __name__ == '__main__':
    app.run_server(debug=True, port=8092)
