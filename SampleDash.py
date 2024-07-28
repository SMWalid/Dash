import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample DataFrame
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [450, 250, 300, 550],
    "Colors": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
}
df = pd.read_csv('C:\Python\Dash\dataSet.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # For deploying

# App layout
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '20px'}, children=[
    html.H1(
        children='My Dash App',
        style={'textAlign': 'center', 'color': '#ff7f0e'}
    ),

    html.Div(children='A simple Dash app with a colorful dashboard.', style={
        'textAlign': 'center', 'color': '#555', 'marginBottom': '30px'
    }),

    dcc.Graph(
        id='bar-chart',
        config={'displayModeBar': False}
    ),

    html.Div([
        dcc.Slider(
            id='slider',
            min=0,
            max=10,
            step=1,
            marks={i: str(i) for i in range(11)},
            value=5,
        )
    ], style={'marginTop': '30px'}),
])

# Callback to update bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('slider', 'value')]
)
def update_bar_chart(slider_value):
    # Update data based on slider value
    updated_df = df.copy()
    updated_df['Values'] = df['Values'] * (slider_value / 5)

    # Create bar chart
    fig = px.bar(
        updated_df,
        x='Category',
        y='Values',
        color='Category',
        text='Values',
        color_discrete_sequence=updated_df['Colors'],
        title='Category Values'
    )
    
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='#f9f9f9',
        font_color='#333',
        title_x=0.5
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)