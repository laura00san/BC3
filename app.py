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

df = pd.read_csv('https://raw.githubusercontent.com/joaopfonseca/business-cases-21-22/main/BC3_recommendation_system/retail.csv')
df_2 = pd.read_excel('C://Users//User//OneDrive//Ambiente de Trabalho//Mestrado//2 semestre//Business Case//BC3//df_for_app.xlsx')
df_2
countries= countries= df['Country'].unique().tolist()

images_countries = pd.DataFrame(df_2['Country'].unique())
images_countries = images_countries.drop(31, axis=0)

images_list = ['https://i.pinimg.com/736x/92/f7/eb/92f7eb347aa042c255d03eed9f7443e9--vintage-cake-stands-vintage-cakes.jpg',
               'https://m.media-amazon.com/images/I/31ZS7Vm+4VL._AC_SX466_.jpg',
               'https://cdn.shopify.com/s/files/1/0254/2030/0362/products/35995-Red-Toadstool-LED-Nightlight_aa2128f5-9f47-41f3-9e8e-4dfd933917d1.jpg',
               'https://www.rexlondon.com/sites/default/files/styles/original/public/22629-new.jpg?itok=EB5alu71',
               'https://www.masoncash.co.uk/media/catalog/product/2/0/2008.199_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=500&width=600&canvas=600:500',
               'https://i.pinimg.com/736x/92/f7/eb/92f7eb347aa042c255d03eed9f7443e9--vintage-cake-stands-vintage-cakes.jpg',
               'https://cdnapi.paperchase.com/600/744/resize/0/0/00611571.jpg',
               'https://ae01.alicdn.com/kf/H88b95df2a9584f0d944fe8a4612ba32fv/Free-shipping-wangwuquan-190mm-forged-steel-bonsai-scissors-Chinese-traditional-household-coated-scissor.jpg',
               'https://i.pinimg.com/736x/92/f7/eb/92f7eb347aa042c255d03eed9f7443e9--vintage-cake-stands-vintage-cakes.jpg',
               'https://www.masoncash.co.uk/media/catalog/product/2/0/2008.199_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=500&width=600&canvas=600:500',
               'https://cdnapi.paperchase.com/600/744/resize/0/0/00611571.jpg',
               'https://www.rexlondon.com/sites/default/files/styles/original/public/20725_15.jpg?itok=-RxFVkU4',
               'https://www.rexlondon.com/sites/default/files/styles/original/public/22551_10x7.5cm_01.jpg?itok=BNIvH2W0',
               'https://cdn.shopify.com/s/files/1/0066/4118/8979/products/WIAT_Dec13_084_copy_700x.jpg?v=1571728736',
               'https://cdn01.pinkoi.com/product/YzAKtP7p/0/1/640x530.jpg',
               'https://i.ebayimg.com/images/g/ypwAAOSwja5esUW3/s-l600.jpg',
               'https://www.rexlondon.com/sites/default/files/styles/original/public/20725_15.jpg?itok=-RxFVkU4',
               'https://www.magpiepoundbury.co.uk/wp-content/uploads/2016/06/dollygirl-lunch-box-500x500.jpg',
               'https://i.pinimg.com/736x/92/f7/eb/92f7eb347aa042c255d03eed9f7443e9--vintage-cake-stands-vintage-cakes.jpg',
               'https://cdn.shopify.com/s/files/1/0955/4708/products/18-2605_1500x_crop_center.jpg?v=1569244233',
               'https://www.masoncash.co.uk/media/catalog/product/2/0/2008.199_1.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=500&width=600&canvas=600:500',
               'https://i.pinimg.com/originals/9c/aa/27/9caa27882fcfde5717a4b9169829285d.jpg',
               'https://cdn.shopify.com/s/files/1/1579/2849/products/29006_3-nine-lives-charlotte-bag_0_1024x1024.png?v=1626353657',
               'https://m.media-amazon.com/images/I/81RpSqRY4QL._AC_SL1500_.jpg',
               'https://i.pinimg.com/originals/93/39/fa/9339fa030435f191345dcd104be8af8d.jpg',
               'https://media.istockphoto.com/photos/slice-of-pizza-on-a-red-plate-atop-table-closeup-picture-id490366026?k=20&m=490366026&s=170667a&w=0&h=V-wdoHCS_wWYrLSmVDQXfq1716CKoOPhs0a4NOr5o-Q=',
               'https://i.pinimg.com/originals/19/ee/d6/19eed60642d54e10c3e31144f667539a.jpg',
               'https://i.etsystatic.com/8463164/r/il/ad052f/1966485080/il_570xN.1966485080_e31z.jpg',
               'https://media.brandalley.co.uk/catalog/product/cache/1/image/900x/c328707a3c432302e119a0cb3e816d26/1/3/1386947-1_1.jpg',
               'https://m.media-amazon.com/images/I/618WzO7DXUL._AC_SX425_.jpg',
               'https://image.made-in-china.com/202f0j00gnpEtSjrqIzu/High-Quality-24-Colored-Pencils-in-Paper-Tube.jpg',
               'data:image/jpeg;base64,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',
               'https://xcdn.next.co.uk/Common/Items/Default/Default/ItemImages/AltItemShot/315x472/T31494s.jpg',
               'https://m.media-amazon.com/images/I/61xcFrHAheL._AC_SS450_.jpg',
               'https://i.pinimg.com/originals/8d/15/f4/8d15f42ee33612adeae7998b52094cad.jpg',
               'https://i.ebayimg.com/images/g/h-4AAOSw2ZhfVtxi/s-l400.jpg',
               'https://www.ubuy.co.it/productimg/?image=aHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0kvNjFVSUVTUEZWcFMuX0FDX1NMMTUwMF8uanBn.jpg'
]

images_countries['image'] = images_list
images_countries.rename(columns = {0:'Country'}, inplace = True)

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