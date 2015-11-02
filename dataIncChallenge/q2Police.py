
# coding: utf-8

# In[2]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[3]:

# Read in data in chunks to handle large file size

#tp = pd.read_csv('311_Service_Requests_from_2010_to_Present.csv', iterator=True, chunksize=10000) # gives TextFileReader, which is iteratable with chunks of 10000 rows.
#df = pd.concat(tp, ignore_index=True)


# In[4]:

df.head()


# In[5]:

# Q2.1: What fraction of complaints are associated with the 2nd most popular agency?
comp = df['Agency'].value_counts()
comp[1] / float(sum(comp))


# In[6]:

# Q 2.2: What is the distance (in degrees) between the 90% and 10% 
# percentiles of degrees latitude?

lat = df['Latitude']
lat = lat[ ~np.isnan(lat) ] #Remove NaN
latPc = np.percentile(lat,[0.1,0.9])
print float(np.diff(latPc))


# In[305]:

# Q 2.4: What is the most 'surprising' complaint type when conditioned on a borough? 
# That is, what is the largest ratio of the conditional probability of a complaint 
# type given a specified borough divided by the unconditioned probability of 
# that complaint type?

cplBr = pd.DataFrame(df.groupby(['Complaint Type', 'Borough']).size())
cpl = pd.DataFrame(df.groupby(['Complaint Type']).size())
br = pd.DataFrame(df.groupby(['Borough']).size())


# In[322]:

# Q 2.4 Answer: 

def norm(row):
    return row/sum(row)

condProb = (cplBr/br) 
unCondProb = cpl.apply(norm)

max((condProb/unCondProb)[0])


# In[ ]:




# In[ ]:




# In[7]:

# Q 2.3: What is the difference between the expected number of calls received during the 
# most and least popular whole hours of the day? #(Remove points which do not
# seem to accurately reflect the actual time they were reported.)

callTime = df['Created Date']


# In[8]:

# dt = pd.DataFrame(callTime)


# In[9]:

########################################################################################
# THIS ONE WORKS! Commented out to avoid the expense of rerunning the script
########################################################################################

#dt['ampm'] = dt['Created Date'].str.split().str.get(2) #AM or PM

#dt['mon'] = dt['Created Date'].str.split().str.get(0).str.split('/').str.get(0) #Month
#dt['day'] = dt['Created Date'].str.split().str.get(0).str.split('/').str.get(1) #Day
#dt['yr'] = dt['Created Date'].str.split().str.get(0).str.split('/').str.get(2) #year

#dt['hr'] = dt['Created Date'].str.split().str.get(1).str.split(':').str.get(0) #Hour
#dt['min'] = dt['Created Date'].str.split().str.get(1).str.split(':').str.get(1) #Min
#dt['sec'] = dt['Created Date'].str.split().str.get(1).str.split(':').str.get(2) #Sec




# In[10]:

#dt.groupby(['yr', 'mon']).size()
dt.groupby(['ampm', 'hr']).size()
dt[dt.hr=='12'].groupby(['ampm','min']).size()


# In[11]:

print len(dt[(dt.hr=='12') & (dt.sec == '00') & (dt['min']=='00') & (dt.ampm == 'AM')])
print len(dt[(dt.hr=='12') & (dt.sec == '01') & (dt['min']=='00') & (dt.ampm == 'AM')])


# !2:00:00 AM is 3,512,306
# 12:01:01 AM is 33


# In[12]:

# Remove rows where the time is exactly 12:00:00 AM

exclude = (dt.hr=='12') & (dt.sec == '00') & (dt['min']=='00') & (dt.ampm == 'AM')
dt2 = dt.loc[~exclude,:]

print len(dt[(dt.hr=='12') & (dt.sec == '00') & (dt['min']=='00') & (dt.ampm == 'AM')])
print len(exclude)
print len(dt2)


# In[13]:

#Make sure the lengths are the same
6630738 + 3512306


# In[14]:

#Make sure the midnight data are gone
print len(dt2[(dt2.hr=='12') & (dt2.sec == '00') & (dt2['min']=='00') & (dt2.ampm == 'AM')])
print len(dt2[(dt2.hr=='12') & (dt2.sec == '01') & (dt2['min']=='00') & (dt2.ampm == 'AM')])


# In[15]:

# Find the most/least popular hour for calls
# Min is 4 am; max is 11 am
dt2.groupby(['ampm', 'hr']).size()


# In[355]:

# Q2.3 answer
# Calculate the expected differences

expMax = dt2[ (dt2.ampm == 'AM') & (dt2.hr=='11')].groupby(['mon','day','yr']).count().mean()[0]
expMin = dt2[ (dt2.ampm == 'AM') & (dt2.hr=='04')].groupby(['mon','day','yr']).count().mean()[0]

print 'Expected Max:\n' + str(expMin) + '\n\nExpected Min:\n' +  str(expMax)

print '\nDiff b/w expected min/max:\n' + str(expMax - expMin)
#quantVar = ['health_dental','other_benefits','other_salaries','overtime','retirement','salaries','total_benefits','total_compensation','total_salary']
#df[quantVar] = df[quantVar].astype(float)


# In[349]:

dt2[ (dt2.ampm == 'AM') & (dt2.hr=='04')].groupby(['mon','day','yr']).count()


# In[223]:

# Q2.6 What is the standard deviation in seconds of the time between consecutive 
# calls? (Remove points which do not seem to accurately reflect the actual 
# time they were reported.)

# Reset index for good measure
#dt2 = dt2.reset_index()

#Create a new column
#Should I first create a new index? Then wouldn't need to loop anything...
# df[delta] = df['s'] - df['s' + 1]


# In[231]:

# Figure out how to do datetime on a smaller dataset
test=dt2[0:200]
print test.head()
test['Created Date'].str.split().str.get(2) #AM or PM
test['Created Date'].str.split().str.get(1).str.split(':').str.get(0) #Hour
test['Created Date'].str.split().str.get(0).str.split('/').str.get(0) #Month
test['Created Date'].str.split().str.get(0).str.split('/').str.get(1) #Day

test.loc[:,'ampm'] = test['Created Date'].str.split().str.get(2) #AM or PM
test.loc[:,'h'] = test['Created Date'].str.split().str.get(1).str.split(':').str.get(0) #Hour
test.loc[:,'m'] = test['Created Date'].str.split().str.get(0).str.split('/').str.get(0) #Month
test.loc[:,'d'] = test['Created Date'].str.split().str.get(0).str.split('/').str.get(1) #Day
test.head()


# In[234]:

from datetime import datetime
from datetime import timedelta

date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

temp1 = ' '.join(list(test.loc[1][['mon','day','yr','hr','min','sec','ampm']]))
temp2 = ' '.join(list(test.loc[2][['mon','day','yr','hr','min','sec','ampm']]))

t1 = datetime.strptime(temp, '%m %d %Y %I %M %S %p')
t2 = datetime.strptime(temp2, '%m %d %Y %I %M %S %p')

#%m %d %Y %I %M %S %p
#timedelta(t1,t2)


# In[90]:

############ Need this one to get the data in datetime form ###########

#dtime = [datetime.strptime(' '.join(list(dt2.iloc[i][['mon','day','yr','hr','min','sec','ampm']])), '%m %d %Y %I %M %S %p') for i in range(len(dt2))]
#dt2.loc[:,'dTime'] = dtime
#dt2.loc[:,'dTimeF'] = dt2['dTime'].shift()
#works
#[' '.join(list(test.loc[i][['mon','day','yr','hr','min','sec','ampm']])) for i in range(4)]


# In[203]:

# Q2.6: What is the standard deviation in seconds of the time between consecutive calls?

#tx = [(dt2.iloc[i]['dTimeF']-dt2.iloc[i]['dTime']).seconds for i in range(1,len(dt2))]
#dt2.loc[range(1,len(dt2)), 'delta'] = tx

#dt2['delta']=(dt2['dTimeF']-dt2['dTime']).seconds


# In[229]:

# Q2.6 answer:
np.std(dt2.loc[range(1,len(dt2))]['delta'])


# In[326]:

# Q2.5: Let's estimate the area that 311 supports. Suppose calls 
# are 2D normally distributed on the surface of the earth 
#with mean and standard deviation given by those of the
#latitude and longitude. How many square kilometers is the 
#single-standard-deviation ellipse?


np.std(df)


# In[350]:

#df.loc[1:4,'Latitude']
lt = df.loc[:,'Latitude']
lt = lt.loc[~np.isnan(lt)]
lt

lg = df.loc[:,'Latitude']
lg = lg.loc[~np.isnan(lg)]
lg

lgStd = np.std(lg)
ltStd = np.std(lt)
ltMn  = np.mean(lt)

print 'std dev of latitude:\n' + str(ltStd)
print '\n\nstd dev of longitude:\n' + str(lgStd)
print '\n\nmean of longitude:\n' + str(ltMn)

#print lt.loc[~np.isnan(lt)]
#np.isnan(~df.loc[1:4,'Latitude'])


# In[361]:

# Area of ellipoid: A = π * a * b
# From http://stackoverflow.com/questions/1253499/simple-calculations-for-working-with-lat-lon-km-distance

# Latitude: 1 deg = 110.574 km
# Longitude: 1 deg = 111.320*cos(latitude) km

callArea = np.pi * (ltStd * 110.574) * (ltStd * 111.320 * np.cos(ltMn*np.pi/180))


# In[362]:

# Answer to 2.5:
callArea

