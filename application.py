from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/trans', methods=['POST'])
def fanyi():
    import mt
    transText = mt.mtChinese(request.form['yuanwen'])
    print("fanyi()", transText, "***")
    return transText

@app.route('/')
def index():
    print("index()")
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=6464)
    #外部可访问。  app.run() #外部不可访问
