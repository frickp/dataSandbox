%matplotlib inline
import requests
import json
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import requests

URL = "https://data.sfgov.org/resource/88g8-5mnd.json"

response = requests.get(URL)
response.raise_for_status()
data = response.json()

df = pd.DataFrame.from_dict(data)

quantVar = ['health_dental','other_benefits','other_salaries','overtime','retirement','salaries','total_benefits','total_compensation','total_salary']
df[quantVar] = df[quantVar].astype(float)

df = df.sort_values(by='total_compensation')
df = df.reset_index()

totComp = df['total_compensation']
t = range(len(totComp))
j = df['department']
j = df['department']
jc = df['department_code']

dfPol = df[df['department_code']=='POL']
dfFir = df[df['department_code']=='FIR']
dfMta = df[df['department_code']=='MTA']

polIdx = [i for i in np.where(df['department_code']=='POL')[0]]
firIdx = np.where(df['department_code']=='FIR')[0]
mtaIdx = np.where(df['department_code']=='MTA')[0]

from bokeh.plotting import figure, output_file, show, ColumnDataSource, output_notebook
from bokeh.models import HoverTool, Select
from bokeh.embed import components 

#output_notebook()

sAll = ColumnDataSource(
        data=dict(
            x = df.index,
            y = df['total_compensation'],
            totSal = df['total_salary'],
            dept = df['department'],
            totBen = df['total_benefits'],
            job = df['job']
        )
    )

sPol = ColumnDataSource(
        data=dict(
            x = dfPol.index,
            y = dfPol['total_compensation'],
            totSal = dfPol['total_salary'],
            dept = dfPol['department'],
            totBen = dfPol['total_benefits'],
            job = dfPol['job']
        )
    )

sFir = ColumnDataSource(
        data=dict(
            x = dfFir.index,
            y = dfFir['total_compensation'],
            totSal = dfFir['total_salary'],
            dept = dfFir['department'],
            totBen = dfFir['total_benefits'],
            job = dfFir['job']
        )
    )

sMta = ColumnDataSource(
        data=dict(
            x = dfMta.index,
            y = dfMta['total_compensation'],
            totSal = dfMta['total_salary'],
            dept = dfMta['department'],
            totBen = dfMta['total_benefits'],
            job = dfMta['job']
        )
    )

p = figure(plot_width=800, plot_height=500, tools="hover,pan,box_zoom,reset,save",
           title="SF public employee salaries", y_axis_label = "Total compensation",
           x_axis_label = "Sorted employee index")

hover = p.select(dict(type=HoverTool))


hover.tooltips = [
    ("Dept", "@dept"),
    ("Job", "@job"),
    ("Tot comp ($)", "@y"),
    ("Tot sal ($)", "@totSal"),
    ("Tot bnft ($)","@totBen")
]

p.circle('x', 'y', size=8, legend="All", source=sAll,fill_color=None, line_color="black",alpha=0.2)
p.circle('x', 'y', size=8, legend="MTA", source=sMta,color='blue',alpha=0.4)
p.circle('x', 'y', size=8, legend="SF Police", source=sPol,color='red',alpha=0.4)
p.circle('x', 'y', size=8, legend="SF Fire", source=sFir,color='orange',alpha=0.4)

p.legend.orientation = "top_left"

#show(p)

script, div = components(p)
return render_template('graph.html', script=script, div=div)
