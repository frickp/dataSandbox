
#Purpose

This is the first iPython notebook I'm adding online. The goal of this notebook is more to learn the syntax, etc.
For example, one asterisk makes text *italic*. Two asterisks makes text **bold**. Putting 2 dollar signs before and after an expression gives an equation:

$$y=10*x$$

An equation can be displayed inline with the text by adding a single dollar sign on
either side of the expression, like so: $y=sin(x)$
    
This is a good website to remember for markdown:
http://nestacms.com/docs/creating-content/markdown-cheat-sheet
    
And for when you come up with something quotable, use a greater-than key
> Be inspired!

Okay, now on to some plots!
*First*, load the dependencies


    import pandas as pd
    import numpy as np
    import matplotlib as plt
    import pylab as pl
    from sklearn import linear_model
    #import statsmodels.api as sm
    %matplotlib inline

Now generate a dataset of a line with some noise built in and see what it looks like...


    #Set a randomization seed for reproducibility
    np.random.seed(1)
    d = np.arange(0,10,0.1)
    df = pd.DataFrame({'x': d})
    df['y']=df['x']*0.5+2 + np.random.randn(len(d))


    pl.plot(df['x'],df['y'])




    [<matplotlib.lines.Line2D at 0x10ec541d0>]




![png](migratingOnline_files/migratingOnline_4_1.png)



    m=sm.OLS(df['y'],df['x']).fit()
    print m.conf_int()
    #m.summary()

              0         1
    x  0.773937  0.864305



    #m=linear_model.LinearRegression()
    #m.fit(df['x'],df['y'])
    

