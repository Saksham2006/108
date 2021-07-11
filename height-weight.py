import plotly.figure_factory as ff
import pandas as pd

data = pd.read_csv('data.csv')
figure = ff.create_distplot([data['Weight(Pounds)'].tolist()], ["Weight"], show_hist=False)
figure.show()