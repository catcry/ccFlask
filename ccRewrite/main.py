# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 01:52:49 2022

@author: catcry
"""

from flask import Flask,render_template,request

from ngConfs import ng_conf_gen
#from ngConfs import ng_list_rules
from dbMan import wrt2db,list_rules

app = Flask(__name__)
 
@app.route('/')
def home():
        return render_template('home1.html')

#<td>{{result_list[i][4]}}</td>
#<td>Creation Date</td>


 
@app.route('/rewrite', methods=['POST'])
def loc_post():
    submitted = request.form
    written = wrt2db(submitted)
    response = ng_conf_gen()
    return response
        
@app.route('/list_rules',methods=['POST'])
def list_rules_page(): 
    # if request.method == 'GET':
    #          return f"Return to Home"
    # if request.method == 'POST':
    #          #form_data = request.form
    no_results, result_list = list_rules()
    return render_template('list_rules.html', len = no_results , result_list = result_list )
# @app.route('/data/', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#        # return render_template('data.html',form_data = form_data)
#     return 0

# def amir(x):
#     print (x)
# #a= request.loc
# #print(a) 
# amir(request.loc)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
