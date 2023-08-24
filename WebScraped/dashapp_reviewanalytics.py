from dash import Dash, html, dcc 
import plotly.express as px
import pandas as pd 

class start_app:
    def __init__(self,csv_File,debug=True):
        data_reviews = pd.read_csv(csv_File)
        web_links = pd.unique(data_reviews['Website Link'])
        review_num = []
        for link in web_links: review_num.append(data_reviews[data_reviews['Website Link']==link].Review.shape[0])

    def get_App(self):
        app = Dash(__name__)
        return app

    def bar_graph(self):
        fig = px.bar(self.data_reviews,x=self.web_links,y=self.review_number)
        return fig 
    
    def run_app(self):
        self.app.run(debug=True)
        self.app.layout = html.Div(children=[
                html.H1(children="Barakat Customer Reviews"),
                html.Div(children='Customer review count against website links'),
                dcc.Graph(
                    id = 'review_count_bar_graph',
                    figure=self.bar_graph()
                )
        ])

if __name__ == '__main__':
    analytics = start_app('bkreview.csv')
    analytics.run_app()
