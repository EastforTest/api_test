import random

from flask import Flask,render_template,request

app = Flask(__name__)

data = ['19018420040','19018420040','19018420037','19018420038','19018420039','19018420036','19018420034','19018420033','19018420028','19018420032','19018420032','19018420030']

@app.route('/index')
def index():
    #return render_template('index.html',data1=data)
    uname = request.args.get("uname")
    return f"欢迎{uname}，登录首页"

@app.route("/choujiang")
def choujiang():
    num = random.randint(0,len(data)-1)
    return render_template('index.html',data1=data,data=data[num])

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)
