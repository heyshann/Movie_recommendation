
from flask import Flask , render_template, request
import pickle
import pandas as pd

model=pickle.load(open('similarity.pkl',"rb"))
movielist = pickle.load(open("movie_list.pkl", 'rb'))

def recommend(movie):
    result=[]
    index = movielist[movielist['title'] == movie].index[0]
    distances = sorted(list(enumerate(model[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:  # top 5 related movie
        result.append(movielist.iloc[i[0]].title)
    return result





app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')   


@app.route('/predict',methods=['POST'])



def pred():
    movie=request.form.get("tags")
    results=recommend(movie)
    
    return render_template('predict.html',result=results)


if __name__=="__main__":
    app.run(debug=True)
