from flask import Flask,render_template,request,redirect
from bokeh.plotting import figure, output_file, show
import numpy as np
from bokeh.embed import components

myApp = Flask(__name__)

myApp.vars = {}
myApp.questions = {}
myApp.questions['What do you want to do?'] = ('Calculation','Plot')

def calcFunc(inData):
	return np.square(int(inData))

def myPlot(in1,in2,in3,in4):
	x = [1, 2, 3, 4]
	y = [in1, in2, in3, in4]
	p = figure(title="User-generated line", x_axis_label='User entry index', y_axis_label='User entry value')
	p.line(x, y, legend="User data", line_width = 4)
	return p

'''
To do:
-Add interactivity to Bokeh plot. Choose plot type/color and refresh.
-So I'm not sure how feasible it is to do the interactive plots directly. Sems like its there in the
	doc, but no examples and I'm not smart enough to figure it out... Maybe search it out more?
-A hack-y workaround could be to have radio buttons that do post requests and the default action is
	to refresh the page. This would be the best. Looks like the documentation is changing in
	real-time.
'''


@myApp.route('/main',methods=['GET','POST'])
def main():
	if request.method == 'GET':
		a1, a2 = myApp.questions.values()[0]
		q = myApp.questions.keys()[0]
		return render_template('steeringWheel.html',question=q,ans1=a1,ans2=a2)
	else:
		# It is a POST...
		myApp.vars['radio'] = request.form['swInput']
		if myApp.vars['radio'] == myApp.questions.values()[0][1]: #if user chooses "Plot"
			#return render_template('dataOutput.html',num=myApp.vars['radio'])
			return redirect('/plotLine')
		else:
			return redirect('/calculation')
		

@myApp.route('/')
def init():
	return redirect('/main')



@myApp.route('/plotLine', methods = ['GET','POST'])
def plotPage():
    if request.method == 'GET':
        return render_template('getPlotInfo.html')
    else:
        # request was a POST
        userIn = {'a':request.form['userPlot1'],'b': request.form['userPlot2'],'c': request.form['userPlot3'],'d': request.form['userPlot4']}
        script, div = components(myPlot(userIn['a'],userIn['b'],userIn['c'],userIn['d']))
        return render_template('myGraph.html', script=script, div=div)
        
@myApp.route('/calculation', methods = ['GET','POST'])
def calcPage():
    if request.method == 'GET':
        return render_template('getCalcInfo.html')
    else:
        # request was a POST
        numCalc = calcFunc(int(request.form['userCalc1']))
        return render_template('dataOutput.html',num=numCalc) 

if __name__ == "__main__":
    myApp.run(debug=True)

