import requests
from flask import Flask,render_template




app = Flask(__name__)
define_port = 80
@app.route('/')
def index():
    
    
    
    response = requests.get("https://meme-api.com/gimme/ProgrammerHumor").json()
    meme_pic = response['preview'][2]
    meme_author = response['author']  
    meme_title = response['title']
     
    return render_template("index.html",meme_pic=meme_pic,meme_author=meme_author,meme_title=meme_title,port=define_port)
  
app.run(host='0.0.0.0',port=define_port)