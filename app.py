import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_daq as daq
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import openpyxl

df = pd.read_csv('https://raw.githubusercontent.com/joaopfonseca/business-cases-21-22/main/BC3_recommendation_system/retail.csv')
df_2 = pd.read_excel('https://raw.githubusercontent.com/laura00san/BC3/main/df_for_app.xlsx')
df_2
countries= countries= df['Country'].unique().tolist()

dropdown_country = dcc.Dropdown(
        id='country',
        options=countries,
        value='United Kingdom',
        style ={'width' :250, "font-size": 13, 'top': -8, 'left': 30}
    )

##########3
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

server = app.server


country_choice = dbc.CardGroup(
            [
                dbc.Label("Choose your country", style={"font-size": 13}),
                html.Br(),
                dropdown_country
            ] ,className="controls_artists"
        )



user_id = dbc.CardGroup(
            [
                dbc.Label("User id", style={"font-size": 13}),
                html.Br(),
                dbc.Input(placeholder="Insert your id here...", type="text", style={"font-size": 13}),
            ] , className="user_id"
        )



recommended_prod = dbc.Card(
    [
        dbc.CardGroup(
            [
                dbc.Col([
                    dbc.Row([
                        html.P('You might like...',style={"font-size": 20, "font-weight": "bold",  "text-align": "center", "color":"white"}),
                        html.Hr()
                    ]),
                    dbc.Row([
                    html.P(id='recommeded_item1', className='rec_prod1', style={"color":"white"}),
                    html.P(id='recommeded_item2', className='rec_prod1',style={"color":"white"}),
                    html.P(id='recommeded_item3', className='rec_prod1', style={"color":"white"}),
                    html.P(id='recommeded_item4', className='rec_prod1', style={"color":"white"}),
                    html.P(id='recommeded_item5', className='rec_prod1', style={"color":"white"}),
                ]
            ),
            ]),
        ])
    ], body=True,
    style={'background': '#026C65', 'width':'50%', 'margin': 'auto'})


navbar = dbc.Navbar([
        html.A([
            dbc.Row([
                dbc.Col(
                country_choice, style={'width':6}
                ),
                dbc.Col(
                user_id,style={'width':6}
                ),

            ]),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(html.Img(src="https://snappinoutofit.files.wordpress.com/2022/04/established-in-1980-2.png", height="130px"),style={'width':3}),
                    dbc.Col(
                        [dbc.NavItem(dbc.NavLink("Home", active=True, href="#", style={'color':'black',"font-weight": "bold", "font-size": 25, 'position':'relative','top':40}))],width=2),
                    dbc.Col(
                        [dbc.NavItem(dbc.NavLink("OurProducts", active=True, href="#", style={"font-weight": "bold",  'color':'#026C65',"font-size": 25, "text-align": "center", 'position':'relative','top':40}),
                                     )],width=2),
                    dbc.Col(
                        [dbc.NavItem(dbc.NavLink("About Us", active=True, href="#", style={'color':'black', "font-weight": "bold", "font-size": 25, 'position':'relative','top':40}),
                                     )],width=2),
                    dbc.Col(
                        [dbc.NavItem(dbc.NavLink("Contact Us", active=True, href="#", style={'color':'black', "font-weight": "bold", "font-size": 25, 'position':'relative','top':40}),
                                     )],width=2),
                ],
                align="between",
                #no_gutters=True,
            )
        ] , style={'width': '100%'})
    ], style={'background': 'green', 'margin-bottom': '10px'}
)






app.layout = dbc.Container([
        navbar,
        recommended_prod
    ],
    fluid=True,
)


@app.callback(
    [
        Output("recommeded_item1", "children"),
        Output("recommeded_item2", "children"),
        Output("recommeded_item3", "children"),
        Output("recommeded_item4", "children"),
        Output("recommeded_item5", "children"),

    ],
    [
        Input("country", "value"),
    ]
)

def recommended_products(country):
    pop_per_country = df_2 [df_2 ['Country'] == country]
    pop_per_country = pop_per_country.head(5)['Description'].tolist()
    return pop_per_country[0],\
            pop_per_country[1],\
            pop_per_country[2],\
            pop_per_country[3],\
            pop_per_country[4]



if __name__ == '__main__':
    app.run_server(debug=True)
