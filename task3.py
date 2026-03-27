import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

print("Running correct file...")  # to confirm correct file is running

# Load dataset (Excel)
data = pd.read_excel("students.xlsx")

print(data.columns)  # check column names

# Create charts
bar_chart = px.bar(
    data,
    x="NAME",
    y="MARKS",
    title="Student Marks Comparison"
)

histogram = px.histogram(
    data,
    x="MARKS",
    nbins=10,
    title="Marks Distribution"
)

scatter = px.scatter(
    data,
    x="AGE",
    y="MARKS",
    color="MARKS",
    size="MARKS",
    title="Age vs Marks"
)

# Create dashboard
app = Dash(__name__)

# Layout
app.layout = html.Div(
    style={'textAlign': 'center', 'fontFamily': 'Arial'},
    children=[

        html.H1("Student Performance Dashboard", style={'marginBottom': '40px'}),

        html.Div([

            html.Div(
                dcc.Graph(figure=bar_chart),
                style={'width': '33%', 'display': 'inline-block'}
            ),

            html.Div(
                dcc.Graph(figure=histogram),
                style={'width': '33%', 'display': 'inline-block'}
            ),

            html.Div(
                dcc.Graph(figure=scatter),
                style={'width': '33%', 'display': 'inline-block'}
            ),

        ])
    ]
)

# Run app
if __name__ == "__main__":
    app.run(debug=True)