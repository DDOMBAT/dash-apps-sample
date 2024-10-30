from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from helper_funcs import get_url

# reading the data into pandas 
df = pd.read_csv(get_url())

# instantiate dash app
app = Dash()

# layout of our app 
app.layout = [
    
    # styled <h1> to be in the center and 
    # have a background color of #84d8d8
    html.H1(children='Population Growth by Year', style={'textAlign': 'center', 'background-color':'#84d8d8'}),
    dcc.Dropdown(df.country.unique(), 
                 'France', 
                 id="dropdown-selection",
                #  multi=True, # adds the ability to select multiple drop down entries
                 placeholder="Select a Country" 
                 ), 
    dcc.Graph(id="graph-content")
]

# dataflow of the components 
# register input/output
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_g(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)