import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
print("Mean of the population are:-", mean)

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_means(100)
    mean_list.append(set_of_means)
mean = statistics.mean(mean_list)
std_dev = statistics.stdev(mean_list)
print("Mean of sampling distribution:", mean)
print("Standard Deviation of sampling distribution:", std_dev)

first_std_deviation_start, first_std_deviation_end = mean-std_dev, mean+std_dev
second_std_deviation_start, second_std_deviation_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_dev), mean+(3*std_dev)

fig= ff.create_distplot([mean_list],["maths_score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17], mode="lines", name="mean"))

fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="Std.Deviation1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="Std.Deviation2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="Std.Deviation3"))

fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Std.Deviation4"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="Std.Deviation5"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="Std.Deviation6"))

fig.show()
