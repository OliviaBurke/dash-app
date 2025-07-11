import dash
from dash import html, dcc
import plotly.express as px

# Sample data
data = {
    "Fruits": ["Apples", "Oranges", "Watermelon", "Kiwis"],
    "Sales": [20, 14, 23, 12]
}
fig = px.bar(data, x="Fruits", y="Sales", title="Fruit Sales", 
                color="Fruits",
                color_discrete_map={
                 "Apples": "#e74c3c",
                 "Oranges": "#f39c12",
                 "Bananas": "#f1c40f",
                 "Kiwis": "#2ecc71"
             })

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello Dash 👋"),
    html.P("Here's a bar chart:"),
    dcc.Graph(figure=fig)  # ← Graph goes here!
])

if __name__ == '__main__':
    app.run(debug=True)
