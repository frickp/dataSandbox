from flask import Flask,render_template,request,redirect
myApp = Flask(__name__)
myApp.vars={}

myApp.questions={}
myApp.questions['who are you?'] = ['me','you','him','her'] 
myApp.questions['why are you here?'] = ['trying to learn','nothing else to do',"what's it to ya?"]
myApp.questions['Is this your favorite app?'] = ['Yes','Definitely','Obviously','All of the above'] 
