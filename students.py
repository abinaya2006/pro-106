import plotly_express as px
import csv
import numpy as np

'''
with open ("Student Marks vs Days Present.csv") as file_data:
    df=csv.DictReader(file_data)

    fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
    fig.show()
'''


def getDataSource(data_path):
    days_present=[]
    marks_in_percentage=[]

    with open(data_path) as a:
        df=csv.DictReader(a)

        for row in df:
            days_present.append(float(row["Days Present"]))
            marks_in_percentage.append(float(row["Marks In Percentage"]))
        
    return {"x":days_present,"y":marks_in_percentage}


def find_correlation(data):
    correlation=np.corrcoef(data["x"],data["y"])
    print("Correlation between days present and marks : ",correlation[0,1] )

def setup():
    data_path="Student Marks vs Days Present.csv"
    data=getDataSource(data_path)
    find_correlation(data)

setup()
