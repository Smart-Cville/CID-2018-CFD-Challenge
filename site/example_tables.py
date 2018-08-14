import dash
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import dateutil.parser as parser

mapbox_access_token = 'pk.eyJ1IjoiaXZhbm5pZXRvIiwiYSI6ImNqNTU0dHFrejBkZmoycW9hZTc5NW42OHEifQ._bi-c17fco0GQVetmZq0Hw'

server = app.server


# Load styles
normalize_css = 'https://unpkg.com/normalize.css@5.0.0'
css_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'

app.css.append_css({
    'external_url': [normalize_css, css_url]
})

df = pd.read_csv('src/data/fireballs.csv')

years = [int(parser.parse(i).year) for i in df['date']]

# GENERACION DE TABLAS CON LOS DATOS IMPORTADOS

def generate_table(df, max_rows=50):
    return html.Div(
      className='container',
      children=[
        html.H1('GREAT BALLS OF FIRE DATA'),
        html.Table(
            className='table',
            # Header
            children=[
              html.Tr([
                html.Th(col) for col in main_columns
              ])
            ]
            +
            # Body
            [
              html.Tr([
                html.Td(df.iloc[i][col]) for col in main_columns
              ]) for i in range(min(len(df), max_rows))
            ],
        )        
      ]
    )

df["year"] = [int(x.split("-")[0]) for x in df.date.values]
main_columns = df.columns.values

# GENERACION DE GRAPH
app.layout = generate_table(df, max_rows=50)

if __name__ == '__main__':
    app.run_server(debug=True, port=9000)
