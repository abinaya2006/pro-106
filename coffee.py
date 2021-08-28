from numpy.lib.function_base import corrcoef
import plotly_express as px
import csv 
import numpy as np

'''
with open("cups of coffee vs hours of sleep.csv") as a:
    df=csv.DictReader(a)

    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()

'''
def getDataSource(data_path):
    coffee=[]
    sleep=[]

    with open(data_path) as a:
        df=csv.DictReader(a)

        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x":coffee,"y":sleep}

def find_correlation(data):
    correlation=np.corrcoef(data["x"],data["y"])

    print("Correlation between cups of coffee and hours of sleep : ",correlation[0,1])

def setup():
    data_path="cups of coffee vs hours of sleep.csv"
    data=getDataSource(data_path)

    find_correlation(data)

setup()

