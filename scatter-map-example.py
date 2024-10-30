from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# load in the data 

URL = "data/tree_census_cleaned.csv"
# load data into dataframe 
tree_census_df = pd.read_csv(URL)


app = Dash(__name__)

app.layout = [
    html.H1(children="Map of Trees", style={'textAlign':'center'}),
    dcc.Checklist(
    ['LONDON PLANETREE',
     'MAPLE, NORWAY',
    'PEAR, CALLERY'],
    ['LONDON PLANETREE'], 
    # inline=True,
    id="tree-select"),
    
    dcc.Graph(id="street-tree-map")
]

@app.callback(
    Output("street-tree-map", "figure"), 
    Input("tree-select", "value"))
def update_g(value):
    
    # sometimes the value is a list if
    # multiple things are selected 
    # a string if a single thing 
    trees_ = []
    if isinstance(value, str):
        trees_ = [value] 
    else:
        trees_ = value 
    

    filter_expr = tree_census_df['spc_common'].isin(trees_)

    all_trees_filtered_df = tree_census_df[filter_expr]
    
        
    
    fig = px.scatter_map(all_trees_filtered_df,
                    lat="lat",
                    lon="lon",
                    color="spc_common",
                    center={'lat':40.68, 'lon':-73.92},
                    color_continuous_scale=px.colors.cyclical.IceFire,
                    zoom = 8,
                    map_style="satellite",
                    hover_data=['spc_common', 'address' ],
                    width=1000, 
                    height=800
                    )

    return fig
if __name__ == '__main__':
    app.run(debug=True)