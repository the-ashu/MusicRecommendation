import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request
import fook
#creating instance of the class
app=Flask(__name__)
loaded_model = pickle.load(open("similar.pkl","rb"))
loaded_model_2 = pickle.load(open("popular.pkl","rb"))
#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    # return render_template('index.html')    
    result = loaded_model_2.recommend_p('9bb911319fbc04f01755814cb5edb21df3d1a336');
    # return result.values.to_list();
    return render_template("index.html",foobar=result)
    # return(len(result));
    #return "Hello World"

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        song_name = request.form.get("song_name")
        # return song_name
        result = loaded_model.similar_items(song_name); 
        return render_template("index.html",foobar=result)


@app.route('/user')
def user():
    # return render_template('index.html')    
    # result = loaded_model_2.recommend_p('9bb911319fbc04f01755814cb5edb21df3d1a336');
    # return result.values.to_list();
    return render_template("user_select.html")
    # return(len(result));
    #return "Hello World"


@app.route('/user_re',methods = ['POST'])
def user_re():
    if request.method == 'POST':
        user_id = request.form.get("user_id")
        # return song_name
        result = loaded_model.recommend_s(user_id); 
        return render_template("user_recommend.html",foobar=result)

if __name__ == "__main__":
	app.run(debug=True)