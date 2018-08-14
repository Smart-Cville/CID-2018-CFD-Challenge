import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go



app = dash.Dash(name=__name__)
app.config.supress_callback_exceptions = True


# Load styles
css_url2 = 'https://codepen.io/garrett-vercoe/pen/yEKLeB.css'
css_bootstrap_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css'
app.css.append_css({
    "external_url": [css_bootstrap_url, css_url2],
})




df = pd.read_csv(
    'fire.csv')

app.layout = html.Div([

#HEADER
    html.Div(
        className='section',
        children=[
            html.H1('PREDICTING FIRE RISK IN CHARLOTTESVILLE', className='landing-text'),

        ]
    ),


#INFO TEXT

    html.Div(
        id='group-x',
        className='row',
        children=[
            html.Div(
                className='col-8',
                children=[
                  html.Div(
                      className='row',
                      children=[
                          html.Div(
                              className='col-3',
                              children=[
                                  html.H2(
                                  'Hover over a residence',
                                  id='text-content',
                                  )],
                                      style={
                                          'fontSize': 60,
                                          'color': '#FFF',
                                          'margin-left': '100px',
                                      }
                                  ),


                          html.Div(
                              className='col-3',
                              children=[
                                  html.H3(
                                      'Amount of residential homes',
                                      id='this-year-1st',
                                      style={
                                          'fontSize': 12,
                                          'color': '#FFF',

                                      }
                                  ),
                                  html.H1(
                                        '13,331',
                                      id='max-energy',
                                      style={
                                          'fontSize': 30,
                                          'color': '#FFF',

                                      }
                                  )
                              ]),
                          html.Div(
                              className='col-3',
                              children=[
                                  html.H3(
                                      'Accuracy Rating',
                                      id='this-year-2nd',
                                      style={
                                          'fontSize': 12,
                                          'color': '#FFF',

                                      }
                                  ),
                                  html.H1(
                                      '75%',
                                      id='max-velocity',
                                      style={
                                          'fontSize': 30,
                                          'color': '#FFF',

                                      }
                                  )
                              ]),



                      ]),

                ]),

            html.Div(
                className='col-3',
                children=[
                    html.H3(
                        'Search particular address',
                        id='this-year-2nd',
                        style={
                            'fontSize': 12,
                            'color': '#FFF',
                            'padding-left' : '0px',
                            'float' : 'left',


                        }
                    ),
                    dcc.Dropdown(
                        id='inputaddress',
                        className='col',
                        options=[
                        {'label': i, 'value': i} for i in df['Address']],
                        value='Input Address'
                    ),


                    html.Div(id='output-container',

                    style={
                        'fontSize': 18,
                        'color': '#FFF',
                        'padding-top' : 20,
                        'margin-left': '0px',
                        'float' : 'left'})


                ]),

            ],
style={
    'margin': 'auto',
    'width': '100%',
    'padding': '10px',

}
    ),


#Risk Row
html.Div(
    className='col-2',
    children=[
        html.H2(
            'Low Risk',
            id='this-year-1st',
            style={
                'fontSize': 20,
                'color': '#d9d2d3',
                'border': '3px solid #d9d2d3',
                'padding': '10px',
                'display':'inline-block',
                'float': 'left',
                'align': 'center',

                'margin-left' : '100px',
                'justify-content' : 'center',

            }
        ),

    ] ),

html.Div(
    className='col-3',
    children=[
        html.H2(
            'Medium Risk',
            id='max-energy',
            style={
                'fontSize': 20,
                'color': '#e59c7c',
                'border': '3px solid #e59c7c',
                'padding': '10px',
                'display':'inline-block',
                'float': 'left',
                'align': 'center',
                'margin-left' : '20px',
                'justify-content' : 'center',


            }
        ),

    ] ),

html.Div(
    className='col-4',
    children=[
        html.H2(
            'High Risk',
            id='blah-hah',
            style={
                'fontSize': 20,
                'color': '#e54253',
                'border': '3px solid #e54253',
                'padding': '10px',
                'display':'inline-block',
                'align' : 'center',
                'margin-left' : '20px',
                'justify-content' : 'center',


            }
        )
    ] ),

# MAPBOX
    dcc.Graph(
    id='map',
    figure={
        'data': [{
            'lat': df['Lat'],
            'lon': df['Lon'],
            'marker': {
                'color': df['Risk'],
                'size': 8,
                'opacity': 0.6
            },
            'customdata': df['Address'],
            'type': 'scattermapbox',
        }],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw',
                'bearing':0,
                'pitch':0,
                'zoom':14,
                'style':'dark',
                'center': {
                'lat':38.0293,
                'lon':-78.4767}

            },

            'plot_bgcolor':'#323130',
            'paper_bgcolor':'rgb(66, 134, 244, 0)',
            'height':750,
            'animation':True,
            'autosize':True,
            'margin': {'l': 0, 'r': 0, 'b': 70, 't': 20}
        }
    }

    ),

    html.Div(
        className='col-8',
        children=[
            html.H2(
                'Predict fire risk for structures around Charlottesville',
                id='blah-hah',
                style={
                    'fontSize': 40,
                    'color': '#fff',
                    'display':'inline-block',
                    'align' : 'center',
                    'margin-left' : '200px',
                    'padding' : '30px',
                    'justify-content' : 'center',


                }
            )
        ] ),
        html.Div(
            className='col-8',
            children=[
                html.H3(
                    'Our team sought to predict which structures in Charlottesville are most at risk for a fire event. This involved a large time commitment in cleaning and joining public data from the Charlottesville Open Data Portal, and combining them with historical data on fire incidents from the Charlottesville Police Department. We then created a series of machine learning algorithms to predict what current homes are at the greatest risk for fire in the future, a result of which is shown above.',
                    id='blah-hah',
                    style={
                        'fontSize': 16,
                        'color': '#d4d4d4',
                        'display':'inline-block',
                        'align' : 'center',
                        'margin-left' : '200px',
                        'justify-content' : 'center',
                        'margin-bottom': '60px',



                    }
                )
            ] ),

            html.Div(
                className='col-8',
                children=[
                    html.H2(
                        'Our Process',
                        id='blah-hah',
                        style={
                            'fontSize': 40,
                            'color': '#fff',
                            'display':'inline-block',
                            'align' : 'center',
                            'margin-left' : '200px',
                            'padding' : '30px',
                            'justify-content' : 'center',


                        }
                    )
                ] ),

            html.Div(
                className='col-8',
                children=[
                    html.H3(
                        '     By using available data and easy-to implement algorithms we believe we successfully modeled fire risk in the Charlottesville community. In our testing, we found we predicted about a third to a half of all fires with ~75% accuracy using only four variables. Most important among these variables were square footage and year the building was built. Large, old buildings were the most likely to catch on fire. When we finished modeling, we had our model generate “low risk” (5% likelihood of fire), “medium risk” (10+% likelihood of fire), and “high risk” (50-80% likelihood of fire) categories. Usually, when our model classified a home as “high risk”--meaning that we think the home has the highest likelihood of a fire--it caught on fire ~75% of the time. And these “high risk” predictions accounted for about a third of all fires. That’s amazing.',
                        id='blah-hah',
                        style={
                            'fontSize': 16,
                            'color': '#d4d4d4',
                            'display':'inline-block',
                            'align' : 'center',
                            'margin-left' : '200px',
                            'justify-content' : 'center',
                            'margin-bottom': '20px',



                        }
                    )
                ] ),

                html.Div(
                    className='col-8',
                    children=[
                        html.H3(
                            '     The fire department can use this high-risk assessment to target the and inspect the riskiest homes, and we can stop some fires before they even happen. Sure, there is some risk of “predicting the future from the past” -- we’re using a model that uses patterns from past data to predict future data, and we weren’t able to deal with issues such as the impact of a past fire on future fire risk. We also are missing invaluable data such as smoke alarm installations. However, although our model and our data could and should be improved, our simple machine learning models generate powerful predictions.',
                            id='blah-hah',
                            style={
                                'fontSize': 16,
                                'color': '#d4d4d4',
                                'display':'inline-block',
                                'align' : 'center',
                                'margin-left' : '200px',
                                'justify-content' : 'center',
                                'margin-bottom': '20px',



                            }
                        )
                    ] ),

                    html.Div(
                        className='col-8',
                        children=[
                            html.H3(
                                '     Our final model was a random forest regression using several variables. We’ve compiled a dashboard that distills all this process into an easy to understand format, so that you don’t need a data science background to understand the data. And what’s great about the dashboard is it’s setup to easily pull from a database server so that the fire data can stay up to date.',
                                id='blah-hah',
                                style={
                                    'fontSize': 16,
                                    'color': '#d4d4d4',
                                    'display':'inline-block',
                                    'align' : 'center',
                                    'margin-left' : '200px',
                                    'justify-content' : 'center',
                                    'margin-bottom': '150px',



                                }
                            )
                        ] ),



])


@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('inputaddress', 'value')])
def update_output(value):
    a = df[df['Address'] ==  value]
    ranking = ''
    if a.iloc[0]['Risk'] == 1:
        ranking = 'low'
    if a.iloc[0]['Risk'] == 2:
        ranking = 'medium'
    if a.iloc[0]['Risk'] == 3:
        ranking = 'high'
    if value != "Input Address" :
        return '{} has a {} risk of a fire occurring.'.format(value, ranking)
    else:
        return ''


@app.callback(
    dash.dependencies.Output(component_id='map',component_property='figure'),
    [dash.dependencies.Input(component_id='inputaddress', component_property='value')]
)

def update_map(inputaddress):
    #function to deliver lat and lon from value in drop box
    found_row = df.loc[df['Address'] == inputaddress]
    found = found_row.iloc[0]
    latx = found[0]
    longx = found[1]
    add = found[2]
    risk = found[4]

    if inputaddress is None:
        return {
            'data': [{
            'lat': df['Lat'],
            'lon': df['Lot'],
            'marker': {
                'color': df['Risk'],
                'size': 20,
                'opacity': 0.6
            },
            'customdata': df['Address'],
            'type': 'scattermapbox',
        }],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw',
                'bearing':0,
                'pitch':0,
                'zoom':16,
                'style':'dark',
                'center': {
                'lat':latx,
                'lon':longx}

            },
            'plot_bgcolor':'#323130',
            'paper_bgcolor':'rgb(66, 134, 244, 0)',
            'height':750,

            'autosize':True,
            'margin': {'l': 0, 'r': 0, 'b': 70, 't': 20}
        },
        }
    else:
        return {
                'data': [{
                    'lat': [latx],
                    'lon': [longx],
                    'marker': {
                        'color': df['Risk'],
                        'size': 18,
                        'opacity': 0.6
                    },
                    'customdata': df['Address'],
                    'type': 'scattermapbox',
                }],
                'layout': {
                    'mapbox': {
                        'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw',
                        'bearing':0,
                        'pitch':0,
                        'zoom':16,
                        'style':'dark',
                        'center': {
                        'lat':latx,
                        'lon':longx}

                    },
                    'plot_bgcolor':'#323130',
                    'paper_bgcolor':'rgb(66, 134, 244, 0)',
                    'height':750,
                    'animation':True,
                    'autosize':True,
                    'margin': {'l': 0, 'r': 0, 'b': 70, 't': 20}
                },

            }


@app.callback(
    dash.dependencies.Output('text-content', 'children'),
    [dash.dependencies.Input('map', 'hoverData')])

def update_text(hoverData):
    s = df[df['Address'] == hoverData['points'][0]['customdata']]
    ranking = ''
    if s.iloc[0]['Risk'] == 1:
        ranking = 'Low'
    if s.iloc[0]['Risk'] == 2:
        ranking = 'Medium'
    if s.iloc[0]['Risk'] == 3:
        ranking = 'High'
    return html.H3(
        '{}, Risk factor: {}'.format(
            s.iloc[0]['Address'],
            ranking,


        )
    )



if __name__ == '__main__':
    app.run_server(debug=True)
