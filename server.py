from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1 style ="text-align:center">Welcome to Playground,add /play to the end of the url<h1>'
@app.route('/play')
def playboxlvl1():
    return render_template('index.html',num = 3,color = 'lightblue')
@app.route('/play/<int:num>')
def playboxlvl2(num):
    return render_template('index.html',num = num, color = 'gold')
@app.route('/play/<int:num>/<string:color>')
def playboxlvl3(num,color):
    return render_template('index.html', num=num,color=color)






if __name__ == "__main__":
    app.run(debug=True)
