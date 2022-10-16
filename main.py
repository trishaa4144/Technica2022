from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

app = Dash(__name__)

app.layout = html.Div(children=[
  html.Div(
    id = "header",
    children = [
      html.H1(children='Finance Ferret'),
      html.Img(src=r'assets/ferret.jpg', id='header-ferret'),
      html.P("Hello, intro", id='intro-text')
    ]),
  html.Div(
    id = "intro",
    children= [
      html.P("Hello, intro", id='intro-text')
    ]
  ),

  html.Div(
    id="sliders",
    children = [
      dcc.Slider(18, 65, value=32, id='age'),
      dcc.Slider(10, 10000, value=200, id='monthly')]
  ),

  html.Div(
    id="graph",
    children = [dcc.Graph(id='401k', figure={})]
  )
  
])

@app.callback([Output(component_id='401k', component_property='figure')],
    [Input(component_id='age', component_property='value'),    
     Input(component_id='monthly', component_property='value')])
def update_401k(age, monthly):
  years = 65 - age
  x = np.linspace(0, years, num=years)
  df2 = monthly * ((1+.07)**(x) - 1)/.07
  fig2= go.Figure(go.Scatter(x=x, y = df2, name=f"corr{1}", mode ="lines"))
  fig2.update_layout(width=950, title="Retirement Savings", title_x=0.5, 
                    xaxis_title="Years", yaxis_title="Savings (USD)")
  return [fig2]



if __name__ == '__main__':
  app.run_server(host="0.0.0.0", debug=True)
