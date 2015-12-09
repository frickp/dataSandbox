def plotPCA(myData,dpt1,dpt2,xVar,yVar,legLoc="bottom_left"):

    from bokeh.plotting import figure, output_file, show, ColumnDataSource, output_notebook
    from bokeh.models import HoverTool, Select

    output_notebook()
    
    newData = myData
    nAll = newData    
    n1 = newData[newData['department_code']==dpt1]
    n2 = newData[newData['department_code']==dpt2]

    sAll = ColumnDataSource(
            data=dict(
                x = nAll[xVar],
                y = nAll[yVar],
                totSal = nAll['total_salary'],
                totCom = nAll['total_compensation'],
                dept = nAll['department'],
                totBen = nAll['total_benefits'],
                job = nAll['job']
            )
        )

    s1 = ColumnDataSource(
            data=dict(
                x = n1[xVar],
                y = n1[yVar],
                totSal = n1['total_salary'],
                totCom = n1['total_compensation'],
                dept = n1['department'],
                totBen = n1['total_benefits'],
                job = n1['job']
            )
        )

    s2 = ColumnDataSource(
            data=dict(
                x = n2[xVar],
                y = n2[yVar],
                totSal = n2['total_salary'],
                totCom = n2['total_compensation'],
                dept = n2['department'],
                totBen = n2['total_benefits'],
                job = n2['job']
            )
        )

    p = figure(plot_width=500, plot_height=400, tools="hover,pan,box_zoom,reset,save",
               title="PCA of SF employees", y_axis_label = yVar,
               x_axis_label = xVar)

    hover = p.select(dict(type=HoverTool))


    hover.tooltips = [
        ("Dept", "@dept"),
        ("Job", "@job"),
        ("Tot comp ($)", "@totCom"),
        ("Tot sal ($)", "@totSal"),
        ("Tot bnft ($)","@totBen")
    ]

    p.circle('x', 'y', size=4, legend="All", source=sAll,fill_color=None, line_color="black",alpha=0.4)
    p.circle('x', 'y', size=4, legend=dpt1, source=s1,color='darkcyan',alpha=0.6)
    p.circle('x', 'y', size=4, legend=dpt2, source=s2,color='red',alpha=0.6)

    p.legend.orientation = legLoc

    show(p)

def plotScatter(myData,dpt1,dpt2,xVar,yVar,legLoc="bottom_left"):

    from bokeh.plotting import figure, output_file, show, ColumnDataSource, output_notebook
    from bokeh.models import HoverTool, Select

    output_notebook()
    
    df = myData
    nAll = df
    n1 = df[df['department_code']==dpt1]
    n2 = df[df['department_code']==dpt2]

    sAll = ColumnDataSource(
            data=dict(
                x = nAll[xVar],
                y = nAll[yVar],
                totSal = nAll['total_salary'],
                totCom = nAll['total_compensation'],
                dept = nAll['department'],
                totBen = nAll['total_benefits'],
                job = nAll['job']
            )
        )

    s1 = ColumnDataSource(
            data=dict(
                x = n1[xVar],
                y = n1[yVar],
                totSal = n1['total_salary'],
                totCom = n1['total_compensation'],
                dept = n1['department'],
                totBen = n1['total_benefits'],
                job = n1['job']
            )
        )

    s2 = ColumnDataSource(
            data=dict(
                x = n2[xVar],
                y = n2[yVar],
                totSal = n2['total_salary'],
                totCom = n2['total_compensation'],
                dept = n2['department'],
                totBen = n2['total_benefits'],
                job = n2['job']
            )
        )

    p = figure(plot_width=500, plot_height=400, tools="hover,pan,box_zoom,reset,save",
               title="SF public employee salaries", y_axis_label = yVar,
               x_axis_label = xVar)

    hover = p.select(dict(type=HoverTool))


    hover.tooltips = [
        ("Dept", "@dept"),
        ("Job", "@job"),
        ("Tot comp ($)", "@totCom"),
        ("Tot sal ($)", "@totSal"),
        ("Tot bnft ($)","@totBen")
    ]

    p.circle('x', 'y', size=5, legend="All", source=sAll,fill_color=None, line_color="black",alpha=0.4)
    p.circle('x', 'y', size=5, legend=dpt1, source=s1,color='darkcyan',alpha=0.6)
    p.circle('x', 'y', size=5, legend=dpt2, source=s2,color='red',alpha=0.6)

    p.legend.orientation = legLoc

    show(p)
