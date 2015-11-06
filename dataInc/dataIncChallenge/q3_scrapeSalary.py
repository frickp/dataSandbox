# Script for Data Incubator q3:
# Written by Peter Frick

# In[1]:

get_ipython().magic(u'matplotlib inline')
import requests
import json
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import requests


# In[2]:

URL = "https://data.sfgov.org/resource/88g8-5mnd.json"

########## Some other data sources that may be interesting for the future. #############
#URL = "http://www.zillow.com/webservice/GetSearchResults.htm?" + "zws-id=" + "X1-ZWz1ezwkcmsft7_1651t" + \
#"&address=" + "san-francisco"
#URL = "https://api.data.gov/ed/collegescorecard/v1/schools/?sort=2011.earnings.6_yrs_after_entry.percent_greater_than_25000%3Adesc&school.operating=1&2013.student.size__range=0..&school.degrees_awarded.predominant=3&fields=id%2Cschool.name%2Cschool.city%2Cschool.state%2C2013.student.size%2Cschool.ownership%2Cschool.degrees_awarded.predominant%2C2013.cost.avg_net_price.overall%2C2013.completion.rate_suppressed.overall%2C2011.earnings.10_yrs_after_entry.median%2C2011.earnings.6_yrs_after_entry.percent_greater_than_25000%2Cschool.under_investigation&api_key=Xxf2NKtwfcXUd8K2hqawnlur6c0YY93xsNFwq0Dy"
#URL = "https://data.sfgov.org/resource/mjr8-p6m5.json"
#URL = "http://data.consumerfinance.gov/api/views/s6ew-h6mp.json"
#URL = "http://gis.ers.usda.gov/arcgis/rest/services/"
#URL = "http://api.data.gov/ed/collegescorecard/v1/schools"


# In[3]:

response = requests.get(URL)
response.raise_for_status()
data = response.json()


# In[4]:

#df = pd.DataFrame(data)
#df.columns


# In[5]:

#print data[0]
df = pd.DataFrame.from_dict(data)
#isinstance((data[0]), dict)


# In[6]:

quantVar = ['health_dental','other_benefits','other_salaries','overtime','retirement','salaries','total_benefits','total_compensation','total_salary']
df[quantVar] = df[quantVar].astype(float)

df = df.sort_values(by='total_compensation')
df = df.reset_index()
df.head()


# In[7]:

dList = range(9)
fig = plt.figure(figsize=(10,9), dpi=1600)
fig.suptitle('Overview of the data',fontsize=15,y=1.08,fontweight='bold')

#Function to make a single plot
def multiPlot(myData):    
    ax=plt.subplot2grid((ncol,nrow),(yPanel,xPanel))
    ax.hist(df[quantVar[myData]],alpha=0.5)#alpha??
    ax.set_xlabel(quantVar[myData],fontsize=14,fontweight='bold')
    #ax.set_ylabel('Y',fontsize=14,fontweight='bold',rotation='Vertical')
    plt.locator_params(axis = 'x', nbins = 2)
    ax.tick_params(labelsize=14)

#Script to add plots to multipanel figure
xPanel = 0; yPanel = 0; ncol = 3; nrow = 3; legIdx=0
#plt.tight_layout()
for i in dList:
    multiPlot(i)
    xPanel=xPanel+1; legIdx=legIdx+1
    if xPanel>(nrow-1):
        xPanel=0
        yPanel=yPanel+1


fig.tight_layout()


# In[8]:

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


# In[10]:

from bokeh.plotting import figure, output_file, show, ColumnDataSource, output_notebook
from bokeh.models import HoverTool, Select

output_notebook()

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

show(p)


# For the second Bokeh plot, I want to do some PCA on the data. The first step is to center the data. I'm scaling it to draw out the differences in data shape. Then calculate explained variance, etc

# In[13]:

from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

dfs = pd.DataFrame(scale(df[quantVar],with_std=True),columns=df[quantVar].columns)

dfResp = dfs['total_compensation']
pred = [quantVar[i] for i in range(len(quantVar)) if quantVar[i] != 'total_compensation']
dfPred = dfs[pred]

pca = PCA()
pca.fit(dfPred)

expVar = pca.explained_variance_ratio_
plt.bar(range(len(expVar)),expVar,alpha=0.5)


# Project the data onto the principal components.

# In[14]:

#New data in PC space
newData = pd.DataFrame(pca.transform(dfPred),columns=['PC' + str(i+1) for i in range(len(expVar))])

#Keep annotations from original data. Indices should be the same.
dfAnno = df[['total_compensation','total_salary','department','total_benefits','job','department_code']]
newData = pd.concat([newData, dfAnno], axis=1)

#Subsets used for plotting
nAll = newData    
nPol = newData[newData['department_code']=='POL']
nFir = newData[newData['department_code']=='FIR']
nMta = newData[newData['department_code']=='MTA']    


# Now, let's visualize the data using principal components.

# In[15]:

from bokeh.plotting import figure, output_file, show, ColumnDataSource, output_notebook
from bokeh.models import HoverTool, Select
from bokeh.io import output_file, show, vform
from bokeh.models.widgets import CheckboxGroup
from bokeh.resources import CDN
from bokeh.embed import file_html

output_notebook()

#output_file("salarySF.html")

checkbox_group = CheckboxGroup(
       labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])


#Not creative enough. I think I could just make a new source for each dept...
sAll = ColumnDataSource(
        data=dict(
            x = nAll['PC1'],
            y = nAll['PC2'],
            totSal = nAll['total_salary'],
            totCom = nAll['total_compensation'],
            dept = nAll['department'],
            totBen = nAll['total_benefits'],
            job = nAll['job']
        )
    )

sPol = ColumnDataSource(
        data=dict(
            x = nPol['PC1'],
            y = nPol['PC2'],
            totSal = nPol['total_salary'],
            totCom = nPol['total_compensation'],
            dept = nPol['department'],
            totBen = nPol['total_benefits'],
            job = nPol['job']
        )
    )

sFir = ColumnDataSource(
        data=dict(
            x = nFir['PC1'],
            y = nFir['PC2'],
            totSal = nFir['total_salary'],
            totCom = nFir['total_compensation'],
            dept = nFir['department'],
            totBen = nFir['total_benefits'],
            job = nFir['job']
        )
    )

sMta = ColumnDataSource(
        data=dict(
            x = nMta['PC1'],
            y = nMta['PC2'],
            totSal = nMta['total_salary'],
            totCom = nMta['total_compensation'],
            dept = nMta['department'],
            totBen = nMta['total_benefits'],
            job = nMta['job']
        )
    )

p = figure(plot_width=800, plot_height=500, tools="hover,pan,box_zoom,reset,save",
           title="SF public employee salaries", y_axis_label = "Principal Component 2",
           x_axis_label = "Principal Component 1")

hover = p.select(dict(type=HoverTool))


hover.tooltips = [
    ("Dept", "@dept"),
    ("Job", "@job"),
    ("Tot comp ($)", "@totCom"),
    ("Tot sal ($)", "@totSal"),
    ("Tot bnft ($)","@totBen")
]

p.circle('x', 'y', size=8, legend="All", source=sAll,fill_color=None, line_color="black",alpha=0.4)
p.circle('x', 'y', size=8, legend="MTA", source=sMta,color='blue',alpha=0.4)
p.circle('x', 'y', size=8, legend="SF Police", source=sPol,color='red',alpha=0.4)
p.circle('x', 'y', size=8, legend="SF Fire", source=sFir,color='orange',alpha=0.4)

p.legend.orientation = "bottom_left"

#html = file_html(p, CDN, "my plot")

show(p)


# So, as before, the Fire Department has a higher total compensation. This is reflected by the rightward skew of the orange dots (higher in PC1). Looks like PC2 is separating the Fire Department from another high pay group above. Let's look at the loadings to see what is driving this difference.

# In[16]:

pca.components_[range(2)]


# Looking at the PCA scores between PCA 1 and 2 shows that the 3rd, 4th entry are quite different between the PCs. Let's take a look at what they are.

# In[17]:

dfPred.head()


# The loadings show us that the SF fire department has a generally higher total compensation, with relatively less overtime and other salary.
