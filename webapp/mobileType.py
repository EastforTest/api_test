import requests
from lxml import etree
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/index3")
def index3():
    return render_template("index3.html")

@app.route("/moblieType")
def moblieType():
    phone = request.args.get("phone")
    data = getMoblieType(phone)
    return '<br/>'.join(data)



def getMoblieType(phone):
    #伪造访问UA
    headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
    #发送请求
    reqes = requests.get(f"https://ip138.com/mobile.asp?mobile={phone}&action=mobile",headers=headers)

    #设置编码格式
    reqes.encoding = "utf-8"

    e = etree.HTML(reqes.text)
    datas = e.xpath("//tr/td[2]/a/text()")

    return datas

app.run(debug=True)