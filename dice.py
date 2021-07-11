import random
import plotly.express as px
import plotly.figure_factory as ff 

result = []
count = []

for i in range(0, 100):
    die1 = random.randint(1, 6)

    result.append(die1)
    count.append(i)

figure = ff.create_distplot([result], ["Result"], show_hist=False)
figure.show()