from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/trans', methods=['POST'])
def fanyi():
    yuanwen = request.form['yuanwen']
    print("fanyi()", yuanwen, "***")
    return "123456"

@app.route('/')
def index():
    print("index()")
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
    #外部可访问。  app.run() #外部不可访问
