# Script for Data Incubator q1:
# Written by Peter Frick

# In[1]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.utils import resample


# In[19]:

#This is the good stuff!

time = 100
xRand = np.random.randint(0, high = 2, size = time)
yRand = np.random.randint(0, high = 2, size = time)
print xRand
xSteps = np.where(xRand == 1, 1, -1)
ySteps = np.where(yRand == 1, 1, -1)
print xSteps
xPos = np.cumsum(xSteps)
yPos = np.cumsum(ySteps)
print xPos
print yPos


# In[20]:

time = 100
xRand = np.random.randint(0, high = 2, size = time)
yRand = np.random.randint(0, high = 2, size = time)
print xRand
xSteps = np.cumsum(np.where(xRand == 1, 1, -1))
ySteps = np.cumsum(np.where(yRand == 1, 1, -1))
print xSteps
xPos = np.cumsum(xSteps)
yPos = np.cumsum(ySteps)
print xPos
print yPos


# In[21]:

def randWalk(time):
    xRand = np.random.randint(0, high = 2, size = time) #simulate binary outcome
    yRand = np.random.randint(0, high = 2, size = time)
    xPos = np.cumsum(np.where(xRand == 1, 1, -1))
    yPos = np.cumsum(np.where(yRand == 1, 1, -1))
    return xPos, yPos
a,b = randWalk(10)
print a
print b


# In[22]:

np.random.rand(6,6)


# In[23]:

# This function returns the fraction of times that distance >= 3 on the tenth move,
# over a certain number (numDraw) of random walks

# I think what I need to do here is to create a matrix. One dimension is the draws for the
# current walk. The second dimension is the draws for every subsequent walk.

def greaterThree(numDraws):
    j = 1
    countCrow3 = 0 
    while j <= numDraws: 
        x, y = randWalk(numDraws)
        x10, y10 = x[9], y[9]
        dist = np.sqrt(np.square(x10) + np.square(y10))
        if dist >= 3:
            countCrow3 += 1
        j += 1
    return countCrow3/float(j)
greaterThree(100)



# In[24]:

max = 0.5
while i < 10:
    x = max(np.random.rand(50))
    print x
    if x > max:
        x = max
    i += 1



# In[25]:

m = np.matrix(np.random.randn(50).reshape((5,10)))
m = np.random.randn(50).reshape((5,10))
#len(np.random.randn(50))


# In[26]:

s = np.array([[4,5,6,4,7],
 [7, 6, 4, 4, 7],
 [6, 7, 4, 5, 6]]).reshape((3,5))
print s
s2 = np.where(s<6,0,s)
print s2
s2[s2 == np.max(s2)] = -1
s2[s2 == np.max(s2)] = 1
s2
#np.where(s != 0 & s == 6,1,-1)
#?np.where


# In[5]:

#This is most recent (1:45)

#np.random.randint(0, high = 4, size = 100)
def randWalk(moves,samples):
    draws = np.random.randint(4, high = 8, size = samples*moves).reshape((samples,moves))
    xSteps = np.where(draws<6,0,draws)
    xSteps[xSteps == np.max(xSteps)] = -1
    xSteps[xSteps == np.max(xSteps)] = 1
    
    ySteps = np.where(draws>5,0,draws)
    ySteps[ySteps == np.max(ySteps)] = -1
    ySteps[ySteps == np.max(ySteps)] = 1
    
    xPos = np.cumsum(xSteps, axis=1)
    yPos = np.cumsum(ySteps, axis=1)
    return xPos, yPos
    
randWalk(5,3)


# In[2]:

# Question 1.1:

def crow3(moves,samples):
    x, y = randWalk(moves=moves,samples=samples)
    x10 = x[:,9]; y10 = y[:,9] #get the x,y position after the tenth step
    m10 = np.sqrt(np.square(x10) + np.square(y10)) #calculate the distance from origin 
    d = len(m10[m10>3])/float(len(m10)) #return the probability
    return d



# In[ ]:

# Q1.1 answer

# crow3(10,200000)   0.452265 
# crow3(10,2000000)  0.4541365
# crow3(10,20000000) 0.4541023
#crow3(10,2000000000)


# In[6]:

# Question 1.2: 

def ever5(moves,samples):
    x, y = randWalk(moves=moves,samples=samples)
    distMat = []
    for i in range(10):
        xi = x[:,i]; yi = y[:,i] #get the x,y position after the tenth step
        mi = np.sqrt(np.square(xi) + np.square(yi)) #calculate the distance from origin 
        distMat.append(mi)
    distMat = np.matrix(distMat)
    maxDist = np.amax(distMat,axis=0)
    return maxDist[maxDist>=5].shape[1]/float(maxDist.shape[1])


# In[8]:

#Q 1.2 answer
#ever5(moves=10, samples=5000000)  0.133442


# In[9]:

# Question 1.3 
# What is the probability that the tourist is ever east of East 1st Avenue 
# but ends up west of West 1st Avenue in 10 moves?

# To find this, I should look for rows where x is < -1 and ends at > 1

def e1w1(moves,samples):
    x, y = randWalk(moves=moves,samples=samples)
    e1 = np.amin(x,axis=1) < -1
    w1 =  x[:,9] > 1
    ew = e1 & w1
    return len(ew[ew==True])/float(len(ew))
    
#e1w1(10,10)


# In[11]:

#Q1.3 Answer
#e1w1(10,1000000) 0.005808


# In[473]:

# Q1.4
# What is the average number of moves until the first time the tourist is at least 10
# city blocks (as the crow flies) from Broadway and Broadway.

def til10(moves,samples,maxVal):
    x, y = randWalk(moves=moves,samples=samples)
    distMat = []
    for i in range(moves):
        xi = x[:,i]; yi = y[:,i] #get the x,y position after the tenth step
        mi = np.sqrt(np.square(xi) + np.square(yi)) #calculate the distance from origin 
        distMat.append(mi)
    distMat = np.matrix(distMat)
    #print distMat
    normDistMat = np.where(distMat >= maxVal,maxVal,distMat)
    dMax = np.max(normDistMat, axis=0)
    #print dMax == 10
    #print dMax
    dMoves = np.argmax(normDistMat, axis=0)
    #print 'number of steps:'
    #print dMoves
    #print 'Keep only walks that exceed 10'
    filtMoves = dMoves[dMax == maxVal]
    #print filtMoves
    print np.mean(filtMoves)


# In[474]:

# Q1.4 Answer:
til10(moves=1000,samples=50000,maxVal=10)       #103.81312


# In[477]:

# Q1.8 Answer:
# til10(moves=100000,samples=500,maxVal=60)     #3541.1


# In[398]:

# q 1.5: What is the probability that the tourist is ever at least 10 city 
# blocks (as the crow flies) from Broadway and Broadway within 60 moves?


def til10within60(moves,samples):
    x, y = randWalk(moves=moves,samples=samples)
    distMat = []
    for i in range(moves):
        xi = x[:,i]; yi = y[:,i] #get the x,y position after the tenth step
        mi = np.sqrt(np.square(xi) + np.square(yi)) #calculate the distance from origin 
        distMat.append(mi)
    distMat = np.matrix(distMat)
    #print distMat
    normDistMat = np.where(distMat>=10,10,distMat)
    #print normDistMat
    #maxDist = np.amax(distMat,axis=0)
    #print maxDist
    #print 'argmax'
    dMax = np.max(normDistMat,axis=0)
    #print dMax == 10
    #print dMax
    dMoves = np.argmax(normDistMat,axis=0)
    #print normDistMat.shape
    #print 'number of steps:'
    #print dMoves
    #print 'Keep only walks that exceed 10'
    filtMoves = dMoves[dMax == 10]
    return len(filtMoves)/float(len(dMoves))
    #print np.mean(filtMoves)




# In[400]:

# Q1.5 Answer:
# til10within60(60,1000000) 0.318354


# In[449]:

# Q1.6: What is the probability that the tourist is at least 10 city blocks 
# (as the crow flies) from Broadway and Broadway after 60 moves?

def til10after60(moves,samples):
    x, y = randWalk(moves=moves,samples=samples)
    distMat = []
    for i in range(moves):
        xi = x[:,i]; yi = y[:,i] #get the x,y position after the tenth step
        mi = np.sqrt(np.square(xi) + np.square(yi)) #calculate the distance from origin 
        distMat.append(mi)
    distMat = np.matrix(distMat)
    normDistMat = np.where(distMat >= 10,10,distMat)
    m60 = normDistMat[59,:]    
    return np.count_nonzero(m60 == 10)/float(samples)


# In[458]:

# Q1.6 answer:
# til10after60(moves=60,samples=100000)   0.20678


# In[470]:

# q 1.7 What is the probability that the tourist is ever east of East 1st Avenue 
# but ends up west of West 1st Avenue in 30 moves?

# Question 1.3 
# What is the probability that the tourist is ever east of East 1st Avenue 
# but ends up west of West 1st Avenue in 10 moves?

# To find this, I should look for rows where x is < -1 and ends at > 1

def e1w1(moves,samples):
    x, y = randWalk(moves=moves,samples=samples)
    e1 = np.amin(x,axis=1) < -1
    w1 =  x[:,29] > 1
    ew = e1 & w1
    return len(ew[ew==True])/float(len(ew))
    


# In[472]:

# Q1.7 answer
#e1w1(30,1000000) #        0.07763


# In[ ]:



