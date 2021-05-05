import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

def randomset_of_mean():

    dataset=[]
    for i in range(0,30):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

sd_arr =[]

for samples in range(0,1000):
    s_mean = randomset_of_mean()
    sd_arr.append(s_mean)


st_dev = statistics.stdev(sd_arr)
mean2 = statistics.mean(sd_arr)

st_dev2 = statistics.stdev(data)
mean3 = statistics.mean(data)

print(sd_arr)
print("standard deviation of sampling distribution:",st_dev)
print("mean of sampling data:" , mean2)
print("standard deviation of whole data:" , st_dev2)
print("mean of whole data:" , mean3)
