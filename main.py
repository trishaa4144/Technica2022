from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

app = Dash(__name__)
app.title = "Finance Ferret"

app.layout = html.Div(children=[
  html.Div(
    id="header",
    children=[
      html.Img(src=r'assets/ferret.png', id='header-ferret'),
      html.H1(children='Finance Ferret', id = "title"),
      html.P(
        "Hello! My name is Finance Ferret, and I'm here to help you make smarter financial decisions! Today we'll be covering investment strategies for young adults, specifically in investing in a Retirement Portfolio!", id='header-text')
    ]),
  html.Div(
    id="definition",
    children=[
      html.H1(children="What is a Retirement Fund?"),
      html.P(
        "A retirement fund allows you to receive income in later years through a portfolio of stock and bonds. When you retire, you will be able to receive income in the form of a pension from this fund."
      ),
      html.Img(src=r'assets/forward.png', id='definition-ferret')
    ]),
  html.Div(id="explanation",
           children=[
             html.H1(children="Types of Retirement Funds"),
             html.H2(children="401K"),
             html.P(children="A 401(k) plan is an employer-sponsored pension account. If it is a Roth IRA, you are contributing after-tax money, so when you withdraw it, it will have already been taxed. Your employer may match your contributions with a 401k, in which case it is best to maximize those benefits."),
             html.H2(children="IRA"),
             html.P(children="IRA stands for Individual Retirement Account and does not have to be company sponsored. Similar to a Roth 401k, a Roth IRA involves contributing after-tax money.")
           ]),
  html.Div(
    id="early",
    children=[
      html.H1(children="Why invest early in retirement?"),
      html.P(
        "If you're young, you may not be thinking as far as retirement. However, thanks to compound interest, investing early will grow you much more money than those who start later."
      ),
      html.P(
        "Compounding is the ability to grow an investment by reinvesting the earnings. It allows investors to accrue wealth over time; based on a 5% interest rate a $10,000 investment at age 20 would grow to over $70,000 by age 60."
      )
    ]),
  html.Div(
        id="ferret-ages",
        children=[html.Img(src=r'assets/bb.png', className="ageimg"),
                  html.Img(src=r'assets/med.png', className="ageimg"),
                  html.Img(src=r'assets/big.png', className="ageimg")
                 ]),
  html.Div(id="sliders",
           children=[
             html.H1(children="Visualize Your Savings", id="visualize"),
             html.P(children="Your current age: ", className="slider-p"),
             dcc.Slider(18,
                        65,
                        value=20,
                        id='age',
                        marks=None,
                        tooltip={
                          "placement": "bottom",
                          "always_visible": True
                        }),
             html.P(children="Estimated monthly contribution (USD): ", className="slider-p"),
             dcc.Slider(10,
                        10000,
                        value=200,
                        id='monthly',
                        marks=None,
                        tooltip={
                          "placement": "bottom",
                          "always_visible": True
                        }),
             html.Br()
           ]),
  html.Div(id="graph", children=[dcc.Graph(id='401k', figure={})]),
  html.P(id="descr", children="As you can see, investing in a retirement fund has much better returns long term than keeping it in a savings account. Don't keep money sitting around! (except for an emergency fund)"),
  html.Div(
    id="tips",
    children=[
      html.H1(children="Tips for Investing", id="tipsheading"),
      html.H4(children="1. Diversify your portfolio"),
      html.P(
        "Don't put all your eggs in one basket. Diversify your investments, so if one goes south, you have others to fall back on."
      ),
      html.H4(children="2. Maximize employer benefits"),
      html.P(
        "Take advantage of employer benefits, such as employer match, where an employer matches a portion of your retirement savings."
      ),
      html.H4(children="3. Take some risk"),
      html.P(
        "With risk comes reward. If you're younger, investing in funds of higher volatility may yield better results and give you time to recooperate before you retire."
      ),
      html.H4(children="4. Start now, start somewhere"),
      html.P(
        "Start as early as you can. Even if youre only setting aside $25, keep investing and saving. You will develop positive money habits."
      )
    ]),
  html.Img(src=r'assets/left.png', id="leftimg")
])


@app.callback([Output(component_id='401k', component_property='figure')], [
  Input(component_id='age', component_property='value'),
  Input(component_id='monthly', component_property='value')
])
def update_401k(age, monthly):
  years = 65 - age
  x = np.linspace(0, years, num=int(years))
  df = monthly * ((1 + .0003)**(x) - 1) / .0003
  df1 = monthly * x
  df2 = monthly * ((1 + .07)**(x) - 1) / .07
  fig2 = go.Figure([
    go.Scatter(x=x, y=df2, name="Retirement Fund (401k/IRA)", mode="lines"),
    go.Scatter(x=x, y=df1, name="Total Investment", mode="lines"),
    go.Scatter(x=x, y=df, name="Savings Account", mode="lines")
  ])
  fig2.update_layout(title="Retirement Savings",
                     title_x=0.5,
                     xaxis_title="Years from Today",
                     yaxis_title="Savings (USD)",
                     template="plotly_dark")
  return [fig2]


if __name__ == '__main__':
  app.run_server(host="0.0.0.0", debug=True)
