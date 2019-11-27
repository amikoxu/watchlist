from flask import Flask, render_template

app = Flask(__name__)

name = "xu"
movies = [
    {'title':'my neirbor toroto','year':'1998'},
    {'title':'dead poet society','year':'1989'},
    {'title':'a perfect world','year':'1993'},
    {'title':'mahjong','year':'1996'},
    {'title':'the pork of music','year':'2012'}
    ]

@app.route('/')
def index():
    
    return render_template('index.html',name=name,movies=movies)

