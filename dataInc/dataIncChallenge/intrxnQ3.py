#THIS IS IN DEVELOPMENT

#Dependencies...


# Define the app as class Flask
app = Flask(__name__)

# Initialize some variables within "app"
app.vars = {}




# Function to plot user input. Based on this link
# http://bokeh.pydata.org/en/0.10.0/docs/user_guide/plotting.html#single-lines
def myPlot(in1,in2,in3,in4):
	x = [1, 2, 3, 4]
	y = [in1, in2, in3, in4]
	p = figure(title="User-generated line", x_axis_label='Entry index', y_axis_label='Entry value')
	p.line(x, y, legend="User data", line_width = 4)
	return p



@app.route('/')
def init():
	return redirect('/main')


@app.route('/main',methods=['GET','POST'])
def main():
	if request.method == 'GET':
		a1, a2 = app.questions.values()[0]
		q = app.questions.keys()[0]
		return render_template('steeringWheel.html',question=q,ans1=a1,ans2=a2)
	else:
		# It is a POST...
		app.vars['radio'] = request.form['swInput']
		if app.vars['radio'] == app.questions.values()[0][1]: #if user chooses "Plot"
			#return render_template('dataOutput.html',num=app.vars['radio'])
			return redirect('/plotLine')
		else:
			return redirect('/calculation')
		
@app.route('/calculation', methods = ['GET','POST'])
def calcPage():
    if request.method == 'GET':
        return render_template('getCalcInfo.html')
        #Is there any way for me to see if the radio is on or off?
    else:
        # request was a POST
        numCalc = calcFunc(int(request.form['userCalc1']))
        return render_template('dataOutput.html',num=numCalc) 

@app.route('/plotLine', methods = ['GET','POST'])
def plotPage():
    if request.method == 'GET': #What if the get request renders the plot and the post request updates the 
        return render_template('getPlotInfo.html')
    else: #Do I turn this into a redirect?
        # request was a POST
        userIn = {'a':request.form['userPlot1'],'b': request.form['userPlot2'],'c': request.form['userPlot3'],'d': request.form['userPlot4']}
        script, div = components(myPlot(userIn['a'],userIn['b'],userIn['c'],userIn['d']))
        return render_template('myGraph.html', script=script, div=div)
        
if __name__ == "__main__":
    app.run(debug=True)
    
if __name__ == '__main__':
    app.run(port=33507)

